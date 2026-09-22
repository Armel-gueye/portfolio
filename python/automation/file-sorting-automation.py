# Automation script: sort and move files into automatically created folders

import os

path = input("Enter the folder path to organize: ").strip()

if not os.path.isdir(path):
    print("The specified folder does not exist.")
else:
    files = os.listdir(path)

    for file_name in files:
        image_folder = "Image_Files"
        video_folder = "Video_Files"
        html_folder = "HTML_Files"
        python_folder = "Python_Files"
        zip_folder = "ZIP_Files"

        _, extension = os.path.splitext(file_name)
        extension = extension.lower()

        if extension in {".jpg", ".jpeg", ".png"}:
            destination_folder = image_folder
        elif extension == ".mp4":
            destination_folder = video_folder
        elif extension in {".html", ".htm"}:
            destination_folder = html_folder
        elif extension == ".py":
            destination_folder = python_folder
        elif extension == ".zip":
            destination_folder = zip_folder
        else:
            continue

        destination_path = os.path.join(path, destination_folder)
        os.makedirs(destination_path, exist_ok=True)

        source_file = os.path.join(path, file_name)
        target_file = os.path.join(destination_path, file_name)

        os.rename(source_file, target_file)
        print(f"Moved {file_name} to /{destination_folder}")
