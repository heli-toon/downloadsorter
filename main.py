import os
import shutil
import mimetypes

# Checking your OS
def get_platform():
    platforms = {
        'linux1': 'Linux',
        'posix': 'Linux',
        'linux2': 'Linux',
        'darwin': 'macOS',
        'win32': 'Windows',
    }
    if os.name not in platforms:
        return os.name
    return platforms[os.name]

print(f"You are running on {get_platform()}.")

# Obtain the path of the downloads folder
if get_platform() == 'Windows':
    downloads_path = os.path.join(os.environ['USERPROFILE'], 'Downloads')
elif get_platform() == 'Linux' or 'Mac':
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
else: 
    print(f'Your {os.name} is not supported')
    exit()

# Create a dictionary to map file extensions to categories
file_categories = {
    'Audio': ('.mp3', '.wav', '.flac', '.aac', '.ogg', '.aiff'),
    'Video': ('.mp4', '.avi', '.mkv', '.mov', '.webm', '.flv'),
    'Images': ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.jiff', '.svg'),
    'Documents': ('.pdf', '.doc', '.docx', '.txt', '.ppt', '.xlsx', '.ods'),
    'Archives': ('.zip', '.rar', '.7z', '.tar', '.gz', '.tar.xz', '.dmg'),
    'Programs': ('.exe', '.msi', '.app', '.dmg', '.deb', '.dll', '.jar', '.app', '.rpm'),
    'Others': ()
}
# Get all files in the downloads folder
files = [f for f in os.listdir(downloads_path) if os.path.isfile(os.path.join(downloads_path, f))]

# Categorize files and move them to the appropriate subfolder
for file in files:
    file_path = os.path.join(downloads_path, file)
    file_type, _ = mimetypes.guess_type(file_path)
    for category, extensions in file_categories.items():
        if file_type and any(file.lower().endswith(ext) for ext in extensions):
            target_folder = os.path.join(downloads_path, category)
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            shutil.move(file_path, os.path.join(target_folder, file))
            break

print("Downloads folder organized successfully!")
