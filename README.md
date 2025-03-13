# Text File Merger

## Overview
This tool combines all `.txt` files within a specified directory into a single output file. It includes an optional feature to sort files numerically based on a prefix, such as "section2.8.txt" and "section10.2.txt".

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
