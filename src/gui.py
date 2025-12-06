import tkinter as tk
from tkinter import ttk, messagebox

from process_user_input import process_user_input

def generate_email():
    try:
        recipient = entry_recipient.get()
        username = entry_username.get()
        user_login = entry_login.get()
        sender = entry_sender.get()
        env = combo_env.get()

        # Template
        email_text = process_user_input(recipient, username, user_login, sender)

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