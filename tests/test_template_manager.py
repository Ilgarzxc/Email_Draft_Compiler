from prettytable import PrettyTable

spreadsheet_from_template = PrettyTable()

spreadsheet_from_template.field_names = ["environment name", "link to the environment"]
spreadsheet_from_template.add_row(["login", "password"])

print(spreadsheet_from_template)