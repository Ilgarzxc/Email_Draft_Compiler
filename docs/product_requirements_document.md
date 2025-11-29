## Email Draft Compiler

_When_ the user creates a new account or resets a password according to the user management process, they need to create an informational email draft with the user's login and a link to the working environment.

_Given_ the application accepts and validates the information and returns a structured email draft in a new Outlook window. Information: sender email address; receiver email address; user login; link to the environment.

_Then_ the application should open a new window in MS Outlook, allow the user to make minor edits, and send the email from the working email address.

### Non-functional requirements

- Application will not save the passwords since no interactions with passwords expected at all.
- Application will be run locally and no need to connect to any external service
- Environment: Windows + MS Outlook

### Limitations

- Required installed MS Outlook client
- Windows-only application

### MVP

- GUI with the designated fields (sender, receiver, login, link)
- Email preview
- "Create an email draft" button
- Outlook opens created draft

### Stack

- Python + pywin32 + customtkinter
- Windows
