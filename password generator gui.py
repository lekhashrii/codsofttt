import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.length_label = tk.Label(master, text="Password Length:")
        self.length_label.grid(row=0, column=0, pady=10)

        self.length_entry = tk.Entry(master)
        self.length_entry.grid(row=0, column=1, pady=10)

        self.complexity_label = tk.Label(master, text="Password Complexity:")
        self.complexity_label.grid(row=1, column=0, pady=10)

        self.complexity_var = tk.StringVar()
        self.complexity_var.set("Easy")
        self.complexity_menu = tk.OptionMenu(master, self.complexity_var, "Easy", "Medium", "Hard")
        self.complexity_menu.grid(row=1, column=1, pady=10)

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.display_button = tk.Button(master, text="Display Password", command=self.display_password)
        self.display_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(master, textvariable=self.password_var, state='readonly')
        self.password_entry.grid(row=4, column=0, columnspan=2, pady=10)

        self.edit_button = tk.Button(master, text="Edit Password", command=self.edit_password)
        self.edit_button.grid(row=5, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            complexity = self.complexity_var.get()
            password = self.generate_password_helper(length, complexity)
            self.password_var.set(password)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid password length.")

    def generate_password_helper(self, length, complexity):
        if complexity == "Easy":
            characters = string.ascii_letters + string.digits
        elif complexity == "Medium":
            characters = string.ascii_letters + string.digits + string.punctuation
        elif complexity == "Hard":
            characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_lowercase + string.ascii_uppercase
        else:
            characters = string.ascii_letters + string.digits

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def display_password(self):
        password = self.password_var.get()
        if password:
            messagebox.showinfo("Password", f"Generated Password: {password}")
        else:
            messagebox.showwarning("Warning", "Please generate a password first.")

    def edit_password(self):
        self.password_entry.config(state='normal')

# Main application loop
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
