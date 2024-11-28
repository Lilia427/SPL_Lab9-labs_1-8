import matplotlib.pyplot as plt

class MultiSubplots:
    def __init__(self, data):
        self.data = data

    def multiple_charts(self, x_column, y_columns):
        fig, axes = plt.subplots(len(y_columns), 1, figsize=(10, 6 * len(y_columns)))
        for i, y_column in enumerate(y_columns):
            axes[i].plot(self.data[x_column], self.data[y_column], marker='o')
            axes[i].set_title(f"{y_column} vs {x_column}")
            axes[i].set_xlabel(x_column)
            axes[i].set_ylabel(y_column)
            axes[i].grid()
        plt.tight_layout()
        plt.show()
