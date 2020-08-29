from PIL import Image

img = Image.open("input.jpg")
info = img.info

if "exif" in info:
    del info["exif"]
img.save("output.jpg", exif=b"")