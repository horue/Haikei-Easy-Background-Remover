import rembg
import PIL
import os
import easygui as eg
from PIL import Image

def remove(image):
    Image.open(image)
    print(image)






image_path=eg.fileopenbox()
remove(image_path)