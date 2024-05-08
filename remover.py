import rembg
import PIL
import os
import easygui as eg
from PIL import Image

def remove(image):
    im=Image.open(image)
    remove(im)
    im.save()
    print(image)






image_path=eg.fileopenbox()
remove(image_path)