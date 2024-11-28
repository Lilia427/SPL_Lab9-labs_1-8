from lab4.data.ascii_templates import Templates
from lab4.data.ascii_templates import build_template_art


def generate_ascii_art(text, symbol, width=None, height=None):
    lines = [""] * 5
    for char in text:
        char_template = Templates.get_ascii_template(char, symbol)
        for i in range(5):
            lines[i] += char_template[i] + "  "
    ascii_art = "\n".join(lines)
    if width or height:
        ascii_art = resize_ascii_art(ascii_art, width, height)
    return ascii_art

def resize_ascii_art(ascii_art, width, height):
    lines = ascii_art.split("\n")
    if width:
        lines = [line[:width] for line in lines]
    if height and height < len(lines):
        lines = lines[:height]
    return "\n".join(lines)
