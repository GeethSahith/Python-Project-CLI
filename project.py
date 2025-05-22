from tabulate import tabulate
from colorama import Fore, init
import sqlite3
import validator_collection as vc

init(autoreset=True)


def setup_database():
    conn = sqlite3.connect("contacts.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS contacts
                 (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT, address TEXT)"""
    )
    conn.commit()
    conn.close()


def fetch_contacts():
    conn = sqlite3.connect("contacts.db")
    c = conn.cursor()
    c.execute("SELECT * FROM contacts")
    contacts = c.fetchall()
    conn.close()
    return contacts


def add_contact_to_db(name, phone, email, address):
    conn = sqlite3.connect("contacts.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
        (name, phone, email, address),
    )
    conn.commit()
    conn.close()


def update_contact_in_db(id, name, phone, email, address):
    conn = sqlite3.connect("contacts.db")
    c = conn.cursor()
    c.execute(
        "UPDATE contacts SET name = ?, phone = ?, email = ?, address = ? WHERE id = ?",
        (name, phone, email, address, id),
    )
    conn.commit()
    conn.close()


def delete_contact_from_db(id):
    conn = sqlite3.connect("contacts.db")
    c = conn.cursor()
    c.execute("DELETE FROM contacts WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def view_contacts():
    contacts = fetch_contacts()
    if not contacts:
        print(Fore.RED + "No contacts available" + Fore.RESET)
    else:
        table = [
            [contact[0], contact[1], contact[2], contact[3], contact[4]]
            for contact in contacts
        ]
        headers = ["ID", "Name", "Phone", "Email", "Address"]
        print(tabulate(table, headers, tablefmt="grid"))


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter Mobile Number: ").strip()
    email = input("Enter Email Address: ").strip()
    address = input("Enter Address: ").strip()
    if name and phone and vc.checkers.is_email(email) and address:
        add_contact_to_db(name, phone, email, address)
        print(Fore.GREEN + "Contact added." + Fore.RESET)
    else:
        print(Fore.RED + "Enter all the fields correctly." + Fore.RESET)


def update_contact():
    view_contacts()
    try:
        index = int(input("Enter the ID of the contact to update: ").strip())
        contacts = fetch_contacts()
        contact_ids = [contact[0] for contact in contacts]
        if index in contact_ids:
            name = input("Enter new name: ").strip()
            phone = input("Enter new phone number: ").strip()
            email = input("Enter new email: ").strip()
            address = input("Enter new address: ").strip()
            if name and phone and vc.checkers.is_email(email) and address:
                update_contact_in_db(index, name, phone, email, address)
                print(Fore.GREEN + "Contact updated." + Fore.RESET)
            else:
                print(
                    Fore.RED
                    + "Please reverify the entered details(Check Typos, mistakes etc...)."
                    + Fore.RESET
                )
        else:
            print(Fore.RED + "Invalid contact ID." + Fore.RESET)
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a valid ID." + Fore.RESET)


def delete_contact():
    view_contacts()
    try:
        id = int(input("Enter the ID of the contact to delete: ").strip())
        contacts = fetch_contacts()
        contact_ids = [contact[0] for contact in contacts]
        if id in contact_ids:
            delete_contact_from_db(id)
            print(Fore.RED + "Contact deleted." + Fore.RESET)
        else:
            print(Fore.RED + "Invalid contact ID." + Fore.RESET)
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a valid ID." + Fore.RESET)


def main():
    setup_database()
    while True:
        print("\nContacts Management System")
        print("Enter character as specified below")
        print("V - View Contacts")
        print("A - Add Contact")
        print("U - Update Contact")
        print("D - Delete Contact")
        print("E - Exit")
        choice = input("Enter your choice: ").upper().strip()

        match choice:
            case "V":
                view_contacts()
            case "A":
                add_contact()
            case "U":
                update_contact()
            case "D":
                delete_contact()
            case "E":
                print("Exiting the program")
                break
            case _:
                print(
                    Fore.RED
                    + "Invalid choice. Please make your choice from the options above."
                    + Fore.RESET
                )


if __name__ == "__main__":
    main()
