# Evaluation of Deep Neural Networks
When training a machine learning model, one of the main things that you want to avoid would be overfitting. This is when your model fits the training data well, but it isn't able to generalize and make accurate predictions for data it hasn't seen before. To prevent this we are searc

### Training accuracy

![alt text](/labs/resources/training.png "Confusion_matrix") (2)
Current number of samples that were assigned the correct class from the training set.
### Validation accuracy

### Training loss
![alt text](/labs/resources/loss.png "Confusion_matrix") (2)

### Validation loss

## Confusion matrix
Source of confusion or error matrix. Is  a way to evaluate performance of the neural network.

![alt text](/labs/resources/cm.png "Confusion_matrix") [2]

Take a look the diagonal of the confusion matrix which tells you how well your model works.

## Validation methods
* __Training Dataset:__ The sample of data used to fit the model.
* __Validation Dataset:__ The sample of data used to provide an unbiased evaluation of a model fit on the training dataset while tuning model hyperparameters. The evaluation becomes more biased as skill on the validation dataset is incorporated into the model configuration.
* __Test Dataset:__ The sample of data used to provide an unbiased evaluation of a final model fit on the training dataset. [1]

### Hold-out Validation
Hold-out is when you split up your dataset into a ‘train’ and ‘test’ set. The training set is what the model is trained on, and the test set is used to see how well that model performs on unseen data. [3]

### K-Fold Cross-Validation
Cross-validation or ‘k-fold cross-validation’ is when the dataset is randomly split up into ‘k’ groups. One of the groups is used as the test set and the rest are used as the training set.[3]

### Leave-K-Out Cross-Validation
 For very limited number o samples we are leaving only specific number of examples.(1 ,10 ,100). This is the same very similar as K-Fold.

 # Exercise
 1. Implement K-Fold and Leave-K-Out crossvalidation to IRIS dataset with NN as an Estimator.
 2. Plot confusion matrices for all of the results.

# References
1. Brownlee, J. What is the Difference Between Test and Validation Datasets? https://machinelearningmastery.15com/difference-test-validation-datasets/.  (Accessed on 02/12/2020)
2. Confusion  matrix  -  Wikipedia.https://en.wikipedia.org/wiki/Confusion_matrix. (Accessed  on1702/12/2020).
3. https://medium.com/@eijaz/holdout-vs-cross-validation-in-machine-learning-7637112d3f8f
4.https://medium.com/@pranoyradhakrishnan/when-to-stop-training-your-neural-network-174ff0a6dea5
