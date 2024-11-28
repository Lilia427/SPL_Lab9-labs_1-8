import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ui import CLI
from utils import FileOperations

def main():
    cli = CLI()
    ascii_art = cli.start()  

    save_option = input("Would you like to save the ASCII art to a file? (y/n): ")
    if save_option.lower() == 'y':
        filename = input("Enter the filename (e.g., art.txt): ")
        FileOperations.save_to_file(ascii_art, filename)

if __name__ == "__main__":
    main()