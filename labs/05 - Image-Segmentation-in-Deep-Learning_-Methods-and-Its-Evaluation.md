# Image Segmentation in Deep Learning: Methods and Its Evaluation
## What is Image Segmentation?
Image segmentation is a critical process in computer vision. It involves dividing a visual input into segments to simplify image analysis. Segments represent objects or parts of objects, and comprise sets of pixels, or “super-pixels”. Image segmentation sorts pixels into larger components, eliminating the need to consider individual pixels as units of observation. There are three levels of image analysis:

 - **Classification** – categorizing the entire image into a class such as “people”, “animals”, “outdoors”
 - **Object detection** – detecting objects within an image and drawing a rectangle around them, for example, a person or a sheep.
 - **Segmentation** – identifying parts of the image and understanding what object they belong to. Segmentation lays the basis for performing object detection and classification.

![alt text](https://missinglink.ai/wp-content/uploads/2019/03/what-is-image-segmentation-e1553795451244.png "Classification vs. Detection vs. Segmentation")

## Semantic Segmentation vs. Instance Segmentation
Within the segmentation process itself, there are two levels of granularity:

 - **Semantic segmentation** — classifies all the pixels of an image into meaningful classes of objects. These classes are “semantically interpretable” and correspond to real-world categories. For instance, you could isolate all the pixels associated with a cat and color them green. This is also known as dense prediction because it predicts the meaning of each pixel.
![alt text](https://missinglink.ai/wp-content/uploads/2019/03/Semantic-segmentation-original-1.png "Segmentation output")
 - **Instance segmentation** — identifies each instance of each object in an image. It differs from semantic segmentation in that it doesn’t categorize every pixel. If there are three cars in an image, semantic segmentation classifies all the cars as one instance, while instance segmentation identifies each individual car.
 - 
 ## Old-School Image Segmentation Methods

There are additional image segmentation techniques that were commonly used in the past but are less efficient than their deep learning counterparts because they use rigid algorithms and require human intervention and expertise. These include:

 - **Thresholding**—divides an image into a foreground and background. A specified threshold value separates pixels into one of two levels to isolate objects. Thresholding converts grayscale images into binary images or distinguishes the lighter and darker pixels of a color image.
 - **K-means clustering**—an algorithm identifies groups in the data, with the variable K representing the number of groups. The algorithm assigns each data point (or pixel) to one of the groups based on feature similarity. Rather than analyzing predefined groups, clustering works iteratively to organically form groups.
 - **Histogram**-based image segmentation—uses a histogram to group pixels based on “gray levels”. Simple images consist of an object and a background. The background is usually one gray level and is the larger entity. Thus, a large peak represents the background gray level in the histogram. A smaller peak represents the object, which is another gray level.
 - **Edge detection**—identifies sharp changes or discontinuities in brightness. Edge detection usually involves arranging points of discontinuity into curved line segments, or edges. For example, the border between a block of red and a block of blue.

## Basic principle of the segmantation
To understand the basic principle of the segmentation it is very important to understand the different operations that are typically used in a Convolutional Network. 

### Convolutional operation
There are two inputs to a convolutional operation
1. A 3D volume (input image) of size (nin x nin x channels)
2. A set of ‘k’ filters (also called as kernels or feature extractors) each one of size (f x f x channels), where f is typically 3 or 5.

The output of a convolutional operation is also a 3D volume (also called as output image or feature map) of size (nout x nout x k).

The relationship between nin and nout is as follows:
![alt text](https://miro.medium.com/max/330/1*V5ZIZg7cGHLASKbnRbKBJQ.png "nin nout")

Convolution operation can be visualized as follows:
![alt text](https://miro.medium.com/max/800/1*QgiVWSD6GscHh9nt55EfXg.gif "Convolutional operations")
In the above GIF, we have an input volume of size 7x7x3. Two filters each of size 3x3x3. Padding =0 and Strides = 2. Hence the output volume is 3x3x2.

One important term used frequently is called as the **Receptive filed**. This is nothing but the region in the input volume that a particular feature extractor (filter) is looking at. In the above GIF, the 3x3 blue region in the input volume that the filter covers at any given instance is the receptive field. This is also sometimes called as the **context**.

To put in very simple terms, **receptive field (context) is the area of the input image that the filter covers at any given point of time.**

### Max pooling operation
In simple words, the function of pooling is to reduce the size of the feature map so that we have fewer parameters in the network.

For example:
![alt text](https://miro.medium.com/max/516/1*lar5CEt_H-Xuw_N7HYuJ0w.png "Maxpooling")
Basically from every 2x2 block of the input feature map, we select the maximum pixel value and thus obtain a pooled feature map. Note that the size of the filter and strides are two important hyper-parameters in the max pooling operation.

The idea is to retain only the important features (max valued pixels) from each region and throw away the information which is not important. By important, it means that information which best describes the context of the image.

A very important point to note here is that both convolution operation and specially the pooling operation reduce the size of the image. This is called as **down sampling**. In the above example, the size of the image before pooling is 4x4 and after pooling is 2x2. In fact down sampling basically means converting a high resolution image to a low resolution image.

Thus before pooling, the information which was present in a 4x4 image, after pooling, (almost) the same information is now present in a 2x2 image.

Now when we apply the convolution operation again, the filters in the next layer will be able to see larger context, i.e. as we go deeper into the network, the size of the image reduces however the receptive field increases.

For example, below is the LeNet 5 architecture:
![alt text](https://miro.medium.com/max/909/1*xj9w5xN0Xrf3w73iVDQrxg.png "Maxpooling")
Notice that in a typical convolutional network, the height and width of the image gradually reduces (down sampling, because of pooling) which helps the filters in the deeper layers to focus on a larger receptive field (context). However the number of channels/depth (number of filters used) gradually increase which helps to extract more complex features from the image.

Intuitively we can make the following conclusion of the pooling operation. By down sampling, the model better understands **“WHAT”** is present in the image, but it loses the information of **“WHERE”** it is present.

### Need for up sampling
As stated previously, the output of semantic segmentation is not just a class label or some bounding box parameters. In-fact the output is a complete high resolution image in which all the pixels are classified.

Thus if we use a regular convolutional network with pooling layers and dense layers, we will lose the “WHERE” information and only retain the “WHAT” information which is not what we want. In case of segmentation we need both “WHAT” as well as “WHERE” information.

Hence there is a need to up sample the image, i.e. convert a low resolution image to a high resolution image to recover the “WHERE” information.

In the literature, there are many techniques to up sample an image. Some of them are bi-linear interpolation, cubic interpolation, nearest neighbor interpolation, unpooling, transposed convolution, etc. However in most state of the art networks, transposed convolution is the preferred choice for up sampling an image.

### Transposed Convolution
Transposed convolution (sometimes also called as deconvolution or fractionally strided convolution) is a technique to perform up sampling of an image with learnable parameters.

To understand process of Transposed Convolutional , you can go through [this blog](https://medium.com/activating-robotic-minds/up-sampling-with-transposed-convolution-9ae4f2df52d0).

However, on a high level, transposed convolution is exactly the opposite process of a normal convolution i.e., the input volume is a low resolution image and the output volume is a high resolution image.

### Summary of the main concept
After reading this section, you should be comfortable with following concepts:
* Receptive field or context
* Convolution and pooling operations down sample the image, i.e. convert a high resolution image to a low resolution image
* Max Pooling operation helps to understand “WHAT” is there in the image by increasing the receptive field. However it tends to lose the information of “WHERE” the objects are.
* In semantic segmentation it is not just important to know “WHAT” is present in the image but it is equally important to know “WHERE” it is present. Hence we need a way to up sample the image from low resolution to high resolution which will help us restore the “WHERE” information.
* Transposed Convolution is the most preferred choice to perform up sampling, which basically learns parameters through back propagation to convert a low resolution image to a high resolution image.

## Segmentation CNN architecture
To understand more deeply the segmentation process of the CNN, we are going to explain it on the *UNET* architecture.

The UNET was developed by Olaf Ronneberger et al. for Bio Medical Image Segmentation. The architecture contains two paths. First path is the contraction path (also called as the encoder) which is used to capture the context in the image. The encoder is just a traditional stack of convolutional and max pooling layers. 
The second path is the symmetric expanding path (also called as the decoder) which is used to enable precise localization using transposed convolutions.

Now, we will describe this architecture with the input image of size 128x128x3.
Below is the detailed explanation of the architecture:
![alt text](https://miro.medium.com/max/2082/1*yzbjioOqZDYbO6yHMVpXVQ.jpeg "u-net")

##### Notes:
* 2@Conv layers means that two consecutive Convolution Layers are applied
* c1, c2, …. c9 are the output tensors of Convolutional Layers
* p1, p2, p3 and p4 are the output tensors of Max Pooling Layers
* u6, u7, u8 and u9 are the output tensors of up-sampling (transposed convolutional) layers

##### Flow of the data in the architecture
The left hand side is the contraction path (Encoder) where we apply regular convolutions and max pooling layers.
In the Encoder, the size of the image gradually reduces while the depth gradually increases, which basically means the network learns the **“WHAT”** information in the image, however it has lost the **“WHERE”** information
* it start from 128x128x3
* applying two convolutional layers with 16 filters of the size 3x3 and same padding we get *c1* of the size *128x128x16*
* applying max pooling with filter size of 2x2 and strides 2 we get *p1* with the size *64x64x16*
* applying the same procedure 4 more times we get *c5* of the size *8x8x256*
The right hand side is the expansion path (Decoder) where we apply transposed convolutions along with regular convolutions
In the decoder, the size of the image gradually increases and the depth gradually decreases
* it start from *c5* 
* applying transposed convolutional layer we get *u6* we get *16x16x128*
* to get better precise locations, at every step of the decoder we use skip connections by concatenating the output of the transposed convolution layers with the feature maps from the Encoder at the same level, thus we get *u6=u6+c4*, so we get tensor of the size *16x16x256*
* After every concatenation we again apply two consecutive regular convolutions with 128 filter of the size 3x3 with the same padding so that the model can learn to assemble a more precise output. Therefore we get *c6* of the size *16x16x128*
* appplying the same procedure 4 times we get final output of the size *128x128x1*, thus, final mask providing segmentation of the objects

This is what gives the architecture a symmetric U-shape, hence the name UNET

## How to evaluate segmentation? 
How do we know our model is performing well? In other words, what are the most common metrics for semantic segmentation?

### 1. Pixel accuracy
**Pixel accuracy** is the easiest to understand conceptually. *It is the percent of pixels in your image that are classified correctly.* **While it is easy to understand, it is in no way the best metric.**
 Let’s say we ran the following image (Left) through our segmentation model. The image on the right is the ground truth, or annotation (what the model is supposed to segment). In this case, our model is trying to segment ships in a satellite image.
![alt text](https://miro.medium.com/max/2800/0*AmruarcqPbBG4jUx.png "ships")

We have computed that our segmentation accuracy is **95%**. But let's see how our segmentation looks like.
![alt text](https://miro.medium.com/max/700/1*yO-dem7wHFv0zNN1LM0saA.png "black")
It detect nothing, however, the calculation is right because it predicted **95%** of the background correctly while the other 5% did not. This issue is called **class imbalance**. When our classes are extremely imbalanced, it means that a class or some classes dominate the image, while some other classes make up only a small portion of the image.

### 2. Intersection-Over-Union (IoU, Jaccard Index)
The Intersection-Over-Union (IoU), also known as the Jaccard Index, is one of the most commonly used metrics in semantic segmentation.
**IoU is the area of overlap between the predicted segmentation and the ground truth divided by the area of union between the predicted segmentation and the ground truth**
![alt text](https://miro.medium.com/max/600/0*kraYHnYpoJOhaMzq.png "ships")
Now let’s try to understand why this metric is better than pixel accuracy by using the same scenario as section 1. For the sake of simplicity, let’s assume all the ships (colored boxes) are part of the same class.

Let’s calculate the ship IoU first. We assume the total area of the image is 100 (100 pixels). First, let’s think about the ships’ overlap. We can pretend that we move the predicted segmentation  directly above the ground truth, and see if there are any ship pixels that overlap. Since there are no pixels that are classified as ships by the model, there are 0 overlapping ship pixels.

Union consists of all of the pixels classified as ships from both images, minus the overlap/intersection. In this case, there are 5 pixels (this is an arbitrary number choice) that are classified as ships total. Subtract the overlap/intersection which is 0 to get 5 as the area of union. After doing the calculations, we learn that the IoU is merely 47.5%! See the calculation below.

Ships: Area of Overlap = 0, Area of Union = (5+0)-0 =5
Area of Overlap/Area of Union = 0%
Now for the black background, we do the same thing.
Background: Area of Overlap = 95, Area of Union = (95+100)–95 = 100
Area of Overlap/Area of Union =95%
Mean IoU = (Ships + Background)/2 = (0%+95%)/2 = 47.5%
That’s a lot lower than the 95% pixel accuracy we calculated. It is obvious that 47.5 is a much better indication of the success of our segmentation, or more appropriately, the lack thereof.

### 3. Dice Coefficient (F1 Score)
The alternative to IoU is Dice Coefficient (F1 Score). **Dice Coefficient is 2 * the Area of Overlap divided by the total number of pixels in both images.**
![alt text](https://miro.medium.com/max/858/1*yUd5ckecHjWZf6hGrdlwzA.png "ships")

## Exercise
1. Evaluate following segmentation [output](https://drive.google.com/file/d/1YID8V61feu_T3daXrFTkFudYzDUFWccr/view?usp=sharing) with [ground truth label](https://drive.google.com/file/d/1uPPCSXYMd1ATj66TrEW0jVmSFOeK6pN6/view?usp=sharing) using three mentioned metrics.
2. Fill out following [test](https://forms.gle/7sZBZRnZG8cp55n96) from the course.
3. Who will not fill out the test, it will be considered as an absence. 



## References
1. https://missinglink.ai/guides/computer-vision/image-segmentation-deep-learning-methods-applications/
2. https://towardsdatascience.com/semantic-segmentation-with-deep-learning-a-guide-and-code-e52fc8958823
3. https://towardsdatascience.com/understanding-semantic-segmentation-with-unet-6be4f42d4b47
4. https://towardsdatascience.com/metrics-to-evaluate-your-semantic-segmentation-model-6bcb99639aa2













