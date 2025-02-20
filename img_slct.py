import tkinter as tk
from tkinter import filedialog

def select_cover_image():
    root = tk.Tk()
    root.withdraw()  # Hide root window
    root.attributes('-topmost', True)  # Bring dialog to front
    file_path = filedialog.askopenfilename(title="Select Cover Image",
                                           filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
    root.destroy()  # Close Tkinter properly
    return file_path
