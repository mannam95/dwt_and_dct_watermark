import numpy as np
from PIL import Image


# Convert image to grayscale if necessary
def convert_image(image_name, size, isRGB = True):
    img = Image.open(image_name).resize((size, size), 1)
    if isRGB:
      img = img.convert('L')
 
    image_array = np.array(img.getdata(), dtype=np.float64).reshape((size, size))

    return image_array