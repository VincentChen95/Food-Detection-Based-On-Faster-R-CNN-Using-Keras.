# Food-Detection-Based-On-Faster-R-CNN.
## Introduction
<br/> Our project dataset mainly came from ECUSTFD[1], which is a free public food image dataset. This dataset has 19 types of food as shown in the figure. The number of food images is 2978. The number of images in each class.
![merge_from_ofoct 4](https://user-images.githubusercontent.com/36937088/49711360-c412ef00-fbf3-11e8-88df-43a8e1be7945.jpg)
<br/> 'apple': 322, 'banana': 212, 'bread': 66, 'bun': 90 , 'doughnut': 210, 'egg': 104, 'fired_dough_twist': 124, 'grape': 58, 'lemon': 185, 'litchi': 78, 'mango': 250, 'mooncake': 134, 'orange': 281, 'peach': 126, 'pear': 182, 'plum': 176, 'qiwi': 137, 'sachima': 150, 'tomato': 201.
## Data pre-process
<br/> The first step is data pre-process, include transforming "xml" annotation file into "csv" file. Then I split data into training and validation set. The ratio is 7:1.
## Methods
<br/> We employed Keras to implement Faster RCNN. For Faster RCNN, it use Region Proposal Network(RPN) to generate the prediction box. specifically, RPN uses CNN to extract a feature map(51*39*256). Then each point at the feature map is responsible for the screening of 9 boxes with different size in the original image. The goal for screening is to check whether there is an object or not in the box. All these points are called 'anchors'. You can adjust the size of the box. After RPN generate the box, we use ResNet to classify all these boxes.
## Test result
<br/> In this project, we achieve 82% mean accuracy for all 19 kinds of food. According to the confusion matrix, we can konw that the result is balanced.
<br/> <img src="https://user-images.githubusercontent.com/36937088/49712623-38509100-fbfa-11e8-85cd-ba4344897fc4.jpg" width="50%" height="50%">
<br/> The test result show as below.
![merge_from_ofoct 5](https://user-images.githubusercontent.com/36937088/49711856-98ddcf00-fbf6-11e8-874b-f811af850141.jpg)
## Requirement
<br/> h5py
<br/> Keras==2.0.3
<br/> numpy
<br/> opencv-python
<br/> sklearn
## References
<br/> [1] https://github.com/Liang-yc/ECUSTFD-resized-
