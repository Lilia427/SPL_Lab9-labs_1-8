import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def handle_error(message):
    print(f"Error: {message}")
