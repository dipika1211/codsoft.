import tkinter as tk

# Function to update expression in the text entry box
def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(key))

# Function to evaluate the expression and display the result
def evaluate():
    try:
        result = str(eval(entry.get()))  # Evaluate the expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry box
def clear():
    entry.delete(0, tk.END)

# Main window
window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")
window.configure(bg="black")

# Entry widget for expression
entry = tk.Entry(window, width=22, font=("Arial", 24), bd=10, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Creating buttons
button_text = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

# Button style
button_bg = "gray"
button_fg = "white"
button_font = ("Arial", 18)

# Create buttons using loop
row_val = 1
col_val = 0
for text in button_text:
    if text == "=":
        button = tk.Button(window, text=text, width=5, height=2, font=button_font, bg="green", fg="white", command=evaluate)
    else:
        button = tk.Button(window, text=text, width=5, height=2, font=button_font, bg=button_bg, fg=button_fg, command=lambda t=text: press(t))
    button.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
clear_button = tk.Button(window, text="Clear", width=24, height=2, font=button_font, bg="red", fg="white", command=clear)
clear_button.grid(row=6, column=0, columnspan=4, padx=5, pady=10)

# Start the main loop
window.mainloop()
