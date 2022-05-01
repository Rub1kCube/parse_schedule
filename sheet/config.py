import openpyxl


class ConfigurationSheet:

    def __init__(self, dest_filename: str):
        self.wb = openpyxl.load_workbook(filename=dest_filename, read_only=True)
        self.sheet_names = self.wb.sheetnames
