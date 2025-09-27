import cx_Freeze
import sys
import os

# Define the base for Windows
base = None
if sys.platform == 'win32':
    base = "Win32GUI"

# Paths for Tcl and Tk
os.environ['TCL_LIBRARY'] = r"C:\Program Files\Python310\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Program Files\Python310\tcl\tk8.6"

# Function to include all files and folders
def include_files_and_folders():
    include_files = [
        'ims.db',            # Database file
    ]

    # Add specific folders with Python files
    folders_to_include = ['bill', 'images']
    for folder in folders_to_include:
        for root, _, files in os.walk(folder):
            for file in files:
                full_path = os.path.join(root, file)
                include_files.append((full_path, full_path))  # Add file to the list

    # Add all Python files in the main directory
    python_files = [
        'billing.py',
        'category.py',
        'create_db.py',
        'dashboard.py',
        'email_pass.py',  # Custom email module
        'employee.py',
        'login.py',
        'product.py',
        'sales.py',
        'supplier.py'
    ]

    for py_file in python_files:
        include_files.append(py_file)

    return include_files

# Define the main executable
executables = [
    cx_Freeze.Executable(
        "login.py", base=base
    )
]

# Setup script
cx_Freeze.setup(
    name="IMS",
    version="1.00",
    description="Inventory Management System\nDeveloped By HAMDAN MALIK",
    author="HAMDAN MALIK",
    options={
        "build_exe": {
            "packages": [
                "tkinter", 
                "os", 
                "sys", 
                "sqlite3",  # Include sqlite3 for database operations
                "time",     # Include time for time-related functions
                "PIL",      # Include PIL (Pillow) for image processing
                "smtplib",  # Include smtplib for email functionality
                "tempfile", # Include tempfile for temporary file management
                "inflect",  # Include inflect for number-to-words conversion
            ],
            "include_files": include_files_and_folders(),  # Include files/folders
        }
    },
    executables=executables
)
