# Contact Book (CRUD operations with dictionary).
import os
import json

FILENAME = "contacts.json"

"""Load contacts from json file"""
def load_contacts():
    if not os.path.exists(FILENAME):
        return {}
    with open(FILENAME, "r") as f:
        return json.load(f)

"""Save contacts to json file"""
def save_contacts(contacts):
    with open(FILENAME, "w") as f:
        json.dump(contacts, f, indent=4)
        
"""Display all contacts"""
def display_contacts(contacts):
    if not contacts:
        print("\nNo contacts found!\n")
        return
    # else
    print("\n---Contact List ---")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}\n")
    print("------------------------\n")

"""Add contact to list contacts"""
def add_contact(contacts):
    name = input("Enter name: ")
    if name in contacts:
        print("Contact already exist!\n")
        return
    #else
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts[name] = {"phone":phone, "email": email}
    save_contacts(contacts)
    print(f"Contact {name} added!\n")

"""Update contact"""
def update_contact(contacts):
    name = input("Enter name: ")
    if name not in contacts:
        print("Contact not found!\n")
        return
    #else
    phone = input("Enter new phone (leave blank to keep old): ")
    email = input("Enter email (leave blank to keep old): ")
    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    save_contacts(contacts)
    print(f"Contact {name} updated!\n")

"""Delete contact"""
def delete_contact(contacts):
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Deleted Contact {name}\n")
    else:
        print("Contact not found!\n")

"""Search contact"""
def search_contact(contacts):
    name = input("Enter the name to search: ")
    if name in contacts:
        info = contacts[name]
        print(f"Found => Name: {name}, Phone: {info['phone']}, Email: {info['email']}\n")
    else:
        print("Contact not found!\n")

def main():
    # get all contacts from contacts.json
    contacts = load_contacts()
    while True:
        print("===== Contact Book =====")
        print("1. View All Contacts")
        print("2. Add Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            display_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            search_contact(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
    
