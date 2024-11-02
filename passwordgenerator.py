import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate a password
def generate_password():
    length = int(entry.get())
    
    # Character set for generating password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generating password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Displaying the generated password
    result_label.config(text=f"Generated Password: {password}")

# Create the main application window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")
window.configure(bg='black')  # Setting background color to black

# Title Label
title_label = tk.Label(window, text="Password Generator", font=("Arial", 16), fg="white", bg="black")
title_label.pack(pady=10)

# Label and Entry for password length
length_label = tk.Label(window, text="Enter password length:", font=("Arial", 12), fg="white", bg="black")
length_label.pack(pady=5)
entry = tk.Entry(window, width=15, font=("Arial", 12))
entry.pack(pady=5)

# Generate Button
generate_button = tk.Button(window, text="Generate Password", command=generate_password, font=("Arial", 12), bg="gray", fg="white")
generate_button.pack(pady=10)

# Label to display the generated password
result_label = tk.Label(window, text="", font=("Arial", 12), fg="green", bg="black")
result_label.pack(pady=10)

# Run the application
window.mainloop()
