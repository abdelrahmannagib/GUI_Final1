import tkinter as tk
from tkinter import filedialog
import shutil
import os

def select_and_save_image(destination_folder):
    # Create a root window and hide it
    root = tk.Tk()
    root.withdraw()

    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")]
    )

    # Check if a file was selected
    if file_path:
        # Get the filename
        file_name = os.path.basename(file_path)

        # Ensure the destination folder exists
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Create the destination path
        destination_path = os.path.join(destination_folder, file_name)

        # Copy the selected image to the destination folder
        shutil.copy(file_path, destination_path)

        print(f"Image saved to {destination_path}")
    else:
        print("No file selected")

# Example usage
destination_folder = "CameraPhotos"
select_and_save_image(destination_folder)
