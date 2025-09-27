# POS-SYSTEM

## Overview

This project provides a basic Point of Sale (POS) system implemented in Python. It's designed to manage inventory, process sales, generate bills, and provide a user interface for employees.

## Key Features & Benefits

*   **Inventory Management:** Track product quantities and details.
*   **Sales Processing:** Create and manage customer bills.
*   **User Authentication:** Secure access for employees.
*   **Category Management:** Organize products into categories.
*   **Reporting (Potential):** Sales and inventory reports can be implemented (future feature).
*   **Database Support:** Uses SQLite for data storage.

## Prerequisites & Dependencies

*   **Python 3.x:**  The project is built using Python.
*   **Tkinter:**  For creating the graphical user interface.
*   **PIL (Pillow):**  For image handling. `pip install Pillow`
*   **ttkbootstrap:** for styled widgets. `pip install ttkbootstrap`
*   **sqlite3:**  For database interactions (usually included with Python).
*   **cx_Freeze:** For converting the project to an executable (optional). `pip install cx_Freeze`
*   **inflect:**  To convert numbers to ordinal strings (e.g., 1st, 2nd, 3rd). `pip install inflect`

## Installation & Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/malikhamdan00/POS-SYSTEM.git
    cd POS-SYSTEM
    ```

2.  **Install Dependencies:**
    ```bash
    pip install Pillow ttkbootstrap inflect
    ```

3.  **Run the Application:**
    ```bash
    python Exe.py  # Or directly run dashboard.py for initial setup
    ```
    Or if running dashboard.py directly:
    ```bash
    python dashboard.py
    ```

4.  **Database Creation (if needed):**

    The `create_db.py` script creates the initial database. It's likely already created, but if not:

    ```bash
    python bill/create_db.py
    ```

## Usage Examples

The application provides a GUI for managing various aspects of the POS system.

*   **Employee Management:** Add, update, and delete employee records.  Access this functionality via menu options within the main application after logging in.
*   **Supplier Management:**  Manage supplier information.
*   **Category Management:** Create and manage product categories.
*   **Product Management:** Add, update, and delete product details, including prices, quantities, and categories.
*   **Billing:**  Process sales and generate bills.  This is the core POS functionality.

## Configuration Options

*   **Database Location:** The database is stored in `ims.db`. This path can be modified in the relevant Python files (e.g., `bill/create_db.py`, `bill/billing.py`, etc.).
*   **Email Password:** The `email_pass.py` file (likely) contains the email password used for sending email.  **Warning:** Store such sensitive information securely. Avoid committing passwords directly to the repository. Consider using environment variables or a secure configuration management system.

## Project Structure

```
POS-SYSTEM/
├── Exe.py            # Script to create executable
└── bill/             # Main application logic
    ├── 21183532.txt  # Example bill files
    ├── 25314743.txt  # Example bill files
    ├── ...           # More example bill files
    ├── billing.py    # Billing module
    ├── category.py   # Category management module
    ├── create_db.py  # Database creation script
    ├── dashboard.py  # Main dashboard/entry point
    ├── email_pass.py # Email password (WARNING: secure this)
    ├── employee.py   # Employee management module
    └── images/       # Image assets
        ├── bg.png      # Background image
        ├── cat.jpg     # Category image
        ├── cat2.jpg    # Category image
        └── category.jpg# Category image
```

## Contributing Guidelines

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with clear, descriptive commit messages.
4.  Submit a pull request.

## License Information

License not specified.  Copyright remains with the owner (malikhamdan00) unless otherwise specified.
