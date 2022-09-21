import os
from PIL import Image
from dct import dct_2d, idct_2d
from dwt import dwt_2d, idwt_2d
from utils import convert_image
from tqdm import tqdm


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

    def save_image_from_array(self, image_array, file_path):
        """
        This function saves the image from the given array.

        :param image_array: image array.
        :param file_path: path of the file.
        :return: None.
        """
        image_array_copy = image_array.clip(0, 255)
        image_array_copy = image_array_copy.astype("uint8")
        img = Image.fromarray(image_array_copy)
        img.save(file_path)



    def integrate_embedding(self):
        """
        This function does all the integration for watermark embedding

        :param options: config options.
        :return: Returns the embedded watermark image
        """
        model = 'haar'
        level = 1

        # create the directory for saving embedded images.
        if not os.path.exists(self.options.save_emb_dir_path):
            os.makedirs(self.options.save_emb_dir_path)

        # This loop runs for all the files presented in the given dirctory
        for file in tqdm(os.listdir(self.options.emb_dir_path)):

            image_array = convert_image(self.options.emb_dir_path + '/' + file, 512)
            watermark_array = convert_image(self.options.wat_dir_path, self.options.watermark_size)

            # Apply 2d-DWT and get coeffs.
            coeffs_image = dwt_2d(image_array, model, level)

            # Apply DCT to DWT - LL coeff.
            dct_array = dct_2d(coeffs_image[0])

            # Apply watermark to all blocks of DCT.
            wat_dct_array = self.embed_watermark_to_all_dct_blocks(dct_array, watermark_array)

            # Inverse of DCT and update the DWT-LL coeff
            coeffs_image[0] = idct_2d(wat_dct_array)

            # Apply Inverse 2d-DWT
            image_array_H = idwt_2d(coeffs_image, model)

            # Save thq embedded image.
            # plt.imsave(config.embedded_images_path + "test.png", embedded_image, cmap=cm.gray)
            self.save_image_from_array(image_array_H, self.options.save_emb_dir_path + '/' + file)
