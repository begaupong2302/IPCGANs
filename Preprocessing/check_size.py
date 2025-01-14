from PIL import Image
import os

# Open an image file
# image_path = "../../FER/FER/happy"
image_path = "../../Exdata2/UTKFaceCrop"
def check_size(image_path):
    with Image.open(image_path) as img:
        # Get image dimensions (width, height)
        width, height = img.size
        print(f"Image dimensions: {width}x{height}")

z = 0
for i in os.listdir(image_path):
    check_size(os.path.join(image_path,i))
    z += 1
    if z > 1000:
        break

