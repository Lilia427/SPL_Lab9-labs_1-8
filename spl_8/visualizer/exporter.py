import os

class Exporter:
    def __init__(self, output_dir="visuals/charts"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def save_plot(self, filename, format="png"):
        filepath = os.path.join(self.output_dir, f"{filename}.{format}")
        try:
            import matplotlib.pyplot as plt
            plt.savefig(filepath, format=format)
            print(f"Plot successfully saved as {filepath}")
        except Exception as e:
            print(f"Error saving plot: {e}")
