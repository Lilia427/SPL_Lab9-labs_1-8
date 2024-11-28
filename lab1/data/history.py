class History:
    def __init__(self):
        self.entries = []

    def add_entry(self, num1, operator, num2, result):
        if num2 is not None:
            entry = f"{num1} {operator} {num2} = {result}"
        else:
            entry = f"{operator}{num1} = {result}"
        self.entries.append(entry)

    def show(self):
        if not self.entries:
            print("No history available.")
        else:
            print("Calculation History:")
            for entry in self.entries:
                print(entry)

    def clear(self):
        self.entries = []
        print("History cleared.")
