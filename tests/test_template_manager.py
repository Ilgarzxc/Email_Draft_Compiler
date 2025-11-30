# importing PrettyTable for future use
from prettytable import PrettyTable 

''' 
Required placeholders in the template:
- Sender email address (required validation: if no spaces and "@" sign present). Variable name: my_mailbox
- Receiver email address (required validation: if no spaces and "@" sign present). Variable name: recepient_email
- Receiver first name (no digits allowed, first letter capitalized). Variable name: recepient_name
- User login (validation: at least 5 characters, no spaces). Variable name: user_login
- Environment name (from the environments_placeholders dictionary). Variable name: environment_name
- Link to the environment (from the environments_placeholders dictionary). Variable name: environment_link
- Signature - predefined text block (no validation). Variable name: signature

All fields must be filled before sending the email and mandatory.
'''

spreadsheet_from_template = PrettyTable()

spreadsheet_from_template.field_names = ["environment name", "link to the environment"]
spreadsheet_from_template.add_row(["login", "password"])

print(spreadsheet_from_template)

# Environment and links dictionary
environments_placeholders = {
    "subscription module": "http://dev.example.com",
    "aci prod": "http://staging.example.com",
    "aci test": "http://prod.example.com"
}

# Email template

'''Dear {recepient_name},

Your account has been created. 

Password sent in a separate email. Please check your mailbox.

If you experience issues with your account, please contact us at {mailbox} for further assistance. 

Best regards,
{signature}'''