import cv2

def selectpixel(event, x, y, flags, param):
    image_path = param
    image = cv2.imread(image_path)
    if event == cv2.EVENT_LBUTTONDOWN:
        selected_pixel = (x, y)
        print("Selected pixel coordinates:", selected_pixel)
