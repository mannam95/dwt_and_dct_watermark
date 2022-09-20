from scipy.fftpack import dct
from scipy.fftpack import idct
import numpy as np

# Refer https://docs.scipy.org/doc/scipy/reference/generated/scipy.fftpack.dct.html
# Refer https://inst.eecs.berkeley.edu/~ee123/sp16/Sections/JPEG_DCT_Demo.html


def dct_2d(data):
    """
    This function does 2D Discrete Cosine Transform(DCT).

    :param data: 2D array with input data.
    :return: Return the Discrete Cosine Transform.
    """
    size = data[0].__len__()
    all_subdct = np.empty((size, size))
    for i in range (0, size, 8):
        for j in range (0, size, 8):
            subpixels = data[i:i+8, j:j+8]
            subdct = dct(dct(subpixels.T, norm="ortho").T, norm="ortho")
            all_subdct[i:i+8, j:j+8] = subdct

    return all_subdct


def idct_2d(data):
    """
    This function does 2D inverse Discrete Cosine Transform(DCT).

    :param data: 2D array with dct coefficient matrix.
    :return: Return the original data by performing inverse Discrete Cosine Transform.
    """
    size = data[0].__len__()
    all_subidct = np.empty((size, size))
    for i in range (0, size, 8):
        for j in range (0, size, 8):
            subidct = idct(idct(data[i:i+8, j:j+8].T, norm="ortho").T, norm="ortho")
            all_subidct[i:i+8, j:j+8] = subidct

    return all_subidct