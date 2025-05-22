# PROJECT TITLE
MY PROJECT TITLE IS CONTACT MANAGEMENT SYSTEM
THE VEDIO DEMO'S URL IS : https://youtu.be/4dVEWxCXzXE
#DESCRIPTION OF THE PROGRAM:
    The Contacts Management System is a Python-based project designed to help users manage their contact information efficiently. The system provides functionality to view, add, update, and delete contacts. All contact data is stored in an SQLite database, ensuring data persistence across sessions.


## Modules and Functions used:
    **Module imports**
        colorama:
        It adds the specified color to the text which is specified in print function.
        sqlite3:
        The `sqlite3` package is a built-in Python module that provides an interface to the SQLite database. It allows for easy, efficient, and
        lightweight database management directly from Python applications. And when called with certain functions a file is created with '.db'
        and here all contacts are stored.
        validator_collection:
        This package simplifies input validation by offering ready-to-use validators for strings, numbers, dates, URLs, and more. So here to check email is given correctly or not is checked by this package.
        tabulate:
        This in Python provides a simple way to format tabular data into visually appealing tables. So in my project i used it to output the
        added contacts into the form of tables
    **Functions Used**
        setup_database()
            Purpose: Initializes the SQLite database if it doesn't exist, creating a contacts table with fields for ID, name, phone number,
            email, and address.
            Usage: Ensures database setup before any operations.
        fetch_contacts()
            Purpose: Retrieves all contacts from the contacts table in the database.
            Usage: Used to fetch existing contacts for viewing or manipulation.
        add_contact_to_db(name, phone, email, address)
            Purpose: Inserts a new contact record into the contacts table with provided details.
            Usage: Used when adding a new contact through user input.
        update_contact_in_db(id, name, phone, email, address)
            Purpose: Updates an existing contact's details in the contacts table based on the contact's ID.
            Usage: Used when modifying an existing contact's information.
        delete_contact_from_db(id)
            Purpose: Deletes a contact record from the contacts table based on the contact's ID.
            Usage: Used when removing a contact from the database.
        view_contacts()
            Purpose: Displays all contacts stored in the database in a formatted table using the tabulate library.
            Usage: Used to present the contacts data to the user in a readable format.
        add_contact()
            Purpose: Collects user input for a new contact and validates the input before adding it to the database.
            Usage: Handles user interaction to add a new contact.
        update_contact()
            Purpose: Allows the user to update details of an existing contact by ID, validating input before committing changes to the database.
            Usage: Facilitates modifying contact information based on user input.
        delete_contact()
            Purpose: Enables the user to delete a contact from the database by specifying the contact's ID.
            Usage: Handles deletion of a contact based on user input.
        main()
            Purpose: Entry point of the program; initializes the database, presents a menu for user interaction, and directs flow based on user
            imput.
            Usage: Orchestrates the execution of the contacts management system.
        These functions collectively create a contacts management system in Python.


## Files:
    project.py - This file contains the main code of my project and root of the files in the directory.
    contacts.db - This file serves as container for tstoring structured data.
    requirements,txt



#### Description:
    1. **Project Title**: Contacts Management System
    2. **Purpose**: Manage a list of contacts efficiently using a command-line interface and SQLite database backend.
    3. **Key Features**:
    - Allows viewing, adding, updating, and deleting contacts.
    - Data validation ensures input integrity (e.g., email format validation).
    - Utilizes `tabulate` for presenting contact information in a grid format.
    - `colorama` provides colored output for better user interaction.
    - Contacts are stored persistently in an SQLite database (`contacts.db`).
    4. **Functionality**:
    - **View Contacts**: Displays all stored contacts or notifies if none are available.
    - **Add Contact**: Collects and validates user input for name, phone, email, and address before adding to the database.
    - **Update Contact**: Allows modification of existing contact details based on the contact ID after validation.
    - **Delete Contact**: Removes a contact from the database after confirming its ID.
    - **Input Handling**: Handles edge cases like invalid IDs or incomplete data entries gracefully.
    5. **User Experience**: Provides a straightforward menu-driven interface for easy navigation and operation.
    6. **Error Handling**: Incorporates error messages to guide users in case of invalid inputs or operations.
    7. **Usage**: Suitable for personal or small business use cases where managing a contact list efficiently is essential.
    8. **Educational Value**: Ideal for learning database operations, input validation, and command-line interface development in Python.

This project effectively combines database management with user interaction. This will be great experiance for the user as well.
