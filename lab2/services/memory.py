class Memory:
    def __init__(self):
        self.memory = None

    def store(self, value):
        self.memory = value
        print(f"Value {value} stored in memory.")

    def retrieve(self):
        if self.memory is not None:
            print(f"Memory: {self.memory}")
            return self.memory
        else:
            print("No value stored in memory.")
            return None

    def clear(self):
        self.memory = None
        print("Memory cleared.")
