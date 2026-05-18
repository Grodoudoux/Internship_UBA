## Delft University of Technology 

## A dot tracking algorithm to measure free surface deformations 

Charruault, Florian; Greidanus, Arnoud; Breugem, Wim-Paul; Westerweel, Jerry 

DOI 

10.3929/ethz-b-000279140 Publication date 2018 Document Version Final published version 

Published in Proceedings 18th International Symposium on Flow Visualization 

## Citation (APA) 

Charruault, F., Greidanus, A., Breugem, W.-P., & Westerweel, J. (2018). A dot tracking algorithm to measure free surface deformations. In T. Rösgen (Ed.), Proceedings 18th International Symposium on Flow Visualization ETH Zürich. https://doi.org/10.3929/ethz-b-000279140 

## Important note 

To cite this publication, please use the final published version (if applicable). Please check the document version above. 

Copyright 

Other than for strictly personal use, it is not permitted to download, forward or distribute the text or part of it, without the consent of the author(s) and/or copyright holder(s), unless the work is under an open content license such as Creative Commons. Takedown policy Please contact us and provide details if you believe this document breaches copyrights. We will remove access to the work immediately and investigate your claim. 

This work is downloaded from Delft University of Technology. For technical reasons the number of authors shown on this cover page is limited to a maximum of 10. 

18[th] International Symposium on Flow Visualization Zurich, Switzerland, June 26-29, 2018 

**==> picture [43 x 58] intentionally omitted <==**

## **A DOT TRACKING ALGORITHM TO MEASURE FREE SURFACE DEFORMATIONS** 

F. Charruault[1,c] , A. J. Greidanus[1] , W-P. Breugem[1] , J. Westerweel[1] 

1Laboratory for Aero and Hydrodynamics, TU Delft, 2628 CD Delft, The Netherlands cCorresponding author: Tel.: +31 152784766; mail:F.T.Charruault@tudelft.nl 

## **KEYWORDS:** 

**Main subjects** : free surface measurements, flow visualization **Fluid:** turbulent flow, air/water interface **Visualization method(s):** Background oriented Schlieren, Free Surface-Synthetic Schlieren **Other keywords:** DIC, PTV, DTA, air cavity, coating 

**ABSTRACT** : _The present study introduces an experimental technique based on a Free Surface-Synthetic Schlieren (FS-SS) method in order to characterize free surfaces subjected to strong deformations. Current synthetic Schlieren methods are based on local image correlation and thus limited to rather weak image deformations, implying that they can only resolve rather large surface wavelengths and limited wave amplitude. The present method is a substantial improvement that allows to measure much stronger image deformations, providing access to shorter surface wavelengths and larger amplitudes (i.e. larger surface curvatures)._ 

## **1 Introduction** 

## **1.1 General introduction** 

Random dot patterns are commonly used in synthetic Schlieren methods to measure free surface heights. The apparent deformation/displacement of a pattern, for instance a random dot pattern, induced by the refraction of light through the interface is usually computed via a Digital Image Correlation (DIC) technique. The latest has been proven to be very robust and accurate but is limited to rather weak deformations as observed by [1]. They show that for values of the absolute principal strain tensor higher than 𝜎𝑟𝑚𝑠 > 0.15, standard DIC algorithms fail to provide reliable results. This can be explained by the fact that correlation techniques average out the displacement of dots within interrogation windows. This situation would typically occur when one would try to reconstruct the free surface of an air cavity (i.e. a thin elongated air layer generated behind a small obstruction in the flow which separates the wall from the outer water flow) (see Fig. 1). 

In this paper, we present the limiting parameters of such a method and we explain how some of them can be tackled by using a Dot Tracking Algorithm (DTA). The latter is based on a simple nearest neighbour approach coupled to a bootstrapping correction which allows us to match pairs of dots between the deformed and undeformed dot pattern. The method is validated with synthetic data and we show that the method works well to reconstruct the interface of a compliant coating. Finally, we apply the method to an air cavity where the deformations are strong and beyond the DIC limit [1]. 

## **1.2 Background** 

It is known that free surface deformation measurements are challenging. Researchers have tried several techniques but none of them is able to measure a wide range of wave heights and wave lengths. 

ISFV18 – Zurich, Switzerland – 2018 

1 

F. Charruault, A.J. Greidanus, W-P. Breugem, J. Westerweel 

However, various non intrusive methods have been developed over the years. There are mainly optical techniques using the reflecting or refractive properties of a transparent interface ( [2], [3], [1], [4]). Among those, one has lately received great interest due to its simplicity and adaptability. This method has been called Free Surface-Synthetic Schlieren (FS-SS) and has been introduced by [1]. The 

**==> picture [483 x 237] intentionally omitted <==**

**Fig. 1. Left: picture and sketch of the experimental setup. One can see the cavity developing downstream of the cavitator. The dot pattern is placed on top of the closure region. On the right, one can see a typical synthetic Schlieren image of an air cavity** 

principal relies on the well-known Background Oriented Schlieren method (BOS) ( [4], [5]). It makes use of the apparent displacement of a Random Dot Pattern (RDP) seen through the interface separating two immiscible media with different densities. They showed that the surface gradient was directly proportional to the apparent displacement field of the synthetic background. The method has shown great potential to study free surface deformations ( [6], [7]). It is robust, requires only one camera and relatively easy to use. Nevertheless, it is limited to rather large surface wave lengths and small surface amplitudes (i.e. low curvatures:𝜎𝑟𝑚𝑠 < 0.15, [1]). Indeed, the computation of the displacement field is ∆𝑋 based on image correlation allowing only weak displacement gradients ( < 3% where ∆𝑋 is the local 𝑑𝐼 

displacement variation and 𝑑𝐼 the interrogation window size) as mentioned by [8]. In order to satisfy this constraint, the interrogation windows have to be sufficiently small. Nevertheless, the size of the interrogation window is also restrained by the image density (i.e. the amount of particles/dots per unit area) which should be bigger than 5 per interrogation window if one desire more than 95% of valid vectors [9]. Consequently, the method is suited for either overall constant shifts of the RDP or for local weak deformations. In other words, DIC methods only detect a translation of two image patterned but not rotation and/or local compression/expansion. These limitations are illustrated with a simple example; the apparent deformation of a RDP induced the refraction of light through a concave lens is shown in Fig. 2. In order to compute the displacement field with a standard DIC method one would need to divide the image into interrogation windows. Fig. 2(a),(b) show an interrogation window taken from a snapshot obtained by a CCD camera with a resolution of 4 Megapixels placed at about 1 _._ 5 m. 

ISFV18 – Zurich, Switzerland – 2018 

2 

A DOT TRACKING ALGORITHM TO MEASURE  FREE SURFACE DEFORMATIONS 

This interrogation window is centered with the main axis of the lens. This situation could typically happen when using the FS-SS. Fig. 2(a) shows the undeformed interrogation window (without the concave lens). 

**==> picture [374 x 292] intentionally omitted <==**

**Fig. 2. (a) Typical interrogation window originating from a random dot pattern seen by a CCD. (b) apparent deformation of the pattern induced by the refraction of light through a concave lens. (c) Cross-correlation between the interrogation windows (a) and (b)** 

In order to compute the displacement between these two images, one could compute the 2D cross correlation between these two images. This would result in the correlation map plotted in Fig. 2(c). Namely, a weak noisy peak with almost zero shift. Indeed, since the lens has a central symmetry, the overall apparent displacement field is zero but locally the lens induces a variable magnification over the image which can be seen as a strong, non-uniform inward displacement (Fig. 2(b)). This situation would typically happen when one would look at the apparent deformation of a RDP induced by a wavy free surface. In other words, an interrogation window that would be centered on a valley or on a peak of a wavy surface would give a nearly zero displacement. One way to surpass this limit would be to use smaller interrogation windows. Nevertheless, the limited resolution of the printer to create the RDP and of the camera do not allow to substantially reduce the interrogation window size. Therefore, in order to increase the spatial resolution and to avoid any non-desired displacement gradient smoothing, we implemented an algorithm based on a Particle Tracking Velocimetry (PTV) approach where the location of the dots is known a priori. This will allow us to compute the displacement of every individual dot. There exist multiple PTV algorithms which can be differentiated into different classes: the relaxation methods [10], the nearest neighbor algorithm [11], the particle distribution methods [12] and the multi-frame methods [13], [14]. The current study makes use of a PTV-like algorithm that is based on an adaptive nearest neighbor search approach which is one of the most robust and simplest 

ISFV18 – Zurich, Switzerland – 2018 

3 

F. Charruault, A.J. Greidanus, W-P. Breugem, J. Westerweel 

approach especially when the location of all the dots is known a priori. We track individual dots that are randomly distributed on a pattern. This enables us to measure stronger displacement gradients and therefore stronger curvatures. This paper is structured as follows: the first part describes the principle of the Dot Tracking Algorithm (DTA) with simple examples while the second part shows an application where both an in-house DIC algorithm ( [9]) and our DTA work. Finally, we perform a challenging experiment where the DIC clearly fails and where the DTA helps us to compute more accurately the displacement of a random dot pattern. 

## **2 The Dot Tracking Algorithm (DTA)** 

## **2.1 Adaptive nearest neighbor approach** 

The essence of the method is based on a simple nearest neighbor search. Its novelty lies in the adaptive estimation of the location of the next pair of dots. The nearest neighbor interpolation function is built up iteratively during the matching procedure. Let us position the lens shown in Fig. 2 on top of three dots that forms an equilateral triangle (P1', P2', P3') centered with the interrogation window (see Fig. 3). An observer placed above the interface will see the dots moving inward (P1, P2, P3). Let us assume that the first match is known (i.e. the pair P1'P1). 

**==> picture [196 x 283] intentionally omitted <==**

**Fig. 3. Cartoon showing the different steps required by the algorithm in a chronological order (from (1) to (5)). The centroids of the displaced and non-displaced dots are shown by closed and open symbols respectively. The red vectors are the actual displacement. The blue vectors show the estimated displacement** 

One can estimate the location of the next two pairs using 𝜹1 = 𝑃1 −𝑃1′. The nearest neighbors to _I_ 1 and _I_ 2 (the dots located within C1 and C2 which are the shortest radii containing dots), are then considered as matches of _P_ 2' and _P_ 3' . If one adds an extra dot _P_ 4', one can estimate more accurately the location of its match _P_ 4 by interpolating the displacement vectors that have already been found. By 

ISFV18 – Zurich, Switzerland – 2018 

4 

A DOT TRACKING ALGORITHM TO MEASURE  FREE SURFACE DEFORMATIONS 

doing so, one can build up an interpolation function which is updated every time that two dots are paired. 

## **2.2 Bootstrapping validation** 

In the previous example, we assumed that the first pair of dots was known. Nevertheless, when dealing with real images, this has to be determined. In order to do so, we test every possible first match within a search region. Each test leads to a unique displacement field which can be used to dewarp the deformed region. The search regions are dewarped using the interpolated displacement fields onto a cartesian grid with a spacing of one pixel. The reconstructed regions can then be cross-correlated with the underformed regions; the highest correlation peak then indicates the correct match. Examples of a correct initialization and wrong initialization are given in Fig. 4 and 5 respectively. 

**==> picture [284 x 103] intentionally omitted <==**

**Fig. 4. (a) Displaced and non-displaced centroids (full and open symbols respectively) belonging to Fig. 2 and their actual correct displacement (red vectors) from a correct initialization (blue vector). (b) dewarped image from the interpolated displacement field seen in (a). (c) cross-correlation between the dewarped image (b) and the reference image Fig. 2(a)** 

**==> picture [284 x 103] intentionally omitted <==**

**Fig. 5.  (a) Displaced and non-displaced centroids (full and open symbols respectively) belonging to Fig. 2. Vector field (in red) resulting from a wrong initialization (blue vector). (b) dewarped image from the interpolated displacement field seen in (a). (c) cross-correlation between the dewarped image (b) and the reference image Fig. 2(a)** 

## **2.3 Search regions** 

In the previous section, we mentioned  search regions in which we limited the matching procedure. These are necessary in order to keep the displacement gradient as small as possible within these regions. Therefore, we generate search regions that are Voronoi cells defined by local maxima (called sites of the Voronoi cells) of the random dot density map. The density map is given by the local density ratio between the number of dots in the deformed image and the number of dots in the undeformed image. To compute the local density ratio we divide the images into interrogation windows in which we count the number of dots. An example of a typical synthetic Schlieren image is given in Fig. 6(a). Interestingly, one can already qualitatively study the topography of the interface with the density map (Fig. 6(b)). 

ISFV18 – Zurich, Switzerland – 2018 

5 

F. Charruault, A.J. Greidanus, W-P. Breugem, J. Westerweel 

**==> picture [368 x 319] intentionally omitted <==**

**Fig. 6. (a) Typical synthetic deformed image. (b) density map of the deformed image and its peaks (white crosses) and valleys (green crosses). (c) deformed image and its search regions (green dashed line) which are Voronoi cells based on the distance between the valleys (green crosses). (d) actual displacement field computed by the DTA. The colors show the magnitude of the vectors in pixels** 

In Fig. 6(c) we show the local maxima and local minima of a typical deformed random dot pattern together with its Voronoi cells. We also shows the displacement field resulting from the DTA. We clearly see that it is able to match all the dots even though the local displacement are substantial (up to 22 pixels). 

## **3 Measurement of weak deformations** 

## **3.1 Experimental setup** 

We performed experiments at the cavitation tunnel of the Delft University of Technology in order to measure the deformations of a compliant coating. The cavitation tunnel allows us to perform measurements up to 7 m.s[−1] . The test section is 2 m long and has a cross-sectional area of 300 × 300 mm[2] . The velocity is set via a differential pressure sensor located in the contraction of the tunnel and controlled via a Proportional Integrator controller. A detailed description of the cavitation tunnel is given by [15]. The test section used for our experiment is open on the top, which enables us to mount different flat plates in order to measure the hydrodynamic drag of different surfaces. It has been designed by [16] in order to study the drag reduction by so-called air cavities. The original design has been improved in order to perform more accurate drag measurements. A fully turbulent boundary layer develops along the coating. The bottom wall is sloped in order to account for the growth of the 

ISFV18 – Zurich, Switzerland – 2018 

6 

A DOT TRACKING ALGORITHM TO MEASURE  FREE SURFACE DEFORMATIONS 

boundary layer. Therefore the inlet of the test section has a cross sectional area of 300×300 mm[2] whereas the outlet has a cross sectional area of 300×315 mm[2] . The bulk velocity in the test section is determined from PIV measurements performed at three different locations (at _x_ = 0 _._ 2 m, _x_ = 1 _._ 0 m, _x_ = 1 _._ 7 m from the leading edge of the plate). The same random dot pattern shown in Fig. 1 has been used to compute the displacement field. It is separated from the coating interface by a layer of polycarbonate (10 mm thick) and an extra layer of glass (2 mm thick) which allows us to magnify the displacement field. A sketch of the setup is given in Fig. 1 Note that for the current experiment, the test plate is not the one drawn in Fig. 1. but the one mentioned earlier. The camera is placed at H = 1400 mm in order to comply with the paraxial approximation [1]. 

## **3.2 Deformation of a compliant coating** 

In order to show that our algorithm works well for mild deformations, we first perform experiments on a compliant coating applied on a flat poly-carbonate plate which has an area of 1998×297 mm[2] . We recorded images at 1200 Hz with a 4 Megapixels camera. For this specific test, the bulk velocity is equal to 5.26 m.s[-1] . A typical image resulting from this experiment is shown in Fig. 7. 

**==> picture [228 x 206] intentionally omitted <==**

**Fig. 7. Typical BOS image taken by a CCD camera. The deformations of the pattern are induced by light refraction through a compliant coating. The displayed pattern size is about 7 × 7 cm[2] . U0 indicates the direction of the water flow** 

Furthermore, it is possible to identify the peaks and valleys of waves travelling on the coating interface which result in magnified regions and compressed regions respectively. The physics beyond this phenomena is described in [17] and [18]. The first step of the algorithm is the computation of the dot density map, which will allow us to define search regions. To do so, we divide the image into interrogation windows of 60×60 pixels with 80% overlap. The result is plotted in Fig. 8(a). Interestingly, the wave topography associated with the deformed dot pattern can already be qualitatively studied from the density map. Using the DTA, we further compute the displacement field which is shown in Fig. 8(b). The algorithm successfully match more than 90% of the dots (among about 60000) (Fig. 8(a)). The unresolved regions (Fig. 8(b)) can be interpolated using an appropriate interpolation scheme. 

ISFV18 – Zurich, Switzerland – 2018 

7 

F. Charruault, A.J. Greidanus, W-P. Breugem, J. Westerweel 

**==> picture [424 x 165] intentionally omitted <==**

**Fig. 8. (a) local image density of the patterned picture shown in Fig. 7.  (b) actual displacement field of the same image computed with the DTA. The colors indicate the magnitude of the vectors in terms of pixels** 

## **3.3 Error assessment** 

So far, we have studied qualitatively the accuracy of the DTA. Therefore, in this section we use the method proposed by [19] to assess the quality of the displacement fields generated by the DTA. Similarly to the technique used in Sec. 2.2 to reconstruct the undeformed region, the displacement can be interpolated in order to dewarp back the image. 

**==> picture [333 x 201] intentionally omitted <==**

**Fig. 9. Histogram of the maximum correlation peaks when computing the cross correlation between the reference undeformed image and the deformed image (Fig. 7). Here we used interrogation windows of 32×32 pixels with 50% overlap. The contour plots represent the normalized cross correlation maps of the image shown in Fig. 7 computed from the PIV displacement field and the DTA displacement field. The colors indicate the height of the normalized correlation peaks. The largest absolute principal component of the strain tensor is equal to 0.3** 

We compare our algorithm to a standard in-house DIC algorithm [9]. We chose interrogation windows of 32×32 pixels with 50% overlap. The results are shown in Fig. 9. The DIC and DTA algorithm display similar results. They both perform well, exhibiting correlation peaks contained in R = [0.8:1.0] which is very satisfactory. The largest absolute principal component of the strain tensor is equal to 0.34 in this case. This is twice larger than the criteria defined by [1]. The fact that both algorithms work fine 

ISFV18 – Zurich, Switzerland – 2018 

8 

A DOT TRACKING ALGORITHM TO MEASURE  FREE SURFACE DEFORMATIONS 

can be explained first of all by the lower density of the dot pattern which avoids overlaps of the dots but also by the scattered distribution of the waves. Indeed, for scattered waves, the displacement field around one wave crest will be computed accurately allowing the detection of outliers on the crest. 

## **4. Strong deformation** 

## **4.1. Deformation of an air cavity** 

We studied mild to strong deformations in the previous section and we showed that both DIC and DTA methods  worked well. Our main motivation was to measure the deformations of a RDP induced by an air cavity interface. To do so, we performed a synthetic Schlieren experiment (shown in Fig. 1) at the cavity closure. The cavity is generated by injection of air downstream of a so-called cavitator placed 25 cm downstream of the leading edge of the plate. The frame rate of the CCD camera is 1700 Hz and its resolution is 4 Megapixels. 

**==> picture [339 x 307] intentionally omitted <==**

**Fig. 10. Different regions characterizing a typical random dot pattern deformed by the refraction of light through an air cavity interface. The complete image can be seen in Fig. 1. The vector fields represent the displacement fields computed via the DTA. (a) wet region downstream of the cavity closure. (b) contact line at the cavity closure. (c) mild to strong deformation of the pattern. (d) strong deformation of the pattern** 

A complete description of the setup can be found in **[16]** . The field of view is about 7 × 7 cm[2] . As it can be seen in Fig. 1 and Fig. 10, the waves travelling on the interface are inhomogeneously distributed in contrast with the compliant coating case. Therefore, the pattern is also inhomogeneously deformed (Fig. 1 and 10) and four different regions can be identified. These regions characterize the air cavity 

ISFV18 – Zurich, Switzerland – 2018 

9 

F. Charruault, A.J. Greidanus, W-P. Breugem, J. Westerweel 

and are the following: (a) the wet region downstream of the cavity closure where the apparent displacement of the pattern is zero; (b) the cavity closure or contact line where the dot pattern is strongly deformed or not visible; (c) a mild to strong deformation region; (d) a strongly deformed region where the dot are elongated. 

**==> picture [413 x 163] intentionally omitted <==**

**Fig. 11. (a) local image density of the patterned picture shown in Fig. 1. (b) actual displacement of the same image, computed with the DTA. For clarity, we only show a small representative region. The colors show the magnitude of the vectors in terms of pixels** 

The density map is given in Fig. 11(a) and shows large variations from 0 _._ 4 to 1 _._ 6 which means that within an interrogation window one could find 60 % lower or 60 % higher number of dots than observed in the reference image. Note that the wave pattern can be qualitatively identify with the density map as well as the cavity closure. By refining the interrogation windows one could identify accurately the contact line. 

## **4.2 DIC versus DTA** 

In order to compare both algorithms, we use the method presented in Sec 3.3 and introduced by **[19]** . The results are shown in the form of a histogram and correlation maps (see Fig. 12). For this specific experiment, we used interrogation windows of 16 × 16 pixels with 50% overlap. Clearly, the accuracy of both methods is lower with such a deformed image than with the image studied in Sec. 3. The correlation peaks span quite evenly from 0 _._ 2 to 0 _._ 9 with a large peak around 0 _._ 98. The latest corresponds to the wet region (the region downstream of the cavity closure) where no cavity is present and therefore where the dots have not moved. However, the amount of correlation peaks that has values between _R_ = [0 _._ 6 : 0 _._ 96], is higher for the DTA than for the DIC. This is also notable in the correlation maps. The area covered by correlation peaks higher than 0 _._ 5 is bigger in the DTA map. The algorithm fails mainly in the region of substantially low image density. Therefore, neither our DTA or our DIC algorithm would be able to extract quantitative information from these areas. Nevertheless, from the image density map, one can identify these regions in order to discard them from the analysis. Furthermore, it is questionable whether the assessment of the error is correct in this particular case. Indeed, we used a linear interpolation scheme with a grid spacing equal to 1px to dewarp the deformed image. This scheme might not be suited for regions of large strain. One may considered using a higher order scheme in order to account for such deformations. 

ISFV18 – Zurich, Switzerland – 2018 

10 

A DOT TRACKING ALGORITHM TO MEASURE  FREE SURFACE DEFORMATIONS 

**==> picture [483 x 289] intentionally omitted <==**

**Fig. 12. Histogram of the maximum correlation peaks when computing the cross correlation between the reference undeformed image and the deformed image (Fig. 1). Here we used interrogation windows of 16×16px with 50% overlap. The contour plots represent the normalized cross correlation maps of the image shown in Fig. 1 computed from the PIV displacement field and the DTA displacement field** 

## **5. Conclusion** 

Synthetic Schlieren methods are promising techniques and have been used successfully to measure density variations of a fluid. Lately, the method has been applied to free surface measurements making use of the fluid density jump between two media. In other words, they used the refraction properties of transparent media [1]. The experimental method is promising and can be used for various applications. In order to measure the apparent displacement of a synthetic Schlieren pattern (for instance a Random Dot Pattern), an algorithm based on Digital Image Correlation (DIC) is used. The latest is widely used for Particle Image Velocimetry measurements and shows a great robustness and a high accuracy. Nevertheless, the method suffers from local averaging which disable the possibility of measuring strong velocity gradients or strong image deformations (with strain 𝜎𝑟𝑚𝑠 > 0.15) for our specific application. Therefore, we implemented a Dot Tracking Algorithm (DTA) which is able to track individual dots randomly distributed and subjected to rather strong displacement gradients. The algorithm is based on an adaptive nearest neighbor approach and is performed within search regions that are formed by Voronoi cells distributed with respect to local maxima of the image density. An additional bootstrapping step makes this algorithm fully automatized. The only input parameters required are the two synthetic Schlieren images (the reference image and the deformed image). In order to assess the capabilities of the method, we performed two different experiments involving two different interface deformations. The first one is the mild deformation of a compliant coating which showed similar results between our algorithm and an algorithm based on a DIC. However, when 

ISFV18 – Zurich, Switzerland – 2018 

11 

F. Charruault, A.J. Greidanus, W-P. Breugem, J. Westerweel 

measuring stronger deformations, namely deformations induced by an air cavity, the DTA showed that it could compute a higher number of vectors correctly compared to the DIC algorithm. Furthermore, it is important to note that the algorithm could be improved by tracking also the dots that are strongly deformed. A more suited interpolation scheme would also allow to estimate better the location of the next pair of dots (see Sec. 2). Finally, even though the DTA is much slower than a standard DIC algorithm, it can be easily parallelized given that the displacement fields can be computed independently in each Voronoi cell. 

## **References** 

- [1]  F. Moisy, M. Rabaud and K. Salsac, “A synthetic schlieren method for the measurement of the topography of a liquid interface,” _Experiments in Fluids,_ vol. 46, p. 1021–1036, 2009. 

- [2]  J. Liu, J. Paul and J. Gollub, “Measurements of the primary instabilities of film flows,” _Journal of Fluid Mechanics,_ no. 250, pp. 69-101, 1993. 

- [3]  J. Kurata, K. Grattan, H. Uchiyama and T. Tanaka, “Water surface measurement in a shallow channel using the transmitted image of a grating,” _Review of Scientific Instruments,_ vol. 61, p. 736, 1990. 

- [4]  M. Raffel, “Background-oriented schlieren (bos) techniques,” _Experiments in Fluids,_ vol. 56, 2015. 

- [5]  H. Richard and M. Raffel, “Principle and applications of the background oriented schlieren (bos) method,” _Measurement Science and Technology,_ vol. 12, 2001. 

- [6]  F. Moisy, G. Michon, M. Rabaud and E. Sultan, “Cross-waves induced by the vertical oscillation of a fully immersed vertical plate,” _Physics of Fluids,_ vol. 24, 2012. 

- [7]  A. Paquier, F. Moisy and M. Rabaud, “Surface deformations and wave generation by wind blowing over a viscous liquid,” _Physics of Fluids,_ vol. 17, 2015. 

- [8]  G. Settles and M. Hargather, “A review of recent developments in schlieren and shadowgraph techniques,” _Measurement Science and Technology,_ vol. 28, 2017. 

- [9]  R. Adrian and J. Westerweel, Particle Image Velocimetry, Cambridge University Press, 2011. 

- [10] K. Ohmi and H. Li, “Particle-tracking velocimetry with new algorithms,” _Measurements Science and Technology,_ vol. 11, 2000. 

- [11] F. Pereira, H. Staijer, E. Graff and M. Gharib, “Two-frame 3d particle tracking,” _Measurements Science and Technology,_ vol. 17, 2006. 

- [12] K. Okamoto, Y. Hassan and W. Schmidl, “New tracking algorithm for particle image velocimetry,” _Experiments in Fluids,_ vol. 19, pp. 342-347, 1995. 

- [13] Y. Hassan and R. Canaan, “Full-field bubbly flow velocity measurements using a multiframe particl tracking technique,” _Experiments in Fluids,_ vol. 12, pp. 49-60, 1991. 

- [14] C. Cierpka, B. Lütke and K. CJ, “Higher order multi-frame particle tracking velocimetry,” _Experiments in Fluids,_ no. 54, 2013. 

- [15] E. Foeth, “The structure of three-dimensional sheet cavitation,” PhD thesis, Delft University of Technology, 2008. 

- [16] O. Zverkhovskyi, “Ship drag reduction by air cavities,” Delft University of Technology, 2014. 

- [17] R. Delfos, A. J. Greidanus, F. Charruault and J. Westerweel, “Wave characteristics of a compliant 

ISFV18 – Zurich, Switzerland – 2018 

12 

A DOT TRACKING ALGORITHM TO MEASURE  FREE SURFACE DEFORMATIONS 

coating under a turbulent flow,” in _The 5th International Conference on Advanced Model Measurement Technology for the Maritime Industry_ , Glasgow, 2017. 

- [18] A. J. Greidanus, R. Delfos and J. Westerweel, “Fluid-structure interaction of compliant coating under turbulent flow conditions: force and piv analysis,” in _The 5th International Conference on Advanced Model Measurements Technology for the Maritime Industry_ , Glasgow, 2017. 

- [19] B. Wieneke, “Piv uncertainty quantification from correlation statistics,” _Experiments in Fluids,_ vol. 26, 2015. 

ISFV18 – Zurich, Switzerland – 2018 

13 

