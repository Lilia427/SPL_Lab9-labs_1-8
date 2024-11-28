import os
from lab3.services.ascii_art import build_template_art
from lab3.services.color_styles import apply_color
from lab3.services.preview import preview_ascii_art
from lab3.data.config import Config

def main():
    text = input("Enter text: ")
    symbol = input("Enter symbol for ASCII art: ")
    
    # Use default symbol if none provided
    if not symbol:
        symbol = Config.default_symbol
    
    color = input("Choose color (red, green, blue, white): ").lower()
    
    # Build ASCII art and apply color
    ascii_art = build_template_art(text, symbol)
    colored_ascii_art = apply_color(ascii_art, color)
    
    # Preview the result
    if preview_ascii_art(colored_ascii_art):
        # Ensure output directory exists
        output_dir = "lab3/output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Save the ASCII art to a file
        with open(f"{output_dir}/saved_art.txt", "w") as file:
            file.write(colored_ascii_art)
        
        print(f"ASCII art saved to '{output_dir}/saved_art.txt'")

if __name__ == "__main__":
    main()
