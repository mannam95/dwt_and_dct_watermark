import pywt

# Refer https://pywavelets.readthedocs.io/en/latest/ref/2d-dwt-and-idwt.html 


def dwt_2d(data, wavelet="haar", level=1):
    """
    This function does two level 2D forward Discrete Wavelet Transform(DWT).

    :param data: 2D array with input data.
    :param wavelet: type of wavelet.
    :param level: level of decomposition.
    :return: Approximation(LL), horizontal detail(LH), vertical detail(HL) and diagonal detail(HH) coefficients respectively.
    """
    coeffs = pywt.wavedec2(data = data, wavelet = wavelet, level = level)
    coeffs_H = list(coeffs) 
   
    return coeffs_H


def idwt_2d(coeffs, wavelet="haar"):
    """
    This function does teo level 2D inverse Discrete Wavelet Transform(DWT).
    Reconstructs data from coefficient arrays.

    :param coeffs: Approximation(LL), horizontal detail(LH), vertical detail(HL) and diagonal detail(HH) coefficients respectively.
    :param wavelet: Wavelet object or name string, or 2-tuple of wavelets. This can also be a tuple containing a wavelet to apply along each axis in axes.
    :return: an image array reconstructed from the coefficients.
    """
    image_array_H = pywt.waverec2(coeffs, wavelet)

    return image_array_H
