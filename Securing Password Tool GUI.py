import tkinter as tk
from tkinter import messagebox, StringVar
import random
import string
import secrets

# Function to generate password
def generate_password(length=12, include_upper=True, include_lower=True, include_numbers=True, include_special=True):
    if length < 1:
        raise ValueError("Password length must be at least 1 character.")
    
    char_pool = ''
    if include_upper:
        char_pool += string.ascii_uppercase
    if include_lower:
        char_pool += string.ascii_lowercase
    if include_numbers:
        char_pool += string.digits
    if include_special:
        char_pool += string.punctuation
    
    if not char_pool:
        raise ValueError("At least one character type must be selected.")
    
    password = ''.join(secrets.choice(char_pool) for _ in range(length))
    return password

# Function to evaluate password strength
def evaluate_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    strength_score = sum([has_upper, has_lower, has_digit, has_special])

    if length >= 12 and strength_score == 4:
        return "Strong"
    elif length >= 8 and strength_score >= 3:
        return "Moderate"
    else:
        return "Weak"

# Function to generate random password and display in GUI
def random_password():
    length = int(password_length.get())
    include_upper = var_upper.get()
    include_lower = var_lower.get()
    include_numbers = var_numbers.get()
    include_special = var_special.get()

    try:
        password = generate_password(length, include_upper, include_lower, include_numbers, include_special)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

        strength = evaluate_password_strength(password)
        strength_label.config(text=f"Password Strength: {strength}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to secure and transform password
def secure_password():
    password = secure_password_entry.get()
    if password:
        SECURE = (('and', '&'), ('dot', '.'), ('for', '4'), ('per', '/'), ('eq', '='), ('s', '$'), ('o', '0'), ('i', '|'), ('h', '#'), ('a', '@'), ('t', '7'))
        for a, b in SECURE:
            password = password.replace(a, b)

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

        strength = evaluate_password_strength(password)
        strength_label.config(text=f"Password Strength: {strength}")
    else:
        messagebox.showwarning("Input required", "Please enter a password to secure.")

# Setting up GUI
root = tk.Tk()
root.title("Secure Password Utility Program")

# Frame for random password generation
frame_random = tk.LabelFrame(root, text="Random Password Generator")
frame_random.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

tk.Label(frame_random, text="Password Length:").grid(row=0, column=0, padx=5, pady=5)
password_length = tk.Entry(frame_random)
password_length.grid(row=0, column=1, padx=5, pady=5)
password_length.insert(0, "12")

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_special = tk.BooleanVar(value=True)

tk.Checkbutton(frame_random, text="Include Uppercase", variable=var_upper).grid(row=1, column=0, padx=5, pady=5)
tk.Checkbutton(frame_random, text="Include Lowercase", variable=var_lower).grid(row=1, column=1, padx=5, pady=5)
tk.Checkbutton(frame_random, text="Include Numbers", variable=var_numbers).grid(row=2, column=0, padx=5, pady=5)
tk.Checkbutton(frame_random, text="Include Special Characters", variable=var_special).grid(row=2, column=1, padx=5, pady=5)

tk.Button(frame_random, text="Generate Password", command=random_password).grid(row=3, columnspan=2, padx=5, pady=5)

password_entry = tk.Entry(frame_random, width=30)
password_entry.grid(row=4, columnspan=2, padx=5, pady=5)

strength_label = tk.Label(frame_random, text="Password Strength: ")
strength_label.grid(row=5, columnspan=2, padx=5, pady=5)

# Frame for secure password transformation
frame_secure = tk.LabelFrame(root, text="Secure Your Password")
frame_secure.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

tk.Label(frame_secure, text="Enter your password:").grid(row=0, column=0, padx=5, pady=5)
secure_password_entry = tk.Entry(frame_secure, width=30)
secure_password_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Button(frame_secure, text="Secure Password", command=secure_password).grid(row=1, columnspan=2, padx=5, pady=5)

root.mainloop()
