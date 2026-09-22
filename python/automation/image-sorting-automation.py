# Automation script: archive image files that have not been modified recently

import os
import time


def script():
    path = input("Enter the folder path containing the images: ").strip()

    if not os.path.isdir(path):
        print("The specified folder does not exist.")
        return

    current_time = time.time()
    images = os.listdir(path)
    archive_folder = "Archived_Images"

    for image in images:
        print("=" * 30, "\n", image)

        full_path = os.path.join(path, image)

        if not os.path.isfile(full_path):
            continue

        modification_time = os.path.getmtime(full_path)
        elapsed_time = current_time - modification_time

        if elapsed_time > 100:
            archive_path = os.path.join(path, archive_folder)
            os.makedirs(archive_path, exist_ok=True)

            new_path = os.path.join(archive_path, image)
            os.rename(full_path, new_path)
            print(f"{image} was moved to {archive_folder}.")

        print(f"Elapsed time: {elapsed_time:.0f} seconds")


script()
