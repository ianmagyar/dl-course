import numpy as np


image1 = np.array([
    [3, 2, 1, 2, 0],
    [0, 4, 2, 0, 1],
    [0, 2, 3, 1, 1],
    [1, 3, 4, 0, 0],
    [2, 1, 2, 1, 0]
])

filter1 = np.array([
    [0, 1, 2],
    [2, 2, 0],
    [0, 1, 2]
])

image2 = np.array([
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
])

filter2 = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]
])


def get_result_array(image_shape, kernel_shape, stride, P):
    """
    Calculates the dimension of the output of convolution and pooling, returns
    an array of zeros with the given dimensions. It uses the equation:
    dimension = (image_dimension - kernel_dimension + 2 * padding) / stride + 1

    Inputs:
     - image_shape - a tuple with the dimensions of the input image
                     (height x width (x channels))
     - kernel_shape - a tuple with the dimensions of the convolution filter
                      (height x width)
     - stride - integer
     - P - integer, the number of padded 0s on each side of the image
    """

    return None


def get_padding_value(kernel_shape, stride, padding):
    """
    Calcuates the padding value (the number of 0s to be added to the image on
    each side). Returns an integer - 0 for no padding and the padding value
    for 'same' padding. Uses the equation:
    P = (kernel_dimension - 1) / 2

    Inputs:
     - kernel_shape - a tuple with the dimensions of the convolution filter
                      (height x width)
     - stride - integer
     - padding - string, can have values 'none' and 'same'
    """

    return 0


def get_padded_image(image, P):
    """
    Returns the image padded by P 0s on each side as a numpy array.

    Inputs:
     - image - a numpy array representing an image
     - P - padding value, a non-negative integer
    """

    return image


def convolve(image, kernel, stride=1, padding='none'):
    """
    Carries out convolution on the given image with the given filter or kernel
    with the given parameters stride and padding. Returns a numpy array with
    the resulting feature map.

    Inputs:
     - image - a numpy array representing an image
     - kernel - a numpy array representing the convolution filter
     - stride - integer
     - padding - string, can have values 'none' and 'same'
    """

    return image


def max_pool(image, kernel_size, stride=1, padding='none'):
    """
    Carries out max pooling on the given image with the given kernel size
    with the given parameters stride and padding. Returns a numpy array with
    the resulting feature map.

    Inputs:
     - image - a numpy array representing an image
     - kernel_size - a tuple representing the filter size (height x width)
     - stride - integer
     - padding - string, can have values 'none' and 'same'
    """

    return image


def avg_pool(image, kernel_size, stride=1, padding='none'):
    """
    Carries out max pooling on the given image with the given kernel size
    with the given parameters stride and padding. Returns a numpy array with
    the resulting feature map.

    Inputs:
     - image - a numpy array representing an image
     - kernel_size - a tuple representing the filter size (height x width)
     - stride - integer
     - padding - string, can have values 'none' and 'same'
    """

    return image


if __name__ == '__main__':
    print(convolve(image1, filter1, stride=1, padding='none'))
    print(convolve(image2, filter2, stride=1, padding='none'))
    print(max_pool(image2, (2, 2), stride=1, padding='none'))
    print(avg_pool(image2, (2, 2), stride=1, padding='none'))
