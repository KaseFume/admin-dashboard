# storage.py
from django.core.files.storage import FileSystemStorage

class ClassSpecificStorage(FileSystemStorage):
    def __init__(self, location=None, base_url=None):
        # Store files in the specified location (e.g., 'images/')
        super().__init__(location=location, base_url=base_url)
