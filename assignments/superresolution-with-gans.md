# Superresolution with GANs
Generative adversarial networks (GANs) have found applications in various branches of deep learning. In this project, you will look at the possibility of using GANs to upscale images from low resolution to high resolution. By solving the project, you will acquire some experience with GANs; loss functions specific to deep learning; image processing using deep learning; creating, processing and splitting datasets; and with the methodology of training deep networks.

## Research goal and expected output
The goal of the project is to test GANs for superresolution. You will use an upscaling factor of 4x, the resolution of the images is up to you (*90x90* to *360x360* is recommended).

Part of the project will be to create a dataset of images of a certain category (the category will be specified at the first meeting; ideas: cars, dogs, birds, faces), preprocess the dataset and split it into training and validation set. The testing set will be provided by the consultant during evaluation of the models.

Another part of the project is to design and implement a GAN architecture. You can use architectures from published papers, but you might have to adjust them to the task at hand. In the first phase of the project, team members will work on individual solutions. After 8 weeks, the students' implementations will be tested, and the best model will then be improved upon by all team members.

The trained model's functionality should be presented through a graphical user interface (local or web application) that should give the user the possibility to check the model's output with sample inputs and also to test it on their own input images.

Finally, the team should provide a documentation for the project. The documentation should contain the following:

1. description of the combined dataset (image sources, image sizes, resolution, etc.)
2. description of the GAN model (architecture, layers, loss function, activation functions, etc.)
3. description of the training process (number of epochs, batch size, partial results from testing with different hyperparameters, graph of the change of the loss function with the final setup)
4. sample inputs and outputs
5. academic paper with a literature review, methodology, evaluation, results and conclusion to be published in the university's journal or a corresponding platform

## Milestones
1. theoretical overview of GANs (week 3) - consultation meeting to answer any questions regarding GANs
2. literature review; first working implementation (week 4) - find similar applications and solutions, architectures, etc. (put together a list of 20 academic papers)
3. dataset and net design (week 5) - hand in a documentation of the dataset used and the proposed GAN architecture
4. overview paper (week 6) - hand in a paper in Latex or Word that provides an overview of state-of-the-art solutions (team work)
5. proof of concept (week 8) - give a presentation with first results during class
6. first tests of student solutions (week 8) - a comparison of the models trained by team members; work will continue on the best-performing model
7. improvement proposal (week 10) - hand in a detailed plan of the changes needed to be done to the datasets and/or model to improve accuracy and usability
8. final presentation (week 12) - final presentation of the solution during class

## Literature
* Goodfellow, Ian, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, and Yoshua Bengio. "[Generative adversarial nets.](http://papers.nips.cc/paper/5423-generative-adversarial-nets.pdf)" In Advances in neural information processing systems, pp. 2672-2680. 2014.
* Ledig, Christian, Lucas Theis, Ferenc Huszár, Jose Caballero, Andrew Cunningham, Alejandro Acosta, Andrew Aitken et al. "[Photo-realistic single image super-resolution using a generative adversarial network.](http://openaccess.thecvf.com/content_cvpr_2017/papers/Ledig_Photo-Realistic_Single_Image_CVPR_2017_paper.pdf)" In Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 4681-4690. 2017.
* Johnson, Justin, Alexandre Alahi, and Li Fei-Fei. "[Perceptual losses for real-time style transfer and super-resolution.](https://arxiv.org/pdf/1603.08155.pdf%7C)" In European conference on computer vision, pp. 694-711. Springer, Cham, 2016.
* Wang, Xintao, Ke Yu, Shixiang Wu, Jinjin Gu, Yihao Liu, Chao Dong, Yu Qiao, and Chen Change Loy. "[Esrgan: Enhanced super-resolution generative adversarial networks.](http://openaccess.thecvf.com/content_ECCVW_2018/papers/11133/Wang_ESRGAN_Enhanced_Super-Resolution_Generative_Adversarial_Networks_ECCVW_2018_paper.pdf)" In Proceedings of the European Conference on Computer Vision (ECCV), pp. 0-0. 2018.
* Yuan, Yuan, Siyuan Liu, Jiawei Zhang, Yongbing Zhang, Chao Dong, and Liang Lin. "[Unsupervised image super-resolution using cycle-in-cycle generative adversarial networks.](http://openaccess.thecvf.com/content_cvpr_2018_workshops/papers/w13/Yuan_Unsupervised_Image_Super-Resolution_CVPR_2018_paper.pdf)" In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition Workshops, pp. 701-710. 2018.


## Contact information
* Consultant: Ján Magyar, MSc. ([jan.magyar@tuke.sk](mailto:jan.magyar@tuke.sk))
* Office hours - Thursday 10:00 a.m. or after agreement over e-mail
