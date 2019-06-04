from astropy.io import fits
import sys
import numpy as np
from PIL import Image


def get_image(filename):
    extension = filename.split(".")[-1]
    
    if extension in ["fits", "fz"]:
        return np.flipud(fits.getdata(filename))
        
    else:
        return np.array(Image.open(sys.argv[1]))


def scale_image(img, percentile=99, scaling="log"):
    img = img.clip(min=0, max=np.nanpercentile(img, percentile))
    img = np.log(img+ 0.001)
    
    return img


def generate_image(filename):
        
    img = get_image(filename)
    #img = scale_image(img)
        
    img = Image.fromarray(img)
    img = img.resize((200, 200), Image.ANTIALIAS)

    img = img.convert('1', dither=Image.FLOYDSTEINBERG)

    img.save("test.png")


if __name__ == "__main__":
    generate_image(sys.argv[1])
