class Printer:
    def print_page(self, text: str):
        print(f"Printing: {text}")

class ReportGenerator:
    def __init__(self, content: str):
        self.content = content

    # ReportGenerator depends on a Printer object strictly during this call
    def output_report(self, printer_device: Printer):
        printer_device.print_page(self.content)

# --- Running the code ---
# 1. Instantiate the individual tool objects independently
my_printer = Printer()
quarter_report = ReportGenerator("Q1 Academic Performance: Excellent!")

# 2. Execute the function call passing the required dependent device
quarter_report.output_report(my_printer)