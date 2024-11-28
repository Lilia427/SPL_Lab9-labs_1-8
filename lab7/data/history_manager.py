class HistoryManager:
    def __init__(self):
        self.history = []

    def add_entry(self, entry):
        self.history.append(entry)

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []
