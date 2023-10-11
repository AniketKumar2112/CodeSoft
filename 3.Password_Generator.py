# To design a password generator application using python.

import tkinter as tk
import random
import string

window_width = 450
window_height = 250

# Function to generate a random password-

def generate_password():
    try:
        password_length = int(length_entry.get())
        
        if password_length <= 0:
            result_label.config(text="Password length should be a positive number.")
        
        else:
            characters = string.ascii_letters + string.digits + string.punctuation
            generated_password = ''.join(random.choice(characters) for _ in range(password_length))
            result_label.config(text="Generated Password: " + generated_password)
            
    except ValueError:
        result_label.config(text="Please enter a valid password length (a positive integer).")

# To create the main window-

window = tk.Tk()
window.title("Password Generator")
window.geometry(f"{window_width}x{window_height}")

# To create a label for password length input-

length_label = tk.Label(window, text="Enter Password Length:", width=20, font=14)
length_label.pack(pady=10)

# To create an entry field for password length-

length_entry = tk.Entry(window, width=30, font=14)
length_entry.pack(pady=10)

# To create a button to generate the password-

generate_button = tk.Button(window, text="Generate Password", command=generate_password, width=30, font=14)
generate_button.pack(pady=20)

# To create a label to display the generated password-

result_label = tk.Label(window, text="", width=30, font=14)
result_label.pack()

# Main loop-

window.mainloop()
