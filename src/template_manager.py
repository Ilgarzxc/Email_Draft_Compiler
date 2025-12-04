def assemble_email(recipient_name: str, username: str, user_login: str, signature:str) -> str:
    email_text = f"""
Dear {recepient_name},

Your account in {environment_name} has been created. 

+------------------------+-------------------------------------+
| {environment_name}     | {environment_link}                  |
+------------------------+-------------------------------------+
| {username}             |  {user_login}                       |
+------------------------+-------------------------------------+

Password sent in a separate email. Please check your mailbox.

If you experience issues with your account, please contact us at ilgar.gurbanov.90@gmail.com for further assistance. 

Best regards,
{signature}
"""
    return email_text.strip()




def process_user_input(recipient_name: str, username: str, user_login: str, signature: str) -> str:

    validate_recipient_name(recipient_name)
    validate_username(username)
    validate_user_login(user_login)
    validate_signature(signature)

    return assemble_email(
        recipient_name=recipient_name,
        username=username,
        user_login=user_login,
        signature=signature
    )

