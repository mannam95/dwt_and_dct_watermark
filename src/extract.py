import os
from matplotlib import cm, pyplot as plt
import numpy as np
from PIL import Image
from pathlib import Path
from dct import dct_2d

from dwt import dwt_2d


class Extract():
    """This class defines config options.

    It also implement a function which will integrate the extracting.
    """

    def __init__(self, options):
        """Init the class."""
        self.options = options
    

    def extract_watermark_from_all_dct_blocks(self, dct_watermarked_coeff, watermark_size):
        """
        This function extracts watermark from all the blocks of DCT.

        :param dct_watermarked_coeff: dct blocks of the watermarked image.
        :param watermark_size: size of the watermark image.
        :return: Returns the extracted watermark array.
        """
        subwatermarks = []

        for x in range (0, len(dct_watermarked_coeff), 8):
            for y in range (0, len(dct_watermarked_coeff), 8):
                coeff_slice = dct_watermarked_coeff[x:x+8, y:y+8]
                subwatermarks.append(coeff_slice[5][5])
        
        watermark = np.array(subwatermarks).reshape(watermark_size, watermark_size)

        return watermark


    def integrate_extraction(self):
        """
        This function does all the integration for watermark extraction

        :param None.
        :return: Returns the embedded watermark image
        """

        # create the extracted images path.
        if not os.path.exists(self.options.save_ext_dir_path):
            os.makedirs(self.options.save_ext_dir_path)

        # This loop runs for all the files presented in the given dirctory
        for index, file in enumerate(os.listdir(self.options.ext_dir_path)):

            # open the image.
            img = Image.open(self.options.ext_dir_path + '/' + file)

            # convert the image to grayscale.
            img = np.asarray(img.convert(mode='L'))

            # get the coefficients of DWT transform..
            coeffs_watermarked_image = dwt_2d(img, 'haar', 1)

            # Extract dct coefficients of the watermarked image.
            dct_watermarked_coeff = dct_2d(coeffs_watermarked_image[0])

            # Extract the watermark from the dct coefficients.
            watermark_array = self.extract_watermark_from_all_dct_blocks(dct_watermarked_coeff, self.options.watermark_size)

            # Convert the data type to uint8.
            watermark_array =  np.uint8(watermark_array)

            # Save the extracted watermark.
            img = Image.fromarray(watermark_array)
            img.convert("L").save(self.options.save_ext_dir_path + "/" + file)
