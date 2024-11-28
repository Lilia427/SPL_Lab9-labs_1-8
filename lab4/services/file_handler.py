import os

def save_to_file(ascii_art, file_name):
    directory = "saved_art"
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, f"{file_name}.txt")
    
    if os.path.exists(file_path):
        overwrite = input(f"{file_name}.txt already exists in {directory}. Overwrite? (yes/no): ").strip().lower()
        if overwrite != "yes":
            print("File not saved.")
            return
    
    with open(file_path, "w") as file:
        file.write(ascii_art)
    
    print(f"Your ASCII art has been saved to {file_path}")
