import tkinter as tk
from tkinter import messagebox

# Dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()
    
    if name and phone:
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
        update_contact_list()
    else:
        messagebox.showwarning("Warning", "Name and Phone are required fields.")

# Function to clear entry fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# Function to view contact list
def view_contact_list():
    listbox_contacts.delete(0, tk.END)
    for name, details in contacts.items():
        listbox_contacts.insert(tk.END, f"{name}: {details['Phone']}")

# Function to search for a contact
def search_contact():
    search_term = entry_search.get()
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term == details['Phone']:
            messagebox.showinfo("Search Result", f"Name: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}")
            return
    messagebox.showwarning("Not Found", "Contact not found.")

# Function to update contact details
def update_contact():
    name = entry_name.get()
    if name in contacts:
        contacts[name] = {
            'Phone': entry_phone.get(),
            'Email': entry_email.get(),
            'Address': entry_address.get()
        }
        messagebox.showinfo("Success", "Contact updated successfully!")
        clear_entries()
        update_contact_list()
    else:
        messagebox.showwarning("Warning", "Contact not found.")

# Function to delete a contact
def delete_contact():
    name = entry_name.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", "Contact deleted successfully!")
        clear_entries()
        update_contact_list()
    else:
        messagebox.showwarning("Warning", "Contact not found.")

# Function to update the contact list display
def update_contact_list():
    listbox_contacts.delete(0, tk.END)
    for name, details in contacts.items():
        listbox_contacts.insert(tk.END, f"{name}: {details['Phone']}")

# Main application window
root = tk.Tk()
root.title("Contact Management System")
root.geometry("500x600")
root.configure(bg="black")

# Style
style_font = ("Arial", 12)
label_fg = "orange"
button_bg = "orange"
button_fg = "black"

# Labels and Entries
tk.Label(root, text="Name:", font=style_font, fg=label_fg, bg="black").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root, font=style_font)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:", font=style_font, fg=label_fg, bg="black").grid(row=1, column=0, padx=10, pady=5)
entry_phone = tk.Entry(root, font=style_font)
entry_phone.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:", font=style_font, fg=label_fg, bg="black").grid(row=2, column=0, padx=10, pady=5)
entry_email = tk.Entry(root, font=style_font)
entry_email.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address:", font=style_font, fg=label_fg, bg="black").grid(row=3, column=0, padx=10, pady=5)
entry_address = tk.Entry(root, font=style_font)
entry_address.grid(row=3, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Add Contact", command=add_contact, bg=button_bg, fg=button_fg, font=style_font).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Update Contact", command=update_contact, bg=button_bg, fg=button_fg, font=style_font).grid(row=4, column=1, padx=10, pady=10)
tk.Button(root, text="Delete Contact", command=delete_contact, bg=button_bg, fg=button_fg, font=style_font).grid(row=5, column=0, padx=10, pady=10)
tk.Button(root, text="View Contact List", command=view_contact_list, bg=button_bg, fg=button_fg, font=style_font).grid(row=5, column=1, padx=10, pady=10)

# Search
tk.Label(root, text="Search:", font=style_font, fg=label_fg, bg="black").grid(row=6, column=0, padx=10, pady=5)
entry_search = tk.Entry(root, font=style_font)
entry_search.grid(row=6, column=1, padx=10, pady=5)

tk.Button(root, text="Search Contact", command=search_contact, bg=button_bg, fg=button_fg, font=style_font).grid(row=7, column=0, columnspan=2, pady=10)

# Contact List
listbox_contacts = tk.Listbox(root, font=style_font, bg="black", fg="orange", width=40, height=10)
listbox_contacts.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
