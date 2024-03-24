from PIL import Image
import random

def cropper(img, width, height, keepColor):
    matchingPixels = 0

    for x in range(0, width):
        for y in range(0, height):
            selected = img.getpixel((x, y))
            if selected != keepColor:
                img.putpixel((x, y), (0, 0, 0, 0))
            else:
                matchingPixels = matchingPixels + 1
    
    print(f"Matching Pixles: {matchingPixels}")

    return img