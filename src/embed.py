import os
import numpy as np
from PIL import Image
from dct import dct_2d, idct_2d
from dwt import dwt_2d, idwt_2d


class Embed():
    """This class defines config options.

    It also implement a function which will integrate the embedding.
    """

    def __init__(self, options):
        """Init the class."""
        self.options = options
    

    def embed_watermark_to_all_dct_blocks(self, image_array, watermark_array):
        """
        This function embeds watermark to all the blocks of DCT.

        :param image_array: dct blocks of the image.
        :param watermark_array: watermark image.
        :return: Returns the embedded dct array.
        """
        watermark_flat = watermark_array.ravel()
        ind = 0
        
        for x in range (0, len(image_array), 8):
            for y in range (0, len(image_array), 8):
                if ind < len(watermark_flat):
                    subdct = image_array[x:x+8, y:y+8]
                    subdct[5][5] = watermark_flat[ind]
                    image_array[x:x+8, y:y+8] = subdct
                    ind += 1 

        return image_array


    def integrate_embedding(self):
        """
        This function does all the integration for watermark embedding

        :param options: config options.
        :return: Returns the embedded watermark image
        """

        # create the directory for saving embedded images.
        if not os.path.exists(self.options.save_emb_dir_path):
            os.makedirs(self.options.save_emb_dir_path)

        # This loop runs for all the files presented in the given dirctory
        for file in os.listdir(self.options.emb_dir_path):
            
            # open the image.
            org_img = Image.open(self.options.emb_dir_path + '/' + file)

            # convert the image to grayscale.
            org_img = np.asarray(org_img.convert(mode='L'))

            # open the watermark image.
            wat_img = Image.open(self.options.wat_dir_path + '/' + file)

            # convert the watermark to grayscale.
            wat_img = np.asarray(wat_img.convert(mode='L'))

            # Apply 2d-DWT and get coeffs.
            coeffs_image = dwt_2d(org_img)

            # Apply DCT to DWT - LL coeff.
            dct_array = dct_2d(coeffs_image[0])

            # Apply watermark to all blocks of DCT.
            wat_dct_array = self.embed_watermark_to_all_dct_blocks(dct_array, wat_img)

            # Inverse of DCT and update the DWT-LL coeff
            coeffs_image[0] = idct_2d(wat_dct_array)

            # Apply Inverse 2d-DWT
            image_array_H = idwt_2d(coeffs_image, 'haar')

            # Save thq embedded image.
            # plt.imsave(config.embedded_images_path + "test.png", embedded_image, cmap=cm.gray)
            im = Image.fromarray(image_array_H)
            im.convert("L").save(self.options.save_emb_dir_path + "/" + file)
