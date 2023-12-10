from PIL import Image
import os

def resize_image(input_path, output_path, new_size):
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Resize the image and save it
            img.resize(new_size).save(output_path)
            # resized_img
            print(f"Image resized and saved to: {output_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Provide input and output paths, and specify the new size
    input_image_path = "sieving .jpg"
    output_image_path = "resized_image.jpg"
    new_size = (300, 200)  # Specify the new width and height in pixels

    # Call the resize_image function
    resize_image(input_image_path, output_image_path, new_size)
