#!/usr/bin/env python3
"""Calibration optique et mesure de déformation de damier sous différentes hauteurs d'eau.

Idée physique :
- La surface libre se déforme sous l'effet des variations de pression.
- La lumière est réfractée à l'interface eau/air (loi de Snell-Descartes).
- Cette réfraction décale la position apparente des coins du damier filmé.
- En comparant la géométrie apparente à un état de référence, on quantifie une
  déformation optique corrélée à la variation de hauteur locale (et donc de pression).

Ce script reste volontairement léger (OpenCV + NumPy) pour tourner sur un PC étudiant.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path
from typing import List, Tuple

import cv2
import numpy as np


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Détecte un damier sur une série d'images de calibration et calcule "
            "la déformation des coins par rapport à une référence."
        )
    )
    parser.add_argument(
        "--images-dir",
        type=Path,
        default=Path("data/calibration"),
        help="Dossier contenant les images de calibration.",
    )
    parser.add_argument(
        "--pattern-size",
        nargs=2,
        type=int,
        default=(9, 6),
        metavar=("COLS", "ROWS"),
        help="Nombre de coins internes du damier (colonnes lignes).",
    )
    parser.add_argument(
        "--square-size-mm",
        type=float,
        default=10.0,
        help="Taille réelle d'un carré (mm), utilisée pour la calibration caméra.",
    )
    parser.add_argument(
        "--reference-regex",
        type=str,
        default=r"(h0|h_?0mm|ref|reference)",
        help="Regex pour identifier l'image de référence (eau statique).",
    )
    parser.add_argument(
        "--output-csv",
        type=Path,
        default=Path("data/calibration/deformation_summary.csv"),
        help="Fichier CSV de sortie des métriques de déformation.",
    )
    parser.add_argument(
        "--max-images",
        type=int,
        default=0,
        help="Limite le nombre d'images traitées (0 = toutes).",
    )
    return parser.parse_args()


def list_images(images_dir: Path) -> List[Path]:
    exts = {".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff"}
    images = sorted([p for p in images_dir.iterdir() if p.suffix.lower() in exts])
    return images


def detect_chessboard_corners(
    image_path: Path, pattern_size: Tuple[int, int]
) -> Tuple[bool, np.ndarray | None, Tuple[int, int]]:
    gray = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
    if gray is None:
        return False, None, (0, 0)

    flags = cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_NORMALIZE_IMAGE
    found, corners = cv2.findChessboardCorners(gray, pattern_size, flags)
    if not found:
        return False, None, gray.shape[::-1]

    # Raffinage subpixel : améliore la précision de la géométrie apparente,
    # donc la qualité du calcul de déformation optique.
    criteria = (
        cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
        30,
        1e-3,
    )
    cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
    return True, corners.reshape(-1, 2), gray.shape[::-1]


def extract_height_mm(filename: str) -> float | None:
    """Extrait une hauteur depuis le nom de fichier (ex: h20mm, 15mm, h_5.5)."""
    patterns = [
        r"h[_-]?(\d+(?:\.\d+)?)mm",
        r"(\d+(?:\.\d+)?)mm",
        r"h[_-]?(\d+(?:\.\d+)?)",
    ]
    name = filename.lower()
    for pattern in patterns:
        match = re.search(pattern, name)
        if match:
            return float(match.group(1))
    return None


def build_object_points(pattern_size: Tuple[int, int], square_size_mm: float) -> np.ndarray:
    cols, rows = pattern_size
    objp = np.zeros((rows * cols, 3), np.float32)
    grid = np.mgrid[0:cols, 0:rows].T.reshape(-1, 2)
    objp[:, :2] = grid * square_size_mm
    return objp


def choose_reference_image(images: List[Path], regex: str) -> Path:
    compiled = re.compile(regex, re.IGNORECASE)
    for image in images:
        if compiled.search(image.stem):
            return image
    return images[0]


def calibrate_camera(
    object_points: List[np.ndarray],
    image_points: List[np.ndarray],
    image_size: Tuple[int, int],
) -> Tuple[float, np.ndarray, np.ndarray]:
    rms, camera_matrix, dist_coeffs, _, _ = cv2.calibrateCamera(
        object_points, image_points, image_size, None, None
    )
    return rms, camera_matrix, dist_coeffs


def main() -> None:
    args = parse_args()

    images_dir = args.images_dir
    if not images_dir.exists():
        raise FileNotFoundError(f"Dossier introuvable: {images_dir}")

    image_paths = list_images(images_dir)
    if not image_paths:
        raise RuntimeError(f"Aucune image de calibration trouvée dans {images_dir}")

    if args.max_images > 0:
        image_paths = image_paths[: args.max_images]

    reference_image = choose_reference_image(image_paths, args.reference_regex)

    pattern_size = tuple(args.pattern_size)
    objp = build_object_points(pattern_size, args.square_size_mm)

    detections = {}
    image_size = None

    for image_path in image_paths:
        found, corners, size = detect_chessboard_corners(image_path, pattern_size)
        if found and corners is not None:
            detections[image_path] = corners
            if image_size is None:
                image_size = size

    if reference_image not in detections:
        raise RuntimeError(
            "Image de référence sans damier détecté. Ajustez --reference-regex "
            "ou la qualité des images."
        )

    if len(detections) < 3 or image_size is None:
        raise RuntimeError("Pas assez d'images valides pour calibrer la caméra (min 3).")

    # Calibration intrinsèque : retire les biais optiques de la caméra
    # (distorsion radiale/tangentielle) avant d'interpréter la physique du bassin.
    object_points = [objp.copy() for _ in detections]
    image_points = [corners.reshape(-1, 1, 2).astype(np.float32) for corners in detections.values()]
    rms, camera_matrix, dist_coeffs = calibrate_camera(object_points, image_points, image_size)

    ref_corners = detections[reference_image]

    rows = []
    for image_path, corners in detections.items():
        # Déformation optique = déplacement apparent des mêmes coins du damier
        # entre l'état de référence et l'état courant.
        displacement = corners - ref_corners
        norm = np.linalg.norm(displacement, axis=1)

        rows.append(
            {
                "image": image_path.name,
                "height_mm": extract_height_mm(image_path.stem),
                "mean_disp_px": float(np.mean(norm)),
                "max_disp_px": float(np.max(norm)),
                "std_disp_px": float(np.std(norm)),
            }
        )

    rows.sort(
        key=lambda r: (
            float("inf") if r["height_mm"] is None else r["height_mm"],
            r["image"],
        )
    )

    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["image", "height_mm", "mean_disp_px", "max_disp_px", "std_disp_px"],
        )
        writer.writeheader()
        writer.writerows(rows)

    print("=== Calibration terminée ===")
    print(f"Images valides: {len(detections)}/{len(image_paths)}")
    print(f"Image de référence: {reference_image.name}")
    print(f"RMS reprojection error (px): {rms:.4f}")
    print("Matrice caméra:\n", camera_matrix)
    print("Coefficients de distorsion:\n", dist_coeffs.ravel())
    print(f"CSV écrit: {args.output_csv}")


if __name__ == "__main__":
    main()
