import tkinter as tk
from tkinter import messagebox
import sqlite3
import os
from twilio.rest import Client
from cryptography.fernet import Fernet


# Generate a key to encrypt and decrypt the database file
def generate_key():
    return Fernet.generate_key()


# Encrypt data
def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())


# Decrypt data
def decrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.decrypt(data).decode()


# Function to validate the password
def validate_password():
    password = password_entry.get()
    if password == 'password123':  # Change the password as needed
        main_window()
        password_window.destroy()
    else:
        global incorrect_attempts
        incorrect_attempts += 1
        if incorrect_attempts == 3:
            # Delete the database file
            delete_database()
            messagebox.showerror("Error", "Database file deleted due to three incorrect attempts.")
        elif incorrect_attempts == 2:
            # Send SMS to owner
            send_sms()
            messagebox.showerror("Error", "Incorrect password! SMS sent to owner.")
        else:
            messagebox.showerror("Error", "Incorrect password!")


# Function to create the main window
def main_window():
    global root
    root = tk.Tk()
    root.title("Personal Details Storage")

    # Labels and Entry fields
    tk.Label(root, text="Name:").grid(row=0, column=0, sticky='w')
    name_entry = tk.Entry(root, width=40)
    name_entry.grid(row=0, column=1)

    tk.Label(root, text="Password:").grid(row=1, column=0, sticky='w')
    password_entry = tk.Entry(root, show="*", width=40)
    password_entry.grid(row=1, column=1)

    tk.Label(root, text="Email:").grid(row=2, column=0, sticky='w')
    email_entry = tk.Entry(root, width=40)
    email_entry.grid(row=2, column=1)

    tk.Label(root, text="Password Hint:").grid(row=3, column=0, sticky='w')
    hint_entry = tk.Entry(root, width=40)
    hint_entry.grid(row=3, column=1)

    # Buttons
    save_button = tk.Button(root, text="Save",
                            command=lambda: save_data(name_entry.get(), password_entry.get(), email_entry.get(),
                                                      hint_entry.get()), width=20, height=2)
    save_button.grid(row=4, column=0, pady=10)

    view_button = tk.Button(root, text="View Data", command=view_data, width=20, height=2)
    view_button.grid(row=4, column=1, pady=10)

    clear_button = tk.Button(root, text="Clear Entries",
                             command=lambda: clear_entries(name_entry, password_entry, email_entry, hint_entry),
                             width=20, height=2)
    clear_button.grid(row=4, column=2, pady=10)

    root.mainloop()


# Function to save data to the encrypted database
def save_data(name, password, email, hint):
    if name == '' or password == '' or email == '' or hint == '':
        messagebox.showerror("Error", "Please fill in all fields")
    else:
        try:
            # Connect to the database
            key = generate_key()
            conn = sqlite3.connect('personal_details.db')
            c = conn.cursor()

            # Create table if not exists
            c.execute('''CREATE TABLE IF NOT EXISTS personal_details
                         (name TEXT, password TEXT, email TEXT, hint TEXT)''')

            # Insert data into the table
            encrypted_password = encrypt_data(password, key)
            c.execute("INSERT INTO personal_details VALUES (?, ?, ?, ?)", (name, encrypted_password, email, hint))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Data saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))


# Function to view data from the encrypted database
def view_data():
    try:
        # Connect to the database
        key = generate_key()  # This should be the same key used for encryption
        conn = sqlite3.connect('personal_details.db')
        c = conn.cursor()

        # Fetch all data from the table
        c.execute("SELECT * FROM personal_details")
        data = c.fetchall()

        # Decrypt and display data in messagebox
        if data:
            decrypted_data = [(row[0], decrypt_data(row[1], key), row[2], row[3]) for row in data]
            messagebox.showinfo("Personal Details", "\n".join(str(row) for row in decrypted_data))
        else:
            messagebox.showinfo("Personal Details", "No data found!")

        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Function to clear entry fields
def clear_entries(*args):
    for entry in args:
        entry.delete(0, 'end')


# Function to send SMS using Twilio
def send_sms():
    try:
        # Twilio credentials
        account_sid = 'your_account_sid'
        auth_token = 'your_auth_token'
        twilio_phone_number = 'your_twilio_phone_number'
        your_phone_number = 'recipient_phone_number'  # Replace with your phone number

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="Warning! Three incorrect password attempts on the database.",
            from_=twilio_phone_number,
            to=your_phone_number
        )
        print("SMS sent successfully! SID:", message.sid)
    except Exception as e:
        print("Error sending SMS:", e)


# Function to delete the database file
def delete_database():
    try:
        os.remove('personal_details.db')
    except FileNotFoundError:
        pass


# Initialize incorrect attempts
incorrect_attempts = 0


# Define about_page function
def about_page():
    about_text = """
    Data Protection with SMS and Auto Delete

    This application allows you to securely store personal details. 
    In case of three incorrect password attempts, the database file is automatically deleted.
    Additionally, an SMS alert is sent to the owner's phone number.

    Developed by [Your Name]
    """
    messagebox.showinfo("About", about_text)


# Create password window
password_window = tk.Tk()
password_window.title("Data Protection with SMS and Auto Delect ")

# Add image
logo_image = tk.PhotoImage(file="pasloc.png")
logo_label = tk.Label(password_window, image=logo_image)
logo_label.pack()

# Password entry
tk.Label(password_window, text="Enter Password:").pack()
password_entry = tk.Entry(password_window, show="*", width=40)
password_entry.pack()

# Submit button
submit_button = tk.Button(password_window, text="Submit", command=validate_password, width=30, height=2)
submit_button.pack()

# Create menu bar
menu_bar = tk.Menu(password_window)
password_window.config(menu=menu_bar)

# Create Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about_page)

password_window.mainloop()
