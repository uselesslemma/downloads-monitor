import time
import os
import hashlib
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DownloadHandler(FileSystemEventHandler):
    def __init__(self, download_folder):
        self.download_folder = download_folder

    def on_created(self, event):
        if event.is_directory:
            return
        file_path = event.src_path
        print(f"New file detected: {file_path}")
        self.check_and_download(file_path)

    def get_file_hash(self, file_path):
        hasher = hashlib.md5()
        with open(file_path, 'rb') as file:
            buf = file.read()
            hasher.update(buf)
        return hasher.hexdigest()

    def check_and_download(self, file_path):
        file_hash = self.get_file_hash(file_path)

        for existing_file in os.listdir(self.download_folder):
            existing_file_path = os.path.join(self.download_folder, existing_file)
            if os.path.isfile(existing_file_path) and existing_file_path != file_path:
                existing_file_hash = self.get_file_hash(existing_file_path)
                if file_hash == existing_file_hash:
                    print(f"Duplicate file detected: '{file_path}' is the same as '{existing_file_path}'.")
                    os.remove(file_path)
                    print(f"File '{file_path}' removed.")
                    return

        print(f"File '{file_path}' has been verified as unique. Standing down...")

def monitor_downloads(download_folder):
    event_handler = DownloadHandler(download_folder)
    observer = Observer()
    observer.schedule(event_handler, download_folder, recursive=False)
    observer.start()
    print(f"Monitoring {download_folder} for new files...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def main():
    from .config import get_config
    config = get_config()
    download_folder = config.get('download_folder')
    monitor_downloads(download_folder)
