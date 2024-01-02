from PIL import Image
import os


def remove_exif(file_path):
    img = Image.open(file_path)
    info = img.info

    if "exif" in info:
        del info["exif"]

    img.save(file_path, exif=b"")
    print(f"EXIF data removed for {file_path} and saved")


def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.bmp', '.png', '.jpg', '.jpeg', '.gif')):
                file_path = os.path.join(root, file)
                remove_exif(file_path)


# Execute
process_directory("images")
