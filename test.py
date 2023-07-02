import tkinter as tk
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_label.config(text="Selected File: " + file_path)
    else:
        file_label.config(text="No file selected")

# Create the main window
window = tk.Tk()
window.title("File Selection")

# Create a button to browse for a file
browse_button = tk.Button(window, text="Browse", command=browse_file)
browse_button.pack(pady=10)

# Create a label to display the selected file path
file_label = tk.Label(window, text="No file selected")
file_label.pack()

# Start the main GUI event loop
window.mainloop()

