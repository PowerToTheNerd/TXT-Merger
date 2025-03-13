import os
import re

# Use your folder path here. 
folder_path = r"folder path containing .txt files"

# Optional section custom sorting delete this if this won't work with your file names.
def natural_sort_key(text):
    """
    Break filename into alphanumeric chunks, converting digit chunks to integers.
    e.g. "Section 2.10_notes.txt" -> ["Section ", 2, ".", 10, "_notes.txt"]
    Sorting by these lists avoids string-based mis-ordering.
    """
    return [
        int(chunk) if chunk.isdigit() else chunk
        for chunk in re.split(r'(\d+)', text)
    ]

# List all .txt files in the folder, excluding main.txt 
txt_files = [
    f for f in os.listdir(folder_path)
    if f.endswith(".txt") and f.lower() != "main.txt"
]

# Sort the list using our natural sort key or use your own custom sorter or just sort.
txt_files.sort(key=natural_sort_key)

# I perosnally like to verify what files were read and made into the main.txt this can be removed.
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