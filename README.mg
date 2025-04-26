# File Organizer Bot 🗂️

A Python script that automatically organizes files into categorized folders based on their extensions.

## Features
- **Automatic Categorization**: Sorts files into appropriate folders (Images, Documents, etc.)
- **Directory Creation**: Automatically creates needed folders
- **Comprehensive Support**: Handles 100+ file extensions
- **Simple Interface**: Easy-to-use command line tool

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Abdelrahman-progg/File-Organizer-Bot.git
   cd File-Organizer-Bot
Install dependencies:

bash
pip install -r requirements.txt
Usage
Run the script:

bash
python Main.py
When prompted, enter the path to the directory you want to organize.

Example:

Enter the path to the directory you want to organize:
C:\Users\YourName\Downloads
Supported File Types
Category	Example Extensions
Images	.jpg, .png, .gif, .webp
Videos	.mp4, .mov, .avi, .mkv
Audio	.mp3, .wav, .flac, .aac
Documents	.pdf, .docx, .xlsx, .pptx
Archives	.zip, .rar, .7z, .tar
Code	.py, .js, .html, .css
Applications	.exe, .msi, .dmg, .apk
Fonts	.ttf, .otf, .woff
System	.dll, .sys, .ini
Others	Any unclassified extensions
Project Structure
File-Organizer-Bot/
├── Main.py              # Main application entry point
├── Organize.py          # Core organization logic
├── test_Organize.py     # Unit tests
└── requirements.txt     # Dependencies
Testing
Run tests with:

bash
pytest test_Organize.py -v
Core Functions
file_type(dir_path)
Takes a directory path as input

Identifies and categorizes all files in the directory

Skips existing directories

file_move(dir_path, file_name, name)
Moves files to their categorized folders

Creates destination folders if they don't exist

Parameters:

dir_path: Parent directory path

file_name: Name of file to move

name: Destination folder name

