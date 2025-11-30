# Capture content of a text file and print it to the console

template = open("Email_Draft_Compiler/templates/main_template.txt", "r")
template_content = template.read()

# Parse the placeholders from the template file and create a list

position1 = template_content.find("{")
message = template_content[position1 + 1:]
print(message)