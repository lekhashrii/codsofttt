import tkinter as tk

def on_click(button_text):
    current_text = entry.get()
    
    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the current expression
entry = tk.Entry(root, width=20, font=('Arial', 14), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Buttons for numbers and operations
buttons = [
    '1', '2', '3', 'C',
    '4', '5', '6', '*',
    '6', '7', '8', '-',
    '0', '.', '/', '+',
    '='
]

row_val = 1
col_val = 0

for button_text in buttons:
    tk.Button(root, text=button_text, width=5, height=2,
              command=lambda b=button_text: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the GUI main loop
root.mainloop()
