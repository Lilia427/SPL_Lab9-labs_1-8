import os
from shared_lib.logger import Logger


class LabRunner:
    """Facade class to manage and execute laboratory projects."""

    def __init__(self):
        """Initialize the LabRunner with available labs."""
        self.logger = Logger()
        self.labs = {
            "1": self.run_lab1,
            "2": self.run_lab2,
            "3": self.run_lab3,
            "4": self.run_lab4,
            "5": self.run_lab5,
            "6": self.run_lab6,
            "7": self.run_lab7,
            "8": self.run_lab8,
        }

    def display_menu(self):
        """Display the main menu."""
        print("\n===== Laboratory Project Runner =====")
        for key, value in self.labs.items():
            print(f"{key}. Run Lab {key}")
        print("0. Exit")
        print("=====================================")

    def run_lab1(self):
        """Run Lab 1."""
        self.logger.info("Running Lab 1")
        os.system("python3 lab1/ui/main.py")

    def run_lab2(self):
        """Run Lab 2."""
        self.logger.info("Running Lab 2")
        os.system("python3 lab2/ui/interface.py")

    def run_lab3(self):
        """Run Lab 3."""
        self.logger.info("Running Lab 3")
        os.system("python3 lab3/ui/interface.py")

    def run_lab4(self):
        """Run Lab 4."""
        self.logger.info("Running Lab 4")
        os.system("python3 lab4/ui/interface.py")

    def run_lab5(self):
        """Run Lab 5."""
        self.logger.info("Running Lab 5")
        os.system("python3 lab5/ui/main.py")

    def run_lab6(self):
        """Run Lab 6."""
        self.logger.info("Running Lab 6")
        os.system("python3 lab6/main.py")

    def run_lab7(self):
        """Run Lab 7."""
        self.logger.info("Running Lab 7")
        os.system("python3 lab7/main.py")

    def run_lab8(self):
        """Run Lab 8."""
        self.logger.info("Running Lab 8")
        os.system("python3 lab8/main.py")

    def execute(self):
        """Main loop to display the menu and execute labs."""
        while True:
            self.display_menu()
            choice = input("Select a lab to run (0 to exit): ").strip()
            if choice == "0":
                print("Exiting Lab Runner. Goodbye!")
                self.logger.info("Exited Lab Runner")
                break
            elif choice in self.labs:
                try:
                    self.labs[choice]()
                except Exception as e:
                    self.logger.error(f"Error running Lab {choice}: {e}")
            else:
                print("Invalid choice. Please try again.")
                self.logger.warning(f"Invalid choice entered: {choice}")


if __name__ == "__main__":
    runner = LabRunner()
    runner.execute()
