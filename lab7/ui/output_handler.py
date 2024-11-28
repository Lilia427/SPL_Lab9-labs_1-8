from prettytable import PrettyTable
from colorama import Fore, Style
from lab7.data.config import DEFAULT_TITLE_COLOR, DEFAULT_MESSAGE_COLOR



class OutputHandler:
    title_color = DEFAULT_TITLE_COLOR
    message_color = DEFAULT_MESSAGE_COLOR

    @staticmethod
    def display_table(data, headers, title=None):
        table = PrettyTable()
        table.field_names = headers
        for row in data:
            table.add_row(row)
        if title:
            print(OutputHandler.title_color + f"\n{title}" + Style.RESET_ALL)
        print(table)

    @staticmethod
    def display_message(message, color=None):
        color = color or OutputHandler.message_color
        print(color + message + Style.RESET_ALL)

    @staticmethod
    def set_title_color(color_code):
        OutputHandler.title_color = color_code
        print(Fore.YELLOW + "Title color updated!" + Style.RESET_ALL)

    @staticmethod
    def set_message_color(color_code):
        OutputHandler.message_color = color_code
        print(Fore.YELLOW + "Message color updated!" + Style.RESET_ALL)
