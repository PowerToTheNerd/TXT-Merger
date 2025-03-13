import os
import re

# Use your folder path here. 
folder_path = r"folder path containing .txt files"

# List all .txt files in the folder, excluding main.txt 
txt_files = [
    f for f in os.listdir(folder_path)
    if f.endswith(".txt") and f.lower() != "main.txt"
]

# Sort the list using the basic sort method
txt_files.sort()

# I personally like to verify what files were read and made into the main.txt this can be removed.
print("Files in sorted order:")
for file_name in txt_files:
    print(" | ", file_name, " | ")

# Open main.txt for writing (overwrites if it exists)
with open(os.path.join(folder_path, "main.txt"), "w", encoding="utf-8") as main_file:
    for filename in txt_files:
        file_path = os.path.join(folder_path, filename)
        try:
            # Read each note file as UTF-8
            with open(file_path, "r", encoding="utf-8") as note_file:
                content = note_file.read()
                main_file.write(content + "\n")
        except UnicodeDecodeError as e:
            print(f"Unicode decode error reading {filename}: {e}")
        except Exception as e:
            print(f"Error reading {filename}: {e}")

# Result
print("All files have been combined into main.txt")
