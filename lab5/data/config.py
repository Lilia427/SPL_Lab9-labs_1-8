from colorama import Fore, Style

class ASCIIConverter:
    def __init__(self, color=False):
        self.color = color

    def convert_to_ascii(self, depth_map):
        ascii_art = ""
        for row in depth_map:
            for depth in row:
                if depth < 0.3:
                    ascii_art += self.get_symbol('.', depth)
                elif depth < 0.6:
                    ascii_art += self.get_symbol('*', depth)
                else:
                    ascii_art += self.get_symbol('#', depth)
            ascii_art += '\n'
        return ascii_art

    def get_symbol(self, symbol, depth):
        if self.color:
            return Fore.LIGHTWHITE_EX + symbol if depth < 0.6 else Fore.LIGHTBLACK_EX + symbol + Style.RESET_ALL
        return symbol