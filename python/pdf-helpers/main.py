import os
import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
from PIL import Image
from tabula.io import convert_into

# Initialize main window
window = tk.Tk()
window.title("PDF Python Helpers")
window.geometry("470x250")
window.resizable(False, False)

# Add a main frame
main_frame = tk.Frame(window, padx=10, pady=10)
main_frame.pack(expand=True, fill='both')

# Title and description
title_label = tk.Label(main_frame, text="PDF Python Helpers", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)
description_label = tk.Label(main_frame, text="Choose a function to proceed:", font=("Helvetica", 12))
description_label.pack(pady=10)


def select_file():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")], title="Select a PDF document")
        if not file_path:
            return

        file_save = filedialog.asksaveasfilename(title="Save File", defaultextension=".csv",
                                                 filetypes=[("CSV files", "*.csv")],
                                                 initialdir=os.path.dirname(file_path))
        if not file_save:
            return

        convert_into(file_path, file_save, output_format="csv", pages='all')
        messagebox.showinfo("Success", "File converted to CSV successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def select_images():
    try:
        file_paths = filedialog.askopenfilenames(filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("All files", "*.*")],
                                                 title="Select images")
        if not file_paths:
            return

        images = [Image.open(file_path) for file_path in file_paths]
        file_save = filedialog.asksaveasfilename(title="Save File", defaultextension=".pdf",
                                                 filetypes=[("PDF files", "*.pdf")],
                                                 initialdir=os.path.dirname(file_paths[0]))
        if not file_save:
            return

        images[0].save(file_save, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
        messagebox.showinfo("Success", "PDF generated successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def select_pdfs():
    try:
        file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")], title="Select PDFs to merge")
        if not file_paths:
            return

        file_save = filedialog.asksaveasfilename(title="Save file", defaultextension=".pdf",
                                                 filetypes=[("PDF files", "*.pdf")],
                                                 initialdir=os.path.dirname(file_paths[0]))
        if not file_save:
            return

        pdf_writer = PyPDF2.PdfWriter()
        for path in file_paths:
            pdf_reader = PyPDF2.PdfReader(path)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

        with open(file_save, 'wb') as out:
            pdf_writer.write(out)
        messagebox.showinfo("Success", "PDFs merged successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Create buttons and place them in a button frame
button_frame = tk.Frame(main_frame)
button_frame.pack(fill='x', pady=10)

select_button = tk.Button(button_frame, text="Convert PDF to CSV", command=select_file, width=25)
select_button.grid(row=0, column=0, padx=10, pady=5)

images_button = tk.Button(button_frame, text="Create PDF from Images", command=select_images, width=25)
images_button.grid(row=0, column=1, padx=10, pady=5)

merge_button = tk.Button(button_frame, text="Merge PDFs", command=select_pdfs, width=25)
merge_button.grid(row=1, column=0, columnspan=2, pady=5)

# Run the Tkinter event loop
window.mainloop()
