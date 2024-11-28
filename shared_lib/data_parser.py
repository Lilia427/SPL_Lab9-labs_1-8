import json
import csv

class DataParser:
    """A class for parsing data from various formats."""

    @staticmethod
    def parse_json(json_string):
        """Parse a JSON string and return a dictionary."""
        try:
            return json.loads(json_string)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {e}")

    @staticmethod
    def parse_csv(file_path):
        """Parse a CSV file and return a list of dictionaries."""
        data = []
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        return data

    @staticmethod
    def parse_text(file_path):
        """Parse a plain text file and return its content as a string."""
        with open(file_path, 'r') as file:
            return file.read()
