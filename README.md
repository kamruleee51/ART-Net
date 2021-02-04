## [Detection, Segmentation, and 3D Pose Estimation of Surgical Tools Using Deep Convolutional Neural Networks and Algebraic Geometry](http://github.com)

This repository contains the source code, results, and annotation details of the proposed dataset for the concurrent detection, segmentation, and 3D pose estimation of surgical tools using deep convolutional neural networks and algebraic geometry. However, the directory tree of this repository is manifested as follows:

<img src="https://user-images.githubusercontent.com/32570071/106894583-5dc58080-6719-11eb-8209-8ad723994d10.png" width="750" height="500" />

Surgical tool detection, segmentation, and 3D pose estimation are crucial components in Computer-Assisted Laparoscopy (CAL). The existing frameworks have two main limitations. First, they do not integrate all three components. Integration is critical; for instance, one should not attempt computing pose if detection is negative. Second, they have highly specific requirements, such as the availability of a CAD model. We propose an integrated and generic framework whose sole requirement for the 3D pose is that the tool shaft is cylindrical. Our framework makes the most of deep learning and geometric 3D vision by combining a proposed Convolutional Neural Network (CNN) with algebraic geometry.
We show two applications of our framework in CAL: tool-aware rendering in Augmented Reality (AR) and tool-based 3D measurement.

This project proposed ART-Net to detect, segment, and extract three geometric primitives simultaneously from the laparoscopic images. 
These primitives are the tool edge-lines, mid-line, and tip. They allow the tool's 3D pose to be estimated by a fast algebraic procedure. The framework only proceeds if a tool is detected. The accuracy of segmentation and geometric primitive extraction is boosted by a new Full resolution feature map Generator (FrG). We extensively evaluate the proposed framework with the  EndoVis and new proposed datasets. 
We compare the segmentation results against several variants of the Fully Convolutional Network (FCN) and U-Net. Several ablation studies are provided for detection, segmentation, and geometric primitive extraction.
The proposed datasets are surgery videos of different patients.

However, more details can be found in the article ([here](http://github.com)) in Medical Image Analysis (Elsevier).  

