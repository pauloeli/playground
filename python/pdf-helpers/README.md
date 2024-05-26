# PDF Python Helpers

PDF Python Helpers is a Python-based application that provides a simple and intuitive graphical user interface (GUI) for
performing various operations on PDF files. The application is built using the Tkinter library for the GUI and uses
several other libraries for PDF manipulation.

## Features

The application provides the following features:

1. **Convert PDF to CSV**: This feature allows you to select a PDF file and convert it into a CSV file. The conversion
   is done using the `tabula-py` library.

2. **Create PDF from Images**: This feature allows you to select one or more image files (JPEG, PNG) and convert them
   into a single PDF file. The conversion is done using the `PIL` library.

3. **Merge PDFs**: This feature allows you to select multiple PDF files and merge them into a single PDF file. The
   merging is done using the `PyPDF2` library.

## Installation

To install the required dependencies for this project, navigate to the project directory and run the following command:

```bash
pip install -r requirements.txt
```

## Build Executable

You can build an executable for the script using `pyinstaller`. First, install `pyinstaller`:

```bash
pip install pyinstaller
```

Then, build the executable:

```bash
pyinstaller --onefile main.py
```

## Usage

To use the application, simply run the `main.py` script or the built executable. The application window will open, and
you can choose the function you want to proceed with.

## License

This project is open-source and available under the MIT License.

