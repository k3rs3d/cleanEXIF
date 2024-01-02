# cleanEXIF 

## Overview

EXIF (Exchangeable Image File Format) data often contains metadata such as camera settings, date, and location, which can be sensitive or unnecessary for certain use cases.

This Python script removes EXIF data from images in a specified directory, using the Python Imaging Library (PIL) to manipulate image files. 

## Features

- Recursively scans a specified directory and its subdirectories for image files (BMP, PNG, JPG, JPEG, GIF).
- Lists the found image files and their count.
- Prompts the user for confirmation before proceeding with EXIF data removal.
- Saves modified images with their original file path, overwriting original images.

## Usage

1. Clone the repository.

2. Navigate to the script directory.

3. Run the script:

    ```bash
    python exif_cleaner.py
    ```

4. Enter the folder path containing the images when prompted.

5. Review the list of found images and confirm to proceed with EXIF data removal.

## Requirements

- Python 3.x
- Pillow library (PIL fork)

Install Pillow using:

```bash
pip install pillow
```
