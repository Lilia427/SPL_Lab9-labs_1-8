def get_user_text():
    text = input("Enter the text you want to convert to ASCII art (default is 'HELLO'): ")
    return text if text else "HELLO"

def get_user_symbol_set():
    symbols = input("Enter a set of symbols (e.g., @#*): ").strip()
    return list(symbols) if symbols else ["#"]

def get_dimensions():
    try:
        width = input("Enter the width of the ASCII art (default is 80): ").strip()
        height = input("Enter the height of the ASCII art (default is 10): ").strip()
        
        width = int(width) if width else 80
        height = int(height) if height else 10
        
        if width <= 0 or height <= 0:
            raise ValueError
    except ValueError:
        print("Invalid dimensions. Please enter positive integers for width and height.")
        return get_dimensions()
    return width, height
