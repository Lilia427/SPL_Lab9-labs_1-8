def apply_color(ascii_art, color_choice):
    if color_choice == "gray":
        return grayscale_ascii(ascii_art)
    else:
        return ascii_art

def grayscale_ascii(ascii_art):
    shades = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]
    grayscale_art = []

    for line in ascii_art.split("\n"):
        shaded_line = ''.join(shades[min(len(shades) - 1, ord(char) % len(shades))] if char.strip() else ' ' for char in line)
        grayscale_art.append(shaded_line)

    return "\n".join(grayscale_art)
