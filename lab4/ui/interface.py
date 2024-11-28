from lab4.services.art_generator import generate_ascii_art
from lab4.ui.user_input import get_user_text, get_user_symbol_set, get_dimensions
from lab4.services.text_alignment import align_text
from lab4.services.file_handler import save_to_file
from lab4.ui.preview import preview_art
from lab4.services.color_option import apply_color
from lab4.services.utils import clear_screen

def main():
    clear_screen()
    print("Welcome to the ASCII Art Generator!")
    
    user_text = get_user_text()
    symbol_set = get_user_symbol_set()
    width, height = get_dimensions()
    
    ascii_art = generate_ascii_art(user_text, symbol_set, width, height)
    
    alignment = input("Choose text alignment (left, center, right) (default is left): ").strip().lower()
    alignment = alignment if alignment in ["left", "center", "right"] else "left"
    aligned_art = align_text(ascii_art, alignment, width)
    
    color_choice = input("Choose color option (bw for black & white, gray for grayscale) (default is bw): ").strip().lower()
    color_choice = color_choice if color_choice in ["bw", "gray"] else "bw"
    colored_art = apply_color(aligned_art, color_choice)
    
    print("\nPreview of your ASCII Art:")
    preview_art(colored_art)
    
    save_option = input("Would you like to save your ASCII art to a file? (yes/no): ").strip().lower()
    if save_option == "yes":
        file_name = input("Enter the file name (without extension): ").strip()
        save_to_file(colored_art, file_name)
        print(f"Your ASCII art has been saved to {file_name}.txt")
    
    print("Thank you for using the ASCII Art Generator!")

if __name__ == "__main__":
    main()
