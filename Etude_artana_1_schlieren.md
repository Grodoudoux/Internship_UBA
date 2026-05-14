**==> picture [242 x 136] intentionally omitted <==**

**A Fluid Motion Estimator for Schlieren Image Velocimetry** Élise Arnaud, Etienne Mémin, Roberto Sosa, Guillermo Artana 

**==> picture [8 x 10] intentionally omitted <==**

## **To cite this version:** 

Élise Arnaud, Etienne Mémin, Roberto Sosa, Guillermo Artana. A Fluid Motion Estimator for Schlieren Image Velocimetry. 9th European Conference on Computer Vision (ECCV ’06), May 2006, Graz, Austria. pp.198–210, ⟨10.1007/11744023_16⟩. ⟨inria-00590206v2⟩ 

**HAL Id: inria-00590206 https://inria.hal.science/inria-00590206v2** 

Submitted on 3 May 2011 

**HAL** is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers. 

L’archive ouverte pluridisciplinaire **HAL** , est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d’enseignement et de recherche français ou étrangers, des laboratoires publics ou privés. 

**==> picture [49 x 19] intentionally omitted <==**

HAL Authorization 

## A Fluid Motion Estimator for Schlieren Image Velocimetry 

Elise Arnaud[1] , Etienne M´emin[2] , Roberto Sosa[3] , and Guillermo Artana[3] 

> 1 Disi, Universit`a di Genova 16146 Genova, Italy arnaud@disi.unige.it 

> 2 IRISA, Universit´e de Rennes 1, 35 042 Rennes Cedex, France memin@irisa.fr 

> 3 Facultad de Ingenier´ıa, Universitad de Buenos Aires Buenos Aires 1412, Argentina {rsosa,gartana}@fi.uba.ar 

Abstract. In this paper, we address the problem of estimating the motion of fluid flows that are visualized through a Schlieren system. Such a system is well known in fluid mechanics as it enables the visualization of unseeded flows. As the resulting images exhibit very low photometric contrasts, classical motion estimation methods based on the brightness consistency assumption (correlation-based approaches, optical flow methods) are completely inefficient. This work aims at proposing a sound energy based estimator dedicated to these particular images. The energy function to be minimized is composed of (a) a novel data term describing the fact that the observed luminance is linked to the gradient of the fluid density and (b) a specific div curl regularization term. The relevance of our estimator is demonstrated on real-world sequences. 

## 1 Introduction 

The ability to understand the complexities of fluid flow behavior has large implications in our daily lives and safety as their control and understanding is of the greatest importance in different applications ranging from aero or hydrodynamic studies (air conditioning, aircraft design, etc.) to environmental sciences (weather forecasting, climate predictions, flood disasters monitoring, etc.). 

Flow visualization has been a powerful tool to depict flow features. Efforts to develop high-quality flow visualization techniques date back over a century. The analysis of the recorded images consisted firstly to a qualitative interpretation of the streak lines, leading overall global insight into the flow properties but lacking quantitative details on important parameters such as velocity fields or turbulence intensities. Point measurement tools such as hot wire probes or Laser Doppler Velocimetry have typically provided these details. As these probes give information only at the point where they are placed, simultaneous evaluations at different points require to dispose a very large number of probes and the evaluation of unsteady field (most of the flows are unsteady) is almost unachievable. 

In an effort to avoid the limitations of these probes, the Particle Image Velocimetry (piv), a non-intrusive diagnostic technique, has been developed in the last two decades. piv enables obtaining velocity fields by seeding the flow with particles (e.g. dye, smoke, particles) and observing the motion of these tracers. An underlying assumption of piv technique is that the motion of these particles follows the motion of the neighboring fluid. This condition is not always satisfied and requires to seed the flow with small sized tracers leading to an increase of the measurement difficulties. Moreover, some phenomena such as natural convection may be influenced by the large amount of seeding particles and the seeding may in return alter results. The setting up of the experiment, adjustment of the seeding concentration and other experimental procedures are in general tedious tasks in many large scale facilities. As a consequence this technique is mainly adapted for test in small closed loops wind tunnels. 

Given the various complexities associated to the use of piv, it is important to examine techniques that can be used to generate quantitative measurements of unseeded flows. The techniques that provide useful visualization images and, at the same time, yields high-quality quantitative data about the flow are of particular interest. In general, Shadowgraph, Schlieren and Interferometry fall into this category. These three techniques do not require flow seeding since they are based on index-of-refraction effects. One of the attractive capabilities of the Schlieren technique is that it can be implemented to undertake full scale measurements and outdoor experiments [1, 2]. 

The objective of this work is to analyze the ability of a dense motion estimator to extract velocity fields from Schlieren images of fluid flows. To date no satisfying technique exists to perform accurately such velocity measurements. The dense motion estimator we propose here relies on a data model specifically designed for such images. The devised data model has been elaborated on physical grounds. In addition to this constraint, we have also considered a div-curl smoothing function allowing the preservation of curl blobs. 

## 2 Description of the Schlieren technique 

The Schlieren technique [3, 4] is an optical method used for fluid flow visualization. Contrary to standard visualization approaches, where a tracer (e.g. solid particle) is followed along the fluid motion or laser-Doppler systems, in which the frequency shift of scattered illumination from such a marker is measured, the Schlieren technique does not require any intrusion in the fluid and prevents any modifications of the considered flow. Such a technique is used to study density fields in transparent media, usually gases or liquids. A typical Schlieren system is described in figure 1. It is based on the fact that a light beam traveling initially in the z direction passing through a medium whose index of refraction varies in x and y direction undergoes a small deviation. For sake of simplicity, the figure 1 presents this phenomenon only in the yz plane. In that case, the light beam has been deviated by an angle α. The Schlieren system is basically a device to observe the angle α as a function of position in the xy plane (respectively the 

**==> picture [323 x 98] intentionally omitted <==**

**----- Start of picture text -----**<br>
Deflected ray<br>α<br>Source<br>y<br>Knife edge<br>z First lens Test section Second lens Screen<br>**----- End of picture text -----**<br>


Fig. 1. Typical Schlieren system using lenses - figure from [3] 

angle in the xz plane). As the light beam deviation depends on the flow density variations, it can be demonstrated that the light pattern obtained with a Schlieren system is determined by the first derivative of the index of refraction such as [3]: 

**==> picture [268 x 25] intentionally omitted <==**

where I(s) is the luminance value of pixel s = (x, y) and ρ(x, y, z) denotes the density of the observed fluid at the physical point of 3d coordinates (x, y, z). The constant K depends on the focal f of the second lens, on the Gladstone-Dale constant C and on ak, the size of the beam cut off by the knife-edge: 

**==> picture [198 x 23] intentionally omitted <==**

As described by the equation (1), the Schlieren visualization integrates the quantity measured over the length of the light beam. As a consequence, this technique is well suited to the study of almost-2d fields, where no density variation is present in the test section. In that case, the light pattern can be expressed as: 

**==> picture [266 x 24] intentionally omitted <==**

where ∆z is the width of the region where the light beam is deflected (supposed small). 

Since the Schlieren technique is non intrusive and does not require any seeding of particles, this visualization procedure enables studies either for laboratory tests or for full scale models in industrial applications. To illustrate this visualization technique, a sample of images are displayed in figure 2. In particular, figure 2(c) represents a typical image provided by Schlieren systems. Such systems are widely used in experimental fluid mechanics laboratories but to date no satisfying solution exists to analyze image sequences of this nature. Indeed, due to the absence of contrast, no image technique allowing a reliable quantitative evaluation of the visualized fluid flow motion is available. To the best of our knowledge, very few works [5, 6] have been carried out to estimate velocity fields from Schlieren images. All these works rely on correlation methods [4]. 

**==> picture [89 x 86] intentionally omitted <==**

**==> picture [101 x 86] intentionally omitted <==**

**==> picture [45 x 86] intentionally omitted <==**

**==> picture [95 x 86] intentionally omitted <==**

**==> picture [257 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) (b) (c) (d)<br>**----- End of picture text -----**<br>


Fig. 2. Example of images obtained from a Schlieren system: (a) human thermal plume (image from [4]) ; (b) instantaneous image of bullet and blast (image from [4]) ; air flow ; visualized flames with a color Schlieren system (here displayed in black and white). 

These methods suffer from several limitations. Among them, one can cite the fact that the results are sensitive to the size of the correlation window support and the possible lack of spatial coherence of the resulting displacement field. We believe that the use of dense motion estimation using optical flow is an interesting alternative that has not been investigated for the Schlieren imagery. These methods, formalized as the minimization of an energy function, have been already successfully implemented for general fluid flow imagery. We have adapted one of these methods to the Schlieren technique. Nevertheless, before describing the proposed dedicated Schlieren energy function, a brief overview of classical dense motion estimator is given in the next section. 

## 3 Related works on dense motion estimation 

## 3.1 Standard optical flow estimation 

Dense estimation of the apparent motion aims at recovering a 2d displacement field w defined over the continuous plane domain S. The estimation is based on the knowledge of the luminance function at two consecutive instants denoted I(s, t), s ∈ S. 

The most accurate techniques to address this problem are related to the Horn and Schunck (H&S) optical flow estimator [7–11]. Such estimators are formalized as the minimizer of an energy function H composed of a data term H1 and a regularization term H2. The first one describes a consistency assumption of the luminance function along a point trajectory. The standard brightness consistency assumption[d] dt[I][= 0 leads to consider the well-know optical flow constraint (][ofc][):] 

**==> picture [275 x 25] intentionally omitted <==**

where ∇I accounts for the spatial gradient of the luminance function and w(s) = (u(s), v(s))[T] is the velocity at point s. The penalty function φ1 is often chosen as the L2 norm but better results may be obtained using a robust function that 

attenuates the effects of areas that do not respect the brightness assumption [8–10]. 

The regularization term captures an a priori on the displacement field. A standard first-order spatial smoothness is usually considered: 

**==> picture [242 x 23] intentionally omitted <==**

where ∥∇w(s)∥ = ∥∇u(s)∥ + ∥∇v(s)∥ with an abuse of notation. Like φ1, the penalty function φ2 authorizes handling local deviations from the smoothness model. The parameter α balances the relative influence of both terms in the functional. 

Facing large frame-to-frame displacements, the data term H1 is not anymore relevant due to its differential nature. To tackle this problem, the brightness consistency assumption has to be expressed in an integrated way, according to the displacement d(s) from time t to t + ∆t instead of the velocity w(s). As we have: 

**==> picture [313 x 23] intentionally omitted <==**

by relaxing the constraint on the limit, the integrated version may be readily written as: 

**==> picture [243 x 11] intentionally omitted <==**

To circumvent the high nonlinearity of this form with respect to the displacement field, the solution consists in proceeding to successive linearizations around an increment field dw. This is usually performed within a multiresolution scheme. A first-order linearization of the first term of (7) yields to the following new energy function (where the time increment ∆t has been set to 1 for simplicity): 

**==> picture [336 x 38] intentionally omitted <==**

For an interested reader, a state of the art of such techniques as well as their comparison can be found in [12, 13]. 

## 3.2 Dense motion analysis in fluid imagery 

As detailed in [14], although estimators based on the energy function (8) have been used for the velocity estimation of fluid structures, the two main assumptions involved in this function are not well suited to that specific case. 

First, the brightness consistency assumption involved in the data term is rarely valid for sequences of fluid flows. As a matter of fact, the observed luminance of a fluid structure may exhibits high spatio-temporal variations caused by temperature and pressure variations or due to its inherent deformable nature. The use of the fluid law of mass conservation (also called the continuity equation) 

as an alternative assumption applied to the evolution of the luminance function has originally been proposed in [15]. Denoting v = (u, v, w) the 3d velocity, the continuity equation reads: 

**==> picture [214 x 22] intentionally omitted <==**

where div(v) =[∂u] ∂x[+] ∂y[∂v][+][∂w] ∂z[denotes][the][divergence][of][the][3d][velocity.][Making] a direct analogy between the density of a fluid particle and its luminance, this law has been integrated in some optical flow schemes [14, 16, 17]. Nevertheless, let us remark that apart from transmittance images [18], the use of the continuity equation remains an approximate constraint when applied to the image brightness. For Schlieren imagery we will show that an exact brightness variation model can be devised. This model will be detailed in the next section. 

Secondly, concerning the regularization term, it can be demonstrated that a first order regularization is not adapted to fluid phenomena as it favors the estimation of velocity fields with low divergence and vorticity. A second order regularization can advantageously be consider as proposed in [19]: 

**==> picture [291 x 24] intentionally omitted <==**

where div(w) =[∂u] ∂x[+] ∂y[∂v][and curl(][w][) =][ −][∂u] ∂y[+] ∂x[∂v][are respectively the divergence] and the vorticity of the 2d field w = (u, v). To circumvent the difficulty of implementing second order smoothness constraint, this regularization term can be simplified - in a computational point of view – in two interleaved first-order div-curl regularizations based on two auxiliary variables ξ1 and ξ2 approximating the divergence and the vorticity of the flow [14]. Introducing the use of a robust penalty function instead of the quadratic function, we have: 

**==> picture [309 x 39] intentionally omitted <==**

where β is a positive regularization parameter. 

## 4 Dense estimator dedicated to Schlieren images 

## 4.1 Data term 

To construct a relevant dense motion estimator for Schlieren image sequences, it is essential to take into account the physical properties of this fluid visualization method. In particular, as previously described, the light pattern at time t is deduced from the density of the fluid (eq. (3)). In case of an almost 2d flow, introducing the time variable, we have: 

**==> picture [275 x 24] intentionally omitted <==**

From that expression, we can deduce: 

**==> picture [298 x 39] intentionally omitted <==**

where v = (u, v, w) is the 3D velocity. This expression can be modified relying on the continuity equation (9) which can be alternatively rewritten after simple manipulations as: 

**==> picture [214 x 22] intentionally omitted <==**

This expression can be advantageously used in the first term A of equation (13). Using expression (12) we have: 

**==> picture [296 x 53] intentionally omitted <==**

In order to simplify the second term B, let us assume that the two first components of the spatial gradient of the density are of the same order, i.e. ∂x[∂][ρ][≈] ∂y[∂][ρ] with no local favored direction. This assumption does not necessary cancel the possibility that a global preferential direction for the pressure gradients may exist. It may be erroneous to associate directly the flow direction, or the favored pressure gradient direction, as the direction of the local fluid density gradients. Many flows of interest behave as incompressible flows and in these kinds of flows it can be admitted that the pressure gradients that drive the fluid flow may produce only negligible changes in the fluid density. The density field results in general from a complex interaction of the different coupled fields: temperature, pressure, buoyancy forces and velocity. As it is difficult to determine a priori a principal direction for the density gradients, it seemed to us reasonable to admit as a first approach that no direction for density gradients is preferential. Using this assumption, expression (12), and the fact that we are interested in this work on the dense motion estimation of mainly bidimensional fluid flows (i.e. inducing ∂∂zρ[= 0),][we][have:] 

**==> picture [263 x 25] intentionally omitted <==**

As a 2D fluid flow is considered, we can also suppose that the apparent 2D velocity is defined by the two first components of the 3D velocity i.e. w = (u, v). From that hypothesis, we can deduce that div(v) = div(w). Then: 

and 

**==> picture [286 x 64] intentionally omitted <==**

The evolution in time of the luminance is then governed by the expression: 

**==> picture [341 x 36] intentionally omitted <==**

Finally, as for most flows studied through a Schlieren system, it can be demonstrated that div(v) = 0, i.e. div(w) = 0, the resulting equation reads: 

**==> picture [233 x 25] intentionally omitted <==**

In a similar manner as the standard optical flow estimation (§ 3.1), the expression (21) is not relevant for the estimation of large frame-to-frame displacements. An integrated version of this constraint has to be considered. Assuming that the velocity is constant between two instants t and t + ∆t, equation (21) is a first order differential equation at constant coefficient (equation of type y[′] (t) − m y(t) = p). Choosing I(s, t) as the initial condition, and setting the time interval ∆t to 1, the integrated for of the data model reads: 

**==> picture [301 x 25] intentionally omitted <==**

To cope with the non linearity of this constraint regarding to the displacement field, a coarse to fine strategy has to be settled. A first-order linearization of the left term in eq. (22) is considered with respect to an increment field dw. Removing the time index for sake of clarity and introducing the following notations I(.) = I(., t) ;[�] I(.) = I(., t + 1), the Schlieren data term can be finally written as: 

**==> picture [327 x 46] intentionally omitted <==**

**==> picture [161 x 19] intentionally omitted <==**

## 4.2 Regularization term 

As for the regularization term, a second-order div-curl regularizer is considered as it enables the preservation of the fluid structures. To deal with the computational difficulties of second order smoothness functional implementation, the approach proposed in [14] is followed. This leads to a regularization term already described by equation (11). Writing this expression in terms of a function of a velocity field increment to be minimized, we have: 

**==> picture [339 x 39] intentionally omitted <==**

This formulation has the very interesting property of allowing the introduction of an a priori information on the divergence and/or vorticity map. In particular, we have seen in the previous paragraph that in the studied experimental images, the divergence of the flow can be considered as null. Such a constraint has to be taken into account in the regularization term also. To that purpose, the term H2 is modified to consider a constrained minimization implemented through a Lagrangian optimization technique. The new regularization reads: 

**==> picture [310 x 39] intentionally omitted <==**

where λ denotes the Lagrangian multiplier associated to the constraint div(w(s)+ dw(s)) = 0. 

## 4.3 Minimization issues 

The incremental estimation of the dense displacement field is conducted through a multiresolution structure that consists in implementing an incremental estimation scheme on a pyramidal hierarchical representation of the image data. At a given resolution level, an incremental displacement field is computed considering that the main component of the displacement is known (supposed null at the coarsest level) and refined by solving: 

**==> picture [237 x 17] intentionally omitted <==**

where H1 and H2 are defined by equations (23,25). The minimization of the functional is considered through a direct discretization of H1 and H2. The different functions involved in the functional are discretized on the image lattice. A particular attention has been paid for the discretization of divergence and curl operator for which an uncentered discretization scheme has been used. 

The overall system is constituted by two main sets of variables that have to be estimated. The first one is the motion field w, and the second set comprises the scalar field ξ. The estimation is conducted alternatively by minimizing H1 + H2 with respect to dw, λ and ξ respectively. For the motion field, considering the curl estimate ξ as being fixed, the robust minimization with respect to dw is solved with an iteratively re-weighted least squares technique. This optimization is embedded in an efficient multi-parametric adaptive multigrid framework [10]. In turn, the motion field dw being fixed, the minimization of the cost function with respect to ξ is in fact equivalent to the minimization of H2 and is again conducted using an iteratively re-weighted least squares technique. 

## 5 Experimental results 

In this section, experimental results are presented to highlight the relevance of our estimator. Two image sequences are studied. They both have been obtained 

in a laboratory of fluid mechanics[4] . The first experiment corresponds to a natural convection of a cylinder test in air at rest and the second one corresponds to a forced convection test of a heated cylinder immersed in a free airstream at room temperature. As it can be noticed on figures 3, 5, the obtained images are very difficult to analyze due to low brightness contrasts. It clearly appears that generic methods based on the brightness consistency assumption (correlation approaches, H&S methods) are hardly suited to these images. 

The images obtained from the first experiment are shown on fig. 3, as well as the sequence of motion fields and vorticity maps obtained by a dense opticalflow estimator [14]. The difficulties of this sequence lie in the lack of luminance variations and in the large frame-to-frame displacements of the fluid structures. As it can be noticed on the vorticity maps, the emergence of a vortex has been well captured by our estimator, as well as the smaller structures. This result proves the validity of the Schlieren dedicated data term. The impact of the new regularization term (that forces the estimation of a flow with null divergence) is demonstrated on fig. 4. This figure presents a comparison between our method and an optical-flow estimator proposed in [14]. As it can be noticed on the presented displacement fields, this latter generates a motion field with areas of high divergence that are not physically plausible. 

The results obtained on the second experiment are shown on fig. 5. These results are displayed in terms of vorticity maps. These pictures show that the moving vertical structures of the fluid flows have been well recovered. We can see in particular the coherent displacement of the lower vortex and the vanishing due to dissipation of the upper vortices. The curl maps also highlight the temporal consistency of the recovered motion fields. 

## 6 Conclusion 

In this paper, we have presented a new method for the estimation of dense fluid motion fields dedicated to images obtained with a Schlieren system. The analysis of the Schlieren images is of great importance in the field of fluid mechanics since this system enables the visualization of unseeded flows. The proposed method is a minimization-based approach where the two terms involved in the cost function have been designed for these images. In particular, the data term has been deduced from the physical relation between the luminance function and the fluid density gradient. The very promising results have demonstrated the interest of using such an approach for the Schlieren image analysis. The following planned step is to validate our approach considering synthetic images produced by a 

- 4 The images have been obtained with a Schlieren system disposed in a Z configuration. It comprised two spherical mirrors of 35 cm in diameter and the light was cut off with two razor blades disposed in vertical and horizontal positions, thus density gradients in both directions could be detected. The parallel light rays traversed the test section of a low speed wind tunnel with windows in the test section of optical quality to avoid improper light deflections. The images were recorded on a monochromatic digital image camera of 12 bits that enabled fast frame acquisition. 

Direct Numerical Simulation code. From this work, several perspectives can be investigated such as the study of 3D flows (using for example the Schlieren tomography [20]), and the design of dedicated algorithms to track the fluid structures. 

## References 

1. Settles, G.S., Hackett, E.B., Miller, J.D., Weinstein, L.M.: Full-scale schlieren flow visualization. In: Flow Visualization VII. (1995) 2–13 

2. Settles, G.S.: The penn state full-scale schlieren system. In: Int. Symp. on Flow Visualization. (2004) 

3. Goldstein, R.J., Kuehn, T.H.: Optical systems for flow measurement: Shadowgraph, schlieren, and interferometric techniques. In: Fluid Mechanics Measurement. Taylor and Francis (1996) 451–508 

4. Settles, G.S.: Schlieren and shadowgraph techniques: visualizing phenomena in transparent media. Springer-Verlag (2001) 

5. Fu, S., Wu, Y., Kothari, R., Xing, H.: Flow visualization using thye negativepositive grid schlieren and its image analysis. In: Int. Symp. on Flow Visualization. (2000) 

6. Kegerise, M.A., Settles, G.S.: Schlieren image-correlation velocimetry and its application to free-convection flows. In: Int. Symp. on Flow Visualization. (2000) 

7. Horn, B., Schunck, B.: Determining optical flow. Artificial Intelligence 17 (1981) 185–203 

8. Black, M., Anandan, P.: The robust estimation of multiple motions: Parametric and piecewise-smooth flow fields. CVIU 63 (1996) 75–104 

9. Brox, T., Bruhn, A., Papenberg, N., Weickert, J.: High accuracy optical flow estimation based on a theory for warping. In: ECCV. (2004) 25–36 

10. M´emin, E., P´erez, P.: Hierarchical estimation and segmentation of dense motion fields. IJCV 46 (2002) 129–155 

11. Ruhnau, P., Kohlberger, T., Nobach, H., Schn¨orr, C.: Variational optical flow estimation for particle image velocimetry. In B. Ruck, A.L., Dopheide, eds.: Proc. Lasermethoden in der Str¨omungsmesstechnik. Karlsruhe (2004) 

12. Barron, J., Fleet, D., Beauchemin, S.: Performance of optical flow techniques. IJCV 12 (1994) 43–77 

13. Beauchemin, S., Barron, J.: The computation of optical flow. ACM Computing Survey 27 (1995) 433–467 

14. Corpetti, T., M´emin, E., P´erez, P.: Dense estimation of fluid flows. PAMI 24 (2002) 365–380 

15. Schunk, B.: The motion constraint equation for optical flow. In: ICPR. (1984) 20–22 

16. B´er´eziat, D., Herlin, H., Younes, L.: A generalized optical flow constraint and its physical interpretation. In: CVPR. Volume 2. (2000) 487–492 

17. Kohlberger, T., M´emin, E., Schn¨orr, C.: Variational dense motion estimation using the Helmholtz decomposition. In: Scale-Space. (2003) 

18. Fitzpatrick, J.: The existence of geometrical density-image transformations corresponding to object motions. CVGIP 44 (1988) 155–174 

19. Suter, D.: Motion estimation and vector splines. In: CVPR. (1994) 939–942 

20. Agrawal, A., Butuk, N., Gollahalli, S., Griffin, D.: Three-dimensional rainbow schlieren tomography of a temperature field en gas flows. Applied Optics (1998) 

**==> picture [265 x 184] intentionally omitted <==**

**----- Start of picture text -----**<br>
image 1 image 2 image 3 image 4<br>(a)<br>(b)<br>**----- End of picture text -----**<br>


(c) 

**==> picture [61 x 86] intentionally omitted <==**

**==> picture [60 x 86] intentionally omitted <==**

**==> picture [61 x 86] intentionally omitted <==**

**==> picture [61 x 86] intentionally omitted <==**

**==> picture [265 x 184] intentionally omitted <==**

**----- Start of picture text -----**<br>
image 5 image 6 image 7 image 8<br>(a)<br>(b)<br>**----- End of picture text -----**<br>


**==> picture [16 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
(c)<br>**----- End of picture text -----**<br>


**==> picture [61 x 86] intentionally omitted <==**

**==> picture [60 x 86] intentionally omitted <==**

**==> picture [61 x 86] intentionally omitted <==**

**==> picture [61 x 86] intentionally omitted <==**

Fig. 3. natural convection. sequence of (a) images, (b) estimated vorticity maps and (c) estimated displacement fields 

**==> picture [15 x 108] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a)<br>(b)<br>**----- End of picture text -----**<br>


**==> picture [67 x 98] intentionally omitted <==**

**==> picture [67 x 97] intentionally omitted <==**

**==> picture [67 x 98] intentionally omitted <==**

**==> picture [67 x 97] intentionally omitted <==**

**==> picture [66 x 98] intentionally omitted <==**

**==> picture [66 x 97] intentionally omitted <==**

Fig. 4. natural convection. comparison between the estimated displacement fields obtained on images 2,3,4 with (a) our estimator and (b) the fluid dedicated estimator of Corpetti et al. [14]. 

**==> picture [134 x 49] intentionally omitted <==**

**==> picture [134 x 49] intentionally omitted <==**

**==> picture [134 x 50] intentionally omitted <==**

**==> picture [134 x 49] intentionally omitted <==**

**==> picture [134 x 50] intentionally omitted <==**

**==> picture [134 x 49] intentionally omitted <==**

**==> picture [134 x 49] intentionally omitted <==**

**==> picture [134 x 50] intentionally omitted <==**

**==> picture [134 x 49] intentionally omitted <==**

**==> picture [134 x 50] intentionally omitted <==**

Fig. 5. forced convection. images 1, 5, 10, 15, 20 and associated estimated vorticity maps 

