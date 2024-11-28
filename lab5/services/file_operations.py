class FileOperations:
    @staticmethod
    def save_to_file(ascii_art, filename):
        with open(filename, "w") as file:
            file.write(ascii_art)
        print(f"ASCII art saved to {filename}")

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, "r") as file:
                return file.read()
        except FileNotFoundError:
            print(f"File {filename} not found.")
            return ""