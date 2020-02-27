# Neural Code Completion with Attention

Intelligent code completion has become an essential research task to accelerate modern software development. In this project, you will develop a deep learning-based code completion for **one** of the given language (Python, Java, Javascript). 

## Research goal and expected output

The goal of the project is to develop a neural network for code completion. Your neural network has to be based on a Transformer architecture. 
You have to use **one** of the given datasets but you are allowed to use a supplementary dataset.
The testing set will be provided by the consultant during the evaluation of the models. You can use architectures from published papers, but you might have to adjust them to the task at hand. 
In the first phase of the project, team members will work on individual solutions. After 8 weeks, the students' implementations will be tested, and the best model will then be improved upon by all team members.
The trained model's functionality should be presented through a graphical user interface (local or web application) that should give the user the possibility to check the model's output with sample inputs and also to test it.
Finally, the team should provide documentation for the project. The documentation should contain the following:

1. description of the dataset and the chosen programming language
2. description of the neural network (architecture, layers, loss function, activation functions, etc.)
3. description of the training process (tokenization, number of epochs, batch size, partial results from testing with different hyperparameters, a graph of the change of different metrics with the final setup)
4. sample results
5. academic paper with a literature review, methodology, evaluation, results with comparison to the state of the art and conclusion to be published in the university's journal or a corresponding platform

## Milestones

1. Theoretical overview of NLP with deep learning (week 3) 
2. Architecture Proposal (week 4)
3. First working Implementation (week 5)
4. Overview paper in Latex format (week 6)
5. Proof of Concept and Improvement Proposal (week 8)


## Literature

* On the Naturalness of Software. A. Hindle, E. T. Barr, Z. Su, M. Gabel, P. Devanbu. ICSE 2012. https://ieeexplore.ieee.org/abstract/document/6227135
* Pythia: AI-assisted Code Completion System. A. Svyatkovskiy, Y. Zhao, S. Fu, Neel Sundaresan. KDD 2019. https://dl.acm.org/doi/abs/10.1145/3292500.3330699\
* Deep Learning to Find Bugs. M. Pradel, K. Sen. 2017. http://mp.binaervarianz.de/DeepBugs_TR_Nov2017.pdf
* SmartPaste: Learning to Adapt Source Code. M. Allamanis, M. Brockscmidt. 2017. https://arxiv.org/abs/1705.07867
* Intelligent code reviews using deep learning. A. Gupta, N. Sundaresan. KDD 2018 https://pdfs.semanticscholar.org/9395/74bb3b9484cd888bb622e286cbf8bf96ba61.pdf
* A deep language model for software code. H. K. Dam, T. Tran, T. Pham. ArXiV 1608.02715 2016. https://arxiv.org/abs/1608.02715
* Structured Generative Models of Natural Source Code. C.J. Maddison, D. Tarlow. ICML 2014. http://proceedings.mlr.press/v32/maddison14.pdf
* Maybe Deep Neural Networks are the Best Choice for Modeling Source Code. R.M. Karampatsis, C. Sutton. 2019. https://arxiv.org/abs/1903.05734

## Additional Resource 

You can find an online resource: course and paper here https://github.com/src-d/awesome-machine-learning-on-source-code.
For transformer architecture, please take a look at this repository https://github.com/huggingface/transformers and https://huggingface.co/transformers/.


## Datasets

* Javascript https://www.sri.inf.ethz.ch/js150
* Python https://www.sri.inf.ethz.ch/py150
* Java http://groups.inf.ed.ac.uk/cup/javaGithub/

## Contact information

* Consultant: Andrij David, MSc. andrijdavid@tuke.sk
* Office hours - agreement over e-mail
