class InputValidator:
    """A class for validating user input."""

    @staticmethod
    def validate_integer(input_value, min_value=None, max_value=None):
        """Validate if the input is an integer within a specified range."""
        try:
            value = int(input_value)
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                raise ValueError(f"Value must be between {min_value} and {max_value}.")
            return value
        except ValueError as e:
            raise ValueError(f"Invalid integer input: {e}")

    @staticmethod
    def validate_float(input_value, min_value=None, max_value=None):
        """Validate if the input is a float within a specified range."""
        try:
            value = float(input_value)
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                raise ValueError(f"Value must be between {min_value} and {max_value}.")
            return value
        except ValueError as e:
            raise ValueError(f"Invalid float input: {e}")
