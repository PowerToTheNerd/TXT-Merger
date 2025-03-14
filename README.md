# Text File Merger

## Using the Executable File
If you prefer to use the executable file, simply download and run `txt_merger.exe`. This will handle the merging process without needing to follow the steps below.

If you don't care about the order ignore this and continue. If not I'd recommend naming them like note1.txt note2.txt in the order you want them in the main.txt file. The program will extract note1.txt first and so on.

Run the Executable: Double-click txt_merger_basic.exe.

Select a Folder: A file dialog will appear. Choose the folder containing the .txt files you want to combine.

Check Output:

A console window will appear, displaying the names of the .txt files being combined, any error messages, and a completion message.

Find the Result: The main.txt file, containing the combined text, will be located in the folder you selected. If you'd like to re run this for another set of .txt files i suggest renaming main.txt to anything else because the program will replace it if the name is the same.

## Overview
This tool combines all `.txt` files within a specified directory into a single output file. It includes an optional feature to sort files numerically based on a prefix, such as "section2.8.txt" and[...]

## Folder Path 
### Example
- Line 5: folder_path = r"C:\\Users\\(YOURUSERNAME)\\Desktop\\Script\\Notes"

## Features
- **Merge Text Files**: Combines multiple `.txt` files into one.
- **Optional Ordered Concatenation**: Sorts files numerically based on their prefixes before merging.

### Example
Given files:
- `section 2.8.txt`
- `section 10.2.txt`

The tool can sort and merge them in numerical order.

## Use txt_merger_basic.py 
If your `.txt` files are named in a simple numerical or alphabetical order, such as `note1.txt`, `2.txt`, `note3.txt`, you can use the basic file ordering feature to merge them in sequence.
