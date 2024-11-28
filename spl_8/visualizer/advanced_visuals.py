import matplotlib.pyplot as plt

class AdvancedVisuals:
    def __init__(self, data):
        self.data = data

    def scatter_plot(self, x_column, y_column):
        plt.figure(figsize=(10, 6))
        plt.scatter(self.data[x_column], self.data[y_column], color='red', alpha=0.7)
        plt.title(f"Scatter Plot: {y_column} vs {x_column}")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.grid()
        plt.show()

    def histogram(self, column, bins=10):
        plt.figure(figsize=(10, 6))
        plt.hist(self.data[column], bins=bins, color='green', alpha=0.7)
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.grid()
        plt.show()
