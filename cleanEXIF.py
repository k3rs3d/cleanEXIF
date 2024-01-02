from PIL import Image
import os


def remove_exif(file_path):
    # Open image file & retrieve its metadata
    img = Image.open(file_path)
    info = img.info

    if "exif" in info:
        del info["exif"]

    # Save the modified image with EXIF data removed
    img.save(file_path, exif=b"")
    print(f"EXIF data removed for {file_path} & file saved")


def process_directory(directory):
    image_files = []

    # Traverse the specified directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.bmp', '.png', '.jpg', '.jpeg', '.gif')):
                file_path = os.path.join(root, file)
                image_files.append(file_path)

    if not image_files:
        print("No images found in the specified directory.")
        return

    # Display the found image files + their count
    print("Found the following images:")
    for file_path in image_files:
        print(file_path)
    print(f"{len(image_files)} images found")

    # Prompt the user to confirm EXIF data removal
    user_input = input("Continue wiping EXIF? (Y/N): ").lower()
    if user_input == "y":
        # Iterate over each image file and remove EXIF data
        for file_path in image_files:
            remove_exif(file_path)
        print("EXIF data removal completed.")
    else:
        print("Operation canceled.")


def main():
    # Prompt user for the image directory
    user_folder = input("Enter the folder containing the images: ")

    # Check if the directory exists
    if not os.path.exists(user_folder):
        print(f"Error: Specified directory '{user_folder}' does not exist.")
        return

    process_directory(user_folder)


if __name__ == "__main__":
    main()