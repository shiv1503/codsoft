# Contact Book using Tkinter
# This program lets you add, view, search, update and delete contacts.

import tkinter as tk
from tkinter import messagebox, simpledialog

# A list to store contacts in memory (each contact = dictionary)
contacts = []

# Function to add a new contact
def add_contact():
    name = name_input.get().strip()
    phone = phone_input.get().strip()
    email = email_input.get().strip()
    address = address_input.get().strip()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and phone number are required.")
        return

    # Add contact to the list
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    # Update list display and clear input fields
    show_contacts()
    clear_inputs()
    messagebox.showinfo("Added", "Contact added successfully!")

# Function to display contacts in the listbox
def show_contacts():
    contact_listbox.delete(0, tk.END)
    for c in contacts:
             contact_listbox.insert(tk.END, f"{c['name']} - {c['phone']} - {c['email']} - {c['address']}")
# Function to clear input fields
def clear_inputs():
    name_input.delete(0, tk.END)
    phone_input.delete(0, tk.END)
    email_input.delete(0, tk.END)
    address_input.delete(0, tk.END)

# Function to search contacts by name or phone
def search_contact():
    query = simpledialog.askstring("Search", "Enter name or phone:")
    if not query:
        return
    query = query.lower()

    found = []
    for c in contacts:
        if query in c['name'].lower() or query in c['phone']:
            found.append(c)

    contact_listbox.delete(0, tk.END)
    for c in found:
        contact_listbox.insert(tk.END, f"{c['name']} - {c['phone']}")

    if not found:
        messagebox.showinfo("Result", "No contacts found.")

# Function to delete selected contact
def delete_contact():
    selected = contact_listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a contact to delete.")
        return

    index = selected[0]
    del contacts[index]
    show_contacts()
    messagebox.showinfo("Deleted", "Contact deleted successfully.")

# Function to update selected contact
def update_contact():
    selected = contact_listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a contact to update.")
        return

    index = selected[0]
    c = contacts[index]

    # Ask user for new details (pre-filled with old details)
    new_name = simpledialog.askstring("Update", "Name:", initialvalue=c['name'])
    new_phone = simpledialog.askstring("Update", "Phone:", initialvalue=c['phone'])
    new_email = simpledialog.askstring("Update", "Email:", initialvalue=c['email'])
    new_address = simpledialog.askstring("Update", "Address:", initialvalue=c['address'])

    contacts[index] = {
        "name": new_name or c['name'],
        "phone": new_phone or c['phone'],
        "email": new_email or c['email'],
        "address": new_address or c['address']
    }

    show_contacts()
    messagebox.showinfo("Updated", "Contact updated successfully!")

# ---------------- GUI Setup ----------------

root = tk.Tk()
root.title("Contact Book")
root.geometry("400x450")

# Input labels and fields
tk.Label(root, text="Name").grid(row=0, column=0, padx=5, pady=5)
name_input = tk.Entry(root)
name_input.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Phone").grid(row=1, column=0, padx=5, pady=5)
phone_input = tk.Entry(root)
phone_input.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Email").grid(row=2, column=0, padx=5, pady=5)
email_input = tk.Entry(root)
email_input.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Address").grid(row=3, column=0, padx=5, pady=5)
address_input = tk.Entry(root)
address_input.grid(row=3, column=1, padx=5, pady=5)

# Buttons for actions
tk.Button(root, text="Add Contact", command=add_contact, width=15).grid(row=4, column=0, padx=5, pady=5)
tk.Button(root, text="Search Contact", command=search_contact, width=15).grid(row=4, column=1, padx=5, pady=5)
tk.Button(root, text="Update Contact", command=update_contact, width=15).grid(row=5, column=0, padx=5, pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact, width=15).grid(row=5, column=1, padx=5, pady=5)

# Listbox to show all contacts
contact_listbox = tk.Listbox(root, width=50)
contact_listbox.grid(row=6, column=0, columnspan=2, padx=5, pady=10)

root.mainloop()
