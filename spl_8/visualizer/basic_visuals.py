import matplotlib.pyplot as plt

class BasicVisuals:
    def __init__(self, data):
        self.data = data

    def line_chart(self, x_column, y_column):
        plt.figure(figsize=(10, 6))
        plt.plot(self.data[x_column], self.data[y_column], marker='o')
        plt.title(f"Line Chart: {y_column} vs {x_column}")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.grid()
        plt.show()

    def bar_chart(self, x_column, y_column):
        plt.figure(figsize=(10, 6))
        plt.bar(self.data[x_column], self.data[y_column], color='skyblue')
        plt.title(f"Bar Chart: {y_column} vs {x_column}")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.grid()
        plt.show()
