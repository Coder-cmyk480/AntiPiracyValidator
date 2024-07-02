import tkinter as tk
from tkinter import messagebox

# Set your desired valid serial number
VALID_SERIAL = "1234-5678-9012"  # Replace with your own serial number

# Validate the entered serial number
def validate_serial():
    entered_serial = entry.get()
    if entered_serial == VALID_SERIAL:
        messagebox.showinfo("Success", "Serial number is valid!")
    else:
        messagebox.showerror("Error", "You have an illegal copy of ProHome. Please shut down the program.")

# Create the GUI
root = tk.Tk()
root.title("Anti-Piracy Screen")

label = tk.Label(root, text="Enter Serial Number:")
label.pack()

entry = tk.Entry(root)
entry.pack()

validate_button = tk.Button(root, text="Validate", command=validate_serial)
validate_button.pack()

root.mainloop()
