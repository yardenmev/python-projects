import os
import subprocess
import zipfile
import tkinter as tk
from tkinter import messagebox

zipf = zipfile.ZipFile('folder.zip', 'w', zipfile.ZIP_DEFLATED)
folder_to_zip = "root-folder"

# Initialize counters for avi and mp3 files
avi_count_before = 0
mp3_count_after = 0

def convert_video_to_mp3(input_file, output_file):
    try:
        ffmpeg_cmd = ["ffmpeg", "-i", input_file, "-vn", "-y", output_file]
        subprocess.run(ffmpeg_cmd, check=True)
    except Exception as e:
        print(f"Error converting {input_file} to MP3: {str(e)}")

# Count the number of .avi files before conversion
for root, dirs, files in os.walk(".", topdown=True):
    for file in files:
        if file.endswith(".avi"):
            avi_count_before += 1

# Perform the conversion
for root, dirs, files in os.walk(".", topdown=True):
    for file in files:
        if file.endswith(".avi"):
            base_name, ext = os.path.splitext(file)
            old_name = os.path.join(root, base_name + ".avi")
            new_name = os.path.join(root, base_name + ".mp3")

            convert_video_to_mp3(old_name, new_name)

# Count the number of .mp3 files after conversion
for root, dirs, files in os.walk(".", topdown=True):
    for file in files:
        if file.endswith(".mp3"):
            mp3_count_after += 1

def zip_folder(folder_path, zipf):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            zipf.write(os.path.join(root, file))
        for dir in dirs:
            zip_folder(os.path.join(root, dir), zipf)

zip_folder(folder_to_zip, zipf)
zipf.close()

# Calculate the difference in file counts
avi_count_after = mp3_count_after  # Assuming one-to-one conversion
file_difference = avi_count_before - mp3_count_after

# Create a Tkinter window to display the information
window = tk.Tk()
window.withdraw()  # Hide the main window

# Display a message box with the results
# message = 
if file_difference >= 1:
    message = f"Total .avi files before conversion: {avi_count_before}\n" \
              f"Total .mp3 files after conversion: {mp3_count_after}\n" \
              f"Total .avi files that didn't convert: {file_difference} "
else:
    message = "All files converted successfully "

messagebox.showinfo("Conversion Results", message)

# Close the Tkinter window after displaying the message box
window.destroy()
