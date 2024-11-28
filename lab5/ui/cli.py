from shapes import Cube, Sphere, Pyramid, Cylinder
from renderer import Renderer

class CLI:
    def __init__(self):
        self.shapes = {
            "cube": Cube,
            "sphere": Sphere,
            "pyramid": Pyramid,
            "cylinder": Cylinder
        }

    def display_menu(self):
        print("3D ASCII Art Generator")
        print("Choose a shape:")
        for idx, shape in enumerate(self.shapes, start=1):
            print(f"{idx}. {shape.capitalize()}")

    def get_shape_choice(self):
        self.display_menu()
        choice = input("Enter the number of the shape you want to draw (default is Cube): ")
        shape_keys = list(self.shapes.keys())
        if choice.isdigit() and 1 <= int(choice) <= len(shape_keys):
            return shape_keys[int(choice) - 1]
        else:
            print("Invalid choice, defaulting to Cube.")
            return "cube"

    def get_color_mode(self):
        color_choice = input("Choose color mode - grayscale (g) or color (c) (default is grayscale): ").lower()
        return "color" if color_choice == 'c' else "grayscale"

    def start(self):
        shape_choice = self.get_shape_choice()
        color_mode = self.get_color_mode()
        shape_class = self.shapes[shape_choice]
        shape = shape_class()
        renderer = Renderer(shape, color_mode=color_mode)
        ascii_art = renderer.render_ascii()
        print("Generated ASCII Art:")
        print(ascii_art)
        return ascii_art