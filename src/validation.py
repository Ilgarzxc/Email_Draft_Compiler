import re

#Compile regex validation for recipient name
recipient_name_regex = re.compile(r"^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžæÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+$")
username_regex = re.compile(r"^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžæÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð@._-]+$")

'''
Validation of recipient name.
Will get string value from GUI and check validity of recipient name.
Expected conditions:
    - letters, spaces, international symbols, some syntax signs
    regex should look similar to 
    ^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžæÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+$
    - No double spaces
    - No spaces before and after the input
    - Lenght (2 to n)
    - No digits
'''

#Set function for recipient_name validation

def validate_recipient_name(recipient_name: str):
    if not recipient_name.strip():
        raise ValueError("Empty recipient name or excessive spaces")
    if len(recipient_name) < 2:
        raise ValueError("Recipient name is too short")
    if "  " in recipient_name:
        raise ValueError("You have double space in recipient name")
    if recipient_name.isnumeric():
        raise ValueError("Recipient name should not be numeric")
    if not recipient_name_regex.match(recipient_name):
        raise ValueError("Recipient name contains invalid character")
    else:
        return recipient_name
    
'''
Validation of username.
General rule is similar to the recipient name checkup, but username can be equal to the user's email address.
Therefore minor changes can be seen there
'''
    
# Set function for username validation
def validate_username(username: str):
    if not username.strip():
        raise ValueError("Empty username or excessive spaces")
    if len(username) < 2:
        raise ValueError("Username is too short")
    if username.isnumeric():
        raise ValueError("Username should not be numeric")
    if not username_regex.match(username):
        raise ValueError("Username contains invalid character")
    else:
        return username