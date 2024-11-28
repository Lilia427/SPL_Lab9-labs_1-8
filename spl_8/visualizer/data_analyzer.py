class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_column_extremes(self):
        extremes = {}
        for column in self.data.select_dtypes(include='number').columns:
            min_value = self.data[column].min()
            max_value = self.data[column].max()
            extremes[column] = {"min": min_value, "max": max_value}
        return extremes

    def get_summary_statistics(self):
        return self.data.describe()
