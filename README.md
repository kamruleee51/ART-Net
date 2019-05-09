# 3D-Pose-and-Segmentation-for-AR-in-MIS
In this project, we present deep convolution neural network (DCNN) for simultaneouslygetting surgical instrument segmentation and geometric features for 3D pose estimation tosolve the current ambiguities of AR based application in MIS. Additionally, we add detectionsub-network to our SIMO-DCNN to get the tool flag.  Tool flag will provide the constrain ofestimating pose or not.  The proposed network with different responsible sub-networks hasbeen trained in an end-to-end fashion and each sub-network of the SIMO-DCNN has dif-ferent loss functions to get responsible output.  We validate our proposed approach on bothex-vivoandin-vivolaparoscopic images where we are able to reach improved results overexisting state-of-the-art approaches on the same dataset. The geometric features obtainedfrom the proposed SIMO network are used to estimate the 3D pose of surgical instrumentsby geometric solver. <br>

The pictorial presentation of overall pipeline that has been accomplishedis shown in Fig.  1.  Firstly, input images are feed to CBR block which is a bunch of con-volution  andreluactivation  with  sub-sampling  and  is  shared  by  all  others  sub-networksfor detection, segmentation and regression simultaneously.  FCS is the fully connected layerfollowed by thesof tmaxclassifier that provides the information about the tool presence inthe image frame and termed as detection sub-network.  If the detected tool flag isyesfromthe detection sub-network,  the pose of the surgical tool will be estimated and vice-versa.DBRS named as segmentation sub-network and DBR named as regression sub-network arethe bunch deconvolution for semantic tissue or instrument pixels labelling and the regres-sion to get three geometric features for pose estimation respectively.  




#### Written by-
#### Md. Kamrul Hasan 
#### Erasmus Scholar on Medical Imaging and Application (MAIA) [http://maiamaster.udg.edu/]
#### For more details write me at kamruleeekuet@gmail.com

The idea for the single input multiple output (SIMO) DCNN along with transfer learning is shown in the Figure below. 
![simo](https://user-images.githubusercontent.com/32570071/52538979-7cd2e700-2d79-11e9-91ef-620780feb8bb.png)

For the details about this project will be added later. 
