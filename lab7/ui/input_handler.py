import re


class InputHandler:
    @staticmethod
    def get_valid_integer(prompt, min_value=None, max_value=None):
        while True:
            try:
                user_input = int(input(prompt))
                if min_value is not None and user_input < min_value:
                    print(f"Please enter a value greater than or equal to {min_value}.")
                    continue
                if max_value is not None and user_input > max_value:
                    print(f"Please enter a value less than or equal to {max_value}.")
                    continue
                return user_input
            except ValueError:
                print("Invalid input. Please enter an integer.")

    @staticmethod
    def validate_email(email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_date(date):
        patterns = [
            r"^\d{4}-\d{2}-\d{2}$",  # YYYY-MM-DD
            r"^\d{2}/\d{2}/\d{4}$"   # DD/MM/YYYY
        ]
        for pattern in patterns:
            if re.match(pattern, date):
                return True
        return False

    @staticmethod
    def validate_phone(phone):
        pattern = r"^\+?[0-9]{10,15}$"
        return bool(re.match(pattern, phone))

    @staticmethod
    def extract_dates(text):
        pattern = r"\b\d{4}-\d{2}-\d{2}\b|\b\d{2}/\d{2}/\d{4}\b"
        return re.findall(pattern, text)

    @staticmethod
    def extract_phone_numbers(text):
        pattern = r"\+?[0-9]{10,15}"
        return re.findall(pattern, text)
