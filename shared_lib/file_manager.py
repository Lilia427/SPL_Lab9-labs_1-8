import os

class FileManager:
    """A class for file management operations."""

    @staticmethod
    def read_file(file_path):
        """Read the contents of a file."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
        with open(file_path, 'r') as file:
            return file.read()

    @staticmethod
    def write_file(file_path, content):
        """Write content to a file."""
        with open(file_path, 'w') as file:
            file.write(content)

    @staticmethod
    def append_to_file(file_path, content):
        """Append content to an existing file."""
        with open(file_path, 'a') as file:
            file.write(content)
