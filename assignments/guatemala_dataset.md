# Segmentation of the Guatemala dataset

## Research goal and expected output
* We are collaborating with team of archeologists to process a huge dataset with DL methods
* The task is very complex, You will be assigned a small subset of the problems to test, implement and evaluate.

* Selecting the most suitable tile for segmentation.The dataset contains multiple tiles with size (approx 17100 x 9800 pixels), that represents different transforms of the lidar source data. We can vary multiple variables to generate data for our specific purposes e.g. size of the input image, threshold for detection, tile selection etc.

* __Expected output__: __Multiple models, that perform well on the selected dataset for detection and segmentation.__

* Front-end - We will probably use this to offload generation of the training datasets to the server

## Milestones
* __Week 4__  - Best possible dataset for detection (we have infinite possibilities - I will explain this in person).

* __Week 5__ - Picking the appropriate method for segmentation - R-CNN, U-Net, Fast R-CNN, Mask R-CNN.

* __Week 8__ - Comparison of performance of this methods on the dataset for binary detection, segmentation. + First draft of the article.

* __Week 11__ - Experiments with architecture tweeks with preprocesing and postprocesing.

* __Week 13__ - Attempts at non-binary segmentation, detection.

## Literature
Read the short intro at the beginning here about the dataset:
* https://science.sciencemag.org/content/361/6409/eaau0137

About the methods used:
* https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e

* https://blog.athelas.com/a-brief-history-of-cnns-in-image-segmentation-from-r-cnn-to-mask-r-cnn-34ea83205de4

* https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/

## Contact information

* miroslav.jascur@tuke.sk
* Consultation - Tuesdays - 14:00-16:00
