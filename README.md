## [Detection, Segmentation, and 3D Pose Estimation of Surgical Tools Using Deep Convolutional Neural Networks and Algebraic Geometry](https://www.sciencedirect.com/science/article/abs/pii/S1361841521000402)

This repository contains the source code, results, and annotation details of the proposed dataset for the concurrent detection, segmentation, and 3D pose estimation of surgical tools using deep convolutional neural networks and algebraic geometry. However, the directory tree of this repository is manifested as follows:

<img src="https://user-images.githubusercontent.com/32570071/106894583-5dc58080-6719-11eb-8209-8ad723994d10.png" width="750" height="500" />

Surgical tool detection, segmentation, and 3D pose estimation are crucial components in Computer-Assisted Laparoscopy (CAL). The existing frameworks have two main limitations. First, they do not integrate all three components. Integration is critical; for instance, one should not attempt computing pose if detection is negative. Second, they have highly specific requirements, such as the availability of a CAD model. We propose an integrated and generic framework whose sole requirement for the 3D pose is that the tool shaft is cylindrical. Our framework makes the most of deep learning and geometric 3D vision by combining a proposed Convolutional Neural Network (CNN) with algebraic geometry.
We show two applications of our framework in CAL: tool-aware rendering in Augmented Reality (AR) and tool-based 3D measurement.

This project proposed ART-Net to detect, segment, and extract three geometric primitives simultaneously from the laparoscopic images. 
These primitives are the tool edge-lines, mid-line, and tip. They allow the tool's 3D pose to be estimated by a fast algebraic procedure. The framework only proceeds if a tool is detected. The accuracy of segmentation and geometric primitive extraction is boosted by a new Full resolution feature map Generator (FrG). We extensively evaluate the proposed framework with the  EndoVis and new proposed datasets. 
We compare the segmentation results against several variants of the Fully Convolutional Network (FCN) and U-Net. Several ablation studies are provided for detection, segmentation, and geometric primitive extraction.
The proposed datasets are surgery videos of different patients.

However, more details can be found in the article ([here](https://www.sciencedirect.com/science/article/abs/pii/S1361841521000402)) in Medical Image Analysis (Elsevier).  

## Network Training
Two stages of training and testing were used (section 4.2 of [article](https://www.sciencedirect.com/science/article/abs/pii/S1361841521000402) presents details). In the first stage, referred to as stage-1, we trained and tested only the segmentation sub-network of ART-Net on the EndoVis (robotic) dataset, whereas in the second stage, referred to as stage-2, we trained and tested the whole ART-Net on the combined EndoVis (non-robotic) and our annotated data.
The following three sets of datasets are utilized in this [article](https://www.sciencedirect.com/science/article/abs/pii/S1361841521000402). 

* EndoVis (robotic) dataset (can be found [here](https://endovissub-instrument.grand-challenge.org/Data/))
* EndoVis (non-robotic) dataset (can be found [here](https://endovissub-instrument.grand-challenge.org/Data/))
* Our proposed dataset (can be found [here](https://forms.gle/BhavnSx55fa8zocj9))

## Data Annotation 
We annotated the tool presence, the segmentation masks, and the geometric primitives for the laparoscopy images, as pictured in the following figure. 
![Annotated Geometric Features](https://user-images.githubusercontent.com/32570071/58099671-6b04a980-7bdc-11e9-83b4-c680de96beba.png)

For the annotation, we have used ImageJ software and basic image processing methods. Firstly, the tool's ROIs are selected from ImageJ software, and then the following block diagram has been used to get the surgical tools' binary masks.
<img src="https://user-images.githubusercontent.com/32570071/58098941-dc435d00-7bda-11e9-8845-1f16a9945198.JPG" width="700" height="290" />

Five points are selected and extracted as CSV together with the ROI selection from the ImageJ software, and then basic image processing methods are used to generate the edge-line, mid-line, and tip-point. The selected five points are displayed in the following figure. Those five points are utilized to generate three geometric primitives applying a simple python script. The primitives hold an intensity of bell-shaped Gaussian distribution.

<img src="https://user-images.githubusercontent.com/32570071/58100378-ce430b80-7bdd-11e9-93bd-b573ca924951.jpg" width="700" height="290" />

Our annotated dataset is made publicly available for research or academic purposes only. However, to access our annotated dataset, the audience is requested to fill the following google form. 

[Registration for Accessing our ART-Net Dataset](https://forms.gle/BhavnSx55fa8zocj9)

Then, the annotated dataset can be found in the following link. 

[ART-Net dataset](https://drive.google.com/file/d/1O9Brs9mWw9KI2jgy8Ho2yljA5uH1_UIE/view?usp=sharing)



If you access our dataset, do not forget to cite the article in the [link](https://www.sciencedirect.com/science/article/abs/pii/S1361841521000402).

#### Written by- <br>
Md. Kamrul Hasan <br>
Former research intern at [EnCoV](http://igt.ip.uca.fr/encov/) research team, France <br>
Former Erasmus Scholar on Medical Imaging and Applications ([MAIA](http://maiamaster.udg.edu/)) <br> 
For more details write me at kamruleeekuet@gmail.com <br> 
Google Scholar https://scholar.google.com/citations?user=36WXELIAAAAJ&hl=en
