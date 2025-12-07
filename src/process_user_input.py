from validation import (validate_recipient_name, validate_sender_name, validate_user_login, validate_recipient_email)
from template_manager import load_template, assemble_email

def process_user_input(recipient_name: str, 
                       recipient_email: str, 
                       user_login: str, 
                       sender_name: str) -> str:
    #Validate input
    validate_recipient_name(recipient_name)
    validate_recipient_email(recipient_email)
    validate_user_login(user_login)
    validate_sender_name(sender_name)

    #Load selected template
    template_text=load_template("template_prod_version.txt")

    #Assemble email
    return assemble_email(
        template_text,
        recipient_name=recipient_name,
        recipient_email=recipient_email,
        user_login=user_login,
        sender_name=sender_name
    )