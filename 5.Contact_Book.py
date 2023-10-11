# Program to create a Phone Book.

import tkinter as tk
from tkinter import messagebox

book_width = 600
book_hieght = 700

# Function to add a new contact-

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        update_contact_list()
        clear_fields()
    else:
        messagebox.showerror("Error", "Name is required.")

# Function to update contact details-

def update_contact():
    selected_index = name_listbox.curselection()
    if selected_index:
        selected_index = int(selected_index[0])  # Get the first selected index
        selected_name = name_listbox.get(selected_index)
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        # To extract the name from the selected item in the Listbox-
        
        name, _ = selected_name.split(" - ")

        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        update_contact_list()
        clear_fields()
    else:
        messagebox.showerror("Error", "Select a contact to update.")

# Function to delete a contact-

def delete_contact():
    selected_index = name_listbox.curselection()
    if selected_index:
        selected_index = int(selected_index[0])  # Get the first selected index
        selected_name = name_listbox.get(selected_index)

        # To extract the name from the selected item in the Listbox-
        
        name, _ = selected_name.split(" - ")

        del contacts[name]
        update_contact_list()
        clear_fields()
    else:
        messagebox.showerror("Error", "Select a contact to delete.")

# Function to search for a contact-

def search_contact():
    search_term = search_entry.get().lower()
    search_results = []
    for name, contact in contacts.items():
        if search_term in name.lower() or search_term in contact["Phone"]:
            search_results.append(f"{name} - {contact['Phone']}")
    update_contact_list(search_results)

# Function to clear input fields-

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Function to update the contact list-

def update_contact_list(contact_list=None):
    name_listbox.delete(0, tk.END)
    if contact_list:
        for item in contact_list:
            name_listbox.insert(tk.END, item)
    else:
        for name, contact in contacts.items():
            name_listbox.insert(tk.END, f"{name} - {contact['Phone']}")

# To create the main window-

book = tk.Tk()
book.title("Contact Book")
book.geometry(f"{book_width}x{book_hieght}")

# Create a dictionary to store contacts-

contacts = {}

# Create labels and input fields for contact details-

# For name-

name_label = tk.Label(book, text="Name:", width=20, font=0)
name_label.grid(row=0, column=0, padx=10, pady=5)

name_entry = tk.Entry(book, width=20, font=0)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# For phone number-

phone_label = tk.Label(book, text="Phone:", width=20, font=0)
phone_label.grid(row=1, column=0, padx=10, pady=5)

phone_entry = tk.Entry(book, width=20, font=0)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

# For email id-

email_label = tk.Label(book, text="Email:", width=20, font=0)
email_label.grid(row=2, column=0, padx=10, pady=5)

email_entry = tk.Entry(book, width=20, font=0)
email_entry.grid(row=2, column=1, padx=10, pady=5)

# For address-

address_label = tk.Label(book, text="Address:", width=20, font=0)
address_label.grid(row=3, column=0, padx=10, pady=5)

address_entry = tk.Entry(book, width=20, font=0)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Create buttons for adding, updating, and deleting contacts-

add_button = tk.Button(book, text="Add Contact", command=add_contact, width=20, font=0)
add_button.grid(row=4, column=0, columnspan=2, pady=10)

update_button = tk.Button(book, text="Update Contact", command=update_contact, width=20, font=0)
update_button.grid(row=5, column=0, columnspan=2, pady=5)

delete_button = tk.Button(book, text="Delete Contact", command=delete_contact, width=20, font=0)
delete_button.grid(row=6, column=0, columnspan=2, pady=5)

# To create labels and input fields for searching contacts-

search_label = tk.Label(book, text="Search Contacts:", width=20, font=0)
search_label.grid(row=7, column=0, padx=10, pady=5)

search_entry = tk.Entry(book, width=20, font=0)
search_entry.grid(row=7, column=1, padx=10, pady=5)

search_button = tk.Button(book, text="Search", command=search_contact, width=20, font=0)
search_button.grid(row=8, column=0, columnspan=2, pady=5)

# To create a listbox to display contact names and phone numbers-

name_listbox = tk.Listbox(book, selectmode=tk.SINGLE, width=50, font=0)
name_listbox.grid(row=9, column=0, columnspan=2, padx=20, pady=5)

# To initialize the contact list-

update_contact_list()

# Main loop-

book.mainloop()
