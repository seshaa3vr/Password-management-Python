import tkinter as tk
from tkinter import messagebox
import re

# Function to analyze password strength
def analyze_password():
    password = password_entry.get()
    strength = 0
    remarks = []

    # Check password length
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password is too short (less than 8 characters).")

    # Check if password contains both uppercase and lowercase characters
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        strength += 1
    else:
        remarks.append("Password should contain both uppercase and lowercase letters.")

    # Check if password contains numbers
    if re.search("[0-9]", password):
        strength += 1
    else:
        remarks.append("Password should contain at least one number.")

    # Check if password contains special characters
    if re.search("[@#$%^&+=!]", password):
        strength += 1
    else:
        remarks.append("Password should contain at least one special character (@#$%^&+=!).")

    # Check for common patterns or dictionary words
    if re.search(r"(password|123456|qwerty|admin|letmein)", password, re.IGNORECASE):
        remarks.append("Password contains common patterns or words that are easily guessable.")

    # Check password length for very strong passwords
    if len(password) >= 12:
        strength += 1
        remarks.append("Password is long enough to be very strong.")

    # Determine password strength level
    if strength == 5:
        strength_level = "Very Strong"
    elif strength >= 3:
        strength_level = "Strong"
    elif strength == 2:
        strength_level = "Weak"
    else:
        strength_level = "Very Weak"

    # Display result in messagebox
    result_message = f"Password Strength: {strength_level}\n"
    if remarks:
        result_message += "Suggestions to improve your password:\n"
        result_message += "\n".join(f"- {remark}" for remark in remarks)
    
    messagebox.showinfo("Password Analyzer Result", result_message)

# Main GUI Application
def create_gui():
    global password_entry

    # Create main window
    root = tk.Tk()
    root.title("Password Analyzer Tool")
    root.geometry("400x200")

    # Create Label
    instruction_label = tk.Label(root, text="Enter your password to analyze:")
    instruction_label.pack(pady=10)

    # Create Entry widget for password input
    password_entry = tk.Entry(root, show="*", width=30)
    password_entry.pack(pady=10)

    # Create Analyze Button
    analyze_button = tk.Button(root, text="Analyze Password", command=analyze_password)
    analyze_button.pack(pady=10)

    # Start the GUI loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()
