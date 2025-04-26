import os
import shutil


FOLDER_MAP = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx', '.csv', '.odt'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
    'Code': ['.py', '.js', '.html', '.css', '.cpp', '.c', '.java', '.cs', '.php', '.rb', '.ts', '.swift', '.go', '.kt'],
    'Applications': ['.exe', '.msi', '.apk', '.dmg', '.pkg', '.deb'],
    'Fonts': ['.ttf', '.otf', '.woff', '.woff2'],
    'System': ['.dll', '.sys', '.ini', '.bat', '.cfg'],
    'Others': []  # Anything else you want to catch manually
}

def file_type(dir_path):
    files = os.listdir(dir_path)
    for file in files:

        if os.path.isdir(os.path.join(dir_path, file)):
            continue
        moved = False
        ext = os.path.splitext(file)[1].lower()

        for folder,extentions in FOLDER_MAP.items():
            
            if ext in extentions :
                file_move(dir_path, file, folder)
                moved = True
                break
            
        if not moved:
            file_move(dir_path, file, 'Others')
                
def file_move(dir_path,file_name, name):
    if not os.path.exists(os.path.join(dir_path, name)):
        os.mkdir(os.path.join(dir_path, name))
    shutil.move(os.path.join(dir_path, file_name), os.path.join(dir_path, name, file_name))
                    

                
    

