import pandas as pd

class CSVLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def load_data(self):
        try:
            self.data = pd.read_csv(self.filepath)
            print(f"Data successfully loaded from {self.filepath}")
            return self.data
        except Exception as e:
            print(f"Error loading CSV file: {e}")
            return None
