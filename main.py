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

# Obtain the path of the downloads folder for your os
if get_platform() == 'Windows':
    downloads_path = os.path.join(os.environ['USERPROFILE'], 'Downloads')
elif get_platform() == 'Linux' or 'Mac':
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
else: 
    print(f'Your {os.name} is not supported')
    exit()

# a dictionary to map file extensions to categories
# 162 files ext 160+ file types supported
file_categories = {
    'Audio': ('.mp3', '.wav', '.flac', '.aac', '.ogg', '.aiff', '.xspf', '.wma', '.mp2', '.au', '.m4a', '.3gp' , '.3gp2', '.3gpp', '.669', '.a52', '.ac3', '.adt', '.adts', '.aif', '.aifc', '.aob', '.ape', '.caf', '.cda', '.dts', '.dv', '.xa', '.wv', '.weba', '.wax'),    
    'Video': ('.mp4', '.avi', '.mkv', '.mov', '.webm', '.flv', '.wmv', '.bik', '.mts', '.drc', '.amv', '.asf', '.dav', '.divx', '.f4v', '.wtv',),
    'Images': ('.jpg', '.jpeg', '.avif', '.png', '.gif', '.bmp', '.webp', '.jfif', '.svg', '.ico', '.pcx', '.ppm', '.cap', '.arw', '.bay', '.cr3', '.crw', '.dcr', '.dcs', '.dib', '.drf', '.erf', '.fff', '.hif', '.wmf', '.wbmp', '.heic'),
    'Documents': ('.pdf', '.epub', '.doc', '.docx', '.txt', '.ppt', '.xlsx', '.tsv','.ods', '.odt', '.odp', '.odf', '.odg', '.accdb', '.rtf', '.md', '.csv', '.pages', '.sxw', '.wpd', '.srt', '.ass', '.lrc', '.lic', '.md'),
    'Archives': ('.zip', '.rar', '.7z', '.tar', '.gz', '.tar.xz', '.dmg', '.001', '.arj', '.bz2', '.bz', '.zst', '.zipx', '.z', '.xz', '.xxe'),
    'Programs': ('.exe', '.msi', '.app', '.dmg', '.deb', '.dll', '.jar', '.apk', '.apk+', '.rpm', '.iso', '.aab', '.mpqe', ),
    'Fonts': ('.woff', '.woff2', '.otf', '.ttf'),
    'Designs': ('.xcf', '.eps', '.ai', '.blend', '.bw', '.dicom', '.exr', '.flc', '.fli', '.g3'),
    'Scripts': ('.py', '.js', '.ts', '.sh', '.bat', '.bas', '.ini', '.ino', '.rb', '.bashrc', '.cpp', '.cs', '.java', '.json', '.php', '.pl', '.sql', '.xml', '.yaml', '.yml'),
    'Others': ('.bin')
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

print("Your Downloads folder has been organized successfully!")
