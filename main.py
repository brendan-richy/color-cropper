import cv2
from PIL import Image
from selectfile import selectFile
from cropper import cropper
from filepaths import outputpath

# Select file
input_image_path = selectFile()
output_image_path = outputpath(input_image_path)


# Convert to RGBA and get basic info
input_image = Image.open(input_image_path)
img = input_image.convert('RGBA')
width, height = input_image.size



selected_pixel = None

def on_mouse_click(event, x, y, flags, param):
    global selected_pixel
    if event == cv2.EVENT_LBUTTONDOWN:
        selected_pixel = (x, y)

# Load your image
image = cv2.imread(input_image_path)

if image is None:
    print("Error: Image not loaded. Please check the file path.")
else:
    cv2.imshow("Select a color to keep", image)
    cv2.setMouseCallback("Select a color to keep", on_mouse_click)

    while True:
        key = cv2.waitKey(1) & 0xFF
        if selected_pixel is not None:
            break

    cv2.destroyAllWindows()

if selected_pixel is not None:
    keepColor = input_image.getpixel(selected_pixel)
    print("Selected Pixel:", selected_pixel)
    print("Keep Color:", keepColor)

    modified_img = cropper(img, width, height, keepColor)

    modified_img.save(output_image_path)
else:
    print("No pixel selected. Exiting without processing.")
