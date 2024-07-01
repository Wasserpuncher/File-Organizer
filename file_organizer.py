import os
import shutil

class FileOrganizer:
    def __init__(self, directory):
        self.directory = directory
        self.file_types = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
            'Documents': ['.txt', '.pdf', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx'],
            'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
            'Music': ['.mp3', '.wav', '.ogg', '.flac']
        }

    def organize_files(self):
        for filename in os.listdir(self.directory):
            if os.path.isfile(os.path.join(self.directory, filename)):
                file_ext = os.path.splitext(filename)[1].lower()
                file_category = self._get_category(file_ext)
                if file_category:
                    self._move_file(filename, file_category)

    def _get_category(self, file_ext):
        for category, extensions in self.file_types.items():
            if file_ext in extensions:
                return category
        return 'Other'

    def _move_file(self, filename, category):
        category_dir = os.path.join(self.directory, category)
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)
        src_path = os.path.join(self.directory, filename)
        dst_path = os.path.join(category_dir, filename)
        shutil.move(src_path, dst_path)
        print(f"Moved: {filename} to {category} directory.")

if __name__ == "__main__":
    directory = 'path/to/your/directory'
    organizer = FileOrganizer(directory)
    organizer.organize_files()
    print("File organization complete.")
