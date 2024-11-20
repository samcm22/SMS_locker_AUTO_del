
# Data Protection with SMS and Auto Delete 🚀

This application ensures secure storage and management of personal details using an encrypted SQLite database. It includes advanced features like password-protected access, automatic database deletion after multiple incorrect password attempts, and SMS alerts for enhanced security. 

## 🔒 Features

### 1. **Password Protection**
- Requires a password to access the main window.
- Prevents unauthorized access to sensitive data.

### 2. **Data Encryption**
- Secures user data using **Fernet encryption** for added security and privacy.

### 3. **Automatic Deletion**
- Deletes the database file after **three incorrect password attempts** to prevent brute-force attacks.

### 4. **SMS Alerts**
- Sends an SMS alert to the owner's phone after **two incorrect password attempts**.

### 5. **CRUD Operations**
- **Save, View, and Clear** personal details like Name, Email, and Password.

### 6. **About Section**
- Provides an overview of the application's purpose and functionality.

---

## 🛠️ Installation

### Prerequisites
- **Python**: Version 3.6 or later.
- Required libraries:
  ```bash
  pip install tkinter cryptography twilio sqlite3
  ```bash
### Clone the Repository
- ** Download or clone the repository:**
  ```bash
  pip install tkinter cryptography twilio sqlite3
  git clone https://github.com/your-username/your-repo-name.git
  cd your-repo-name ```bash
  
## 🚀 Usage
### ** Launch the Application **
**Run the script using Python:**
                 **👉 python your_script_name.py**
Access with Password
Use the default password: **password123** (or customize it in the script).
🔐-------------------💀---------------------🔐

First Attempt:  **Displays an "Incorrect Password" message.**
Second Attempt: **Sends an SMS alert to the owner's phone.**
Third Attempt: **Deletes the database file.**

### Navigate to the main window upon successful login.
Main Window Functionalities

 **Enter personal details:**
                   
                   Name, 
                   Password, 
                   Email, 
                   Password Hint.


### About Page
Access via the Help menu for a detailed overview of the application.

## ⚙️ Configuration

**Twilio SMS Setup**
Create a Twilio account at Twilio.
#### Obtain the following:

account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_phone_number = 'your_twilio_phone_number'
your_phone_number = 'recipient_phone_number'

## Customize Password
Modify the password in the validate_password function:

####  🔑 if password == 'your_new_password':🔑  

## 🔧 Troubleshooting
Database Errors
Ensure the database file exists before attempting to view data.
The same encryption key must be used for saving and retrieving data.
Twilio SMS Issues
Verify your Twilio credentials and phone numbers.
Check for active internet connectivity.
## 📝 License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed. See the LICENSE file for details.

## 👤 Author
Sam@cm
Contact  ihacku2232004@gmail.com
Enjoy using Data Protection with SMS and Auto Delete! 🔐💬

