import tkinter as tk
from tkinter import ttk, messagebox

from process_user_input import process_user_input

def generate_email():
    try:
        recipient_name = entry_recipient.get()
        recipient_email = entry_recipient_email.get()
        user_login = entry_login.get()
        sender = entry_sender.get()
        env = combo_env.get()

        # Template
        email_text = process_user_input(recipient_name, recipient_email, user_login, sender)

        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, email_text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Email Draft Compiler")

# Input fields
ttk.Label(root, text="Recipient Name").pack()
entry_recipient = ttk.Entry(root)
entry_recipient.pack()

ttk.Label(root, text="Recipient email").pack()
entry_recipient_email = ttk.Entry(root)
entry_recipient_email.pack()

ttk.Label(root, text="User login").pack()
entry_login = ttk.Entry(root)
entry_login.pack()

ttk.Label(root, text="Sender name").pack()
entry_sender = ttk.Entry(root)
entry_sender.pack()

ttk.Label(root, text="Environment").pack()
combo_env = ttk.Combobox(root, values=["prod", "test", "dev"])
combo_env.pack()

ttk.Button(root, text="Generate", command=generate_email).pack(pady=10)

# Output 
text_output = tk.Text(root, height=20, width=80)
text_output.pack()

root.mainloop()