from colorama import Fore, Style
from lab5.shapes import Cube, Sphere, Pyramid, Cylinder


class Renderer:
    def __init__(self, shape, color_mode="grayscale"):
        self.shape = shape
        self.color_mode = color_mode

    def render_ascii(self):
        if isinstance(self.shape, Cube):
            return self.apply_color(self.render_cube())
        elif isinstance(self.shape, Sphere):
            return self.apply_color(self.render_sphere())
        elif isinstance(self.shape, Pyramid):
            return self.apply_color(self.render_pyramid())
        elif isinstance(self.shape, Cylinder):
            return self.apply_color(self.render_cylinder())
        else:
            return "Unknown shape"

    def apply_color(self, ascii_art):
        if self.color_mode == "grayscale":
            return ascii_art
        elif self.color_mode == "color":
            colorized_art = ascii_art.replace('+', f"{Fore.RED}+{Style.RESET_ALL}") \
                                     .replace('-', f"{Fore.YELLOW}-{Style.RESET_ALL}") \
                                     .replace('|', f"{Fore.GREEN}|{Style.RESET_ALL}") \
                                     .replace('/', f"{Fore.CYAN}/{Style.RESET_ALL}") \
                                     .replace('\\', f"{Fore.CYAN}\\{Style.RESET_ALL}")
            return colorized_art
        else:
            return ascii_art

    def render_cube(self):
        return """
            +------+
           /      /|
          /      / |
         +------+  +
         |      | /
         |      |/
         +------+
        """

    def render_sphere(self):
        return """
               , - ~ ~ ~ - ,
           , '               ' ,
         ,                       ,
        ,                         ,
       ,                           ,
       ,                           ,
        ,                         ,
         ,                       ,
           ,                  , '
             ' - , _ _ _ ,  '
        """

    def render_pyramid(self):
        return """
         /\\
        /  \\
       /    \\
      /______\\
        """

    def render_cylinder(self):
        return """
           ______
         /        \\
        |          |
        |          |
        |          |
         \\________/
        """