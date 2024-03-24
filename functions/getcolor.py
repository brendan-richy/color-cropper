import cv2
from PIL import Image

def getcolor(img, selectedpixel):
    color = img.getpixel(selectedpixel)
    return color