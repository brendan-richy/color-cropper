from PIL import Image
import random

def cropper(img, width, height):
    bgColor = img.getpixel((0, 0))

    while True:
        x = random.randint(0,width)
        y = random.randint(0, height)

        r, g, b, t = img.getpixel((x, y))

        if (r, g, b, t) != bgColor:
            print(f"({x}, {y}) Isn't background color")
            print(r, g, b, t)
            keepColor = r, g, b, t
            print(f"bgColor: {bgColor}")
            print(f"keepColor: {keepColor}")

            break
        else: 
            print(f"Is bg color")

    for x in range(0, width):
        for y in range(0, height):
            selected = img.getpixel((x, y))
            if selected != keepColor:
                img.putpixel((x, y), (0, 0, 0, 0))
                
                
                
                
                
                
    

    return img

input_image_path = "images/yellowblack.png"
output_image_path = "images/yellowblack_modified.png"

input_image = Image.open(input_image_path)
img = input_image.convert('RGBA')
width, height = input_image.size

modified_img = cropper(img, width, height)
modified_img.save(output_image_path)  # Save the modified image to a new file
