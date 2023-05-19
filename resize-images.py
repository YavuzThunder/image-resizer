import os
from PIL import Image


def resize_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                image = Image.open(input_path)
                resized_image = image.resize((32, 32), Image.ANTIALIAS)
                resized_image.save(output_path, "JPEG")
                print(f"Resized {filename}")
            except IOError:
                print(f"Failed to resize {filename}")


# Enter the path of your input and output files, respectively, in the fields in quotation marks.
input_folder = "C:/Users/yavuz/Desktop/input"
output_folder = "C:/Users/yavuz/Desktop/output"

resize_images(input_folder, output_folder)
