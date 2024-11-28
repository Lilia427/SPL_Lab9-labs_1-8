class Settings:
    def __init__(self, decimal_places=2):
        self.decimal_places = decimal_places

    def set_decimal_places(self, places):
        if isinstance(places, int) and places >= 0:
            self.decimal_places = places
            print(f"Decimal places set to {places}.")
        else:
            print("Invalid input. Please enter a non-negative integer.")

    def round_result(self, result):
        return round(result, self.decimal_places)
