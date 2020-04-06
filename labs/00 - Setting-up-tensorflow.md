# Lab 0: Getting ready!

In this course, you'll be programming in Python to create and train deep learning models with various tools. In this tutorial, we'll explain how to set up your programming environment for using TensorFlow and Keras.

## Step 1: Installing Python
We'll be using Python 3 which is available for download from the [language's web page](https://www.python.org/downloads/); we recommend, however, you use the [Anaconda distribution](https://www.anaconda.com/), which contains some useful libraries for machine learning by default.

### Step 1.1: Installing Anaconda
Anaconda is a freeware distribution that you can download [here](https://www.anaconda.com/distribution/). Make sure to install the latest Python 3 version.

### Step 1.2: Create a virtual environment in Anaconda
Anaconda is available only for the latest version of Python, 3.7 at the time of writing this manual. In Python and Anaconda, however, you can create a virtual environment, which will help us to work with TensorFlow and Keras. Virtual environments enable you to install libraries and frameworks without affecting the main installation.

To create a virtual environment, start Anaconda Prompt with admin privileges and enter the following command:

```conda create --name VENV_NAME python=3.7```

where `VENV_NAME` is any name you'd like to give to the virtual environment. To work with the virtual environment, you must first activate the virtual environment:

```conda activate VENV_NAME```

To return to the base environment, type:

```conda deactivate```

### Step 1.3: Upgrade some selected libraries
Through the Anaconda prompt, you can upgrade/install some libraries that you'll surely use during the semester:

```
pip install --upgrade numpy
pip install --upgrade matplotlib
pip install --upgrade scipy
pip install --upgrade sklearn
```

## Step 2: Installing TensorFlow and Keras
You can use the tool `pip` to install any libraries by entering the following command to the Anaconda prompt:

```
python -m pip install tensorflow
python -m pip install keras
```

This installs `TensorFlow` and `Keras` with all their dependencies. In case of errors please refer to the installation guides of [TensorFlow](https://www.tensorflow.org/install/pip) or [Keras](https://keras.io/#installation).

## Step 3: Checking your installation
Now we'll check whether all tools have been installed properly. In your virtual environment, start python by typing `python` and try to import TensorFlow and Keras:

```
import tensorflow
import keras
```

The first import might take a few seconds. If, during importing, an error occurs with one of the libraries, you need to upgrade it as in Step 1.3.

You can stop python running by typing `exit()` and then exiting Anaconda prompt.