import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from PIL import Image
from tabula.io import convert_into

window = tk.Tk()

window.title("PDF Python Helpers")

window.geometry("400x100+{}+{}".format(int(window.winfo_screenwidth() / 2 - 200),
                                       int(window.winfo_screenheight() / 2 - 50)))

description_label = tk.Label(window, text="This is a sample Python program to helper in some functions")
description_label.place(relx=0.5, rely=0.2, anchor='center')


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")],
                                           title="Select document")

    file_save = filedialog.asksaveasfile(title="Save File", defaultextension=".csv",
                                         filetypes=[("CSV files", "*.csv")],
                                         initialdir=os.path.dirname(file_path))

    convert_into(file_path, file_save.name, output_format="csv", pages='all')

    messagebox.showinfo("Success", "File converted to CSV with success")


def select_images():
    file_paths = filedialog.askopenfilenames(filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("All files", "*.*")],
                                             title="Please images")

    images = [
        Image.open(file_path)
        for file_path in file_paths
    ]

    file_save = filedialog.asksaveasfile(title="Save File",
                                         defaultextension=".pdf",
                                         filetypes=[("PDF files", "*.pdf")],
                                         initialdir=os.path.dirname(file_paths[0]))

    images[0].save(file_save.name, "PDF", resolution=100.0, save_all=True, append_images=images[1:])

    messagebox.showinfo("Success", "PDF generated with success")


select_button = tk.Button(window, text="Select PDF Spreadsheet", command=select_file)
select_button.pack(side='left', anchor='center')

images_button = tk.Button(window, text="Select Images", command=select_images)
images_button.pack(side='right', anchor='center')

window.mainloop()
