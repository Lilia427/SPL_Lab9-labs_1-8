class ASCIIArtGenerator:
    """A class for generating ASCII art from text."""

    @staticmethod
    def generate_art(text, symbol="*"):
        """Generate ASCII art from the given text and symbol."""
        art = []
        for char in text:
            art.append(f"{symbol * 3} {char} {symbol * 3}")
        return "\n".join(art)

    @staticmethod
    def save_art_to_file(art, file_path):
        """Save the generated ASCII art to a file."""
        with open(file_path, 'w') as file:
            file.write(art)
