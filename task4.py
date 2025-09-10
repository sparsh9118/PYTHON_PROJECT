# Simple Contact Book Program

contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = [phone, email, address]
    print("Contact added.\n")

def view_contacts():
    if contacts:
        print("\nSaved Contacts:")
        for name, info in contacts.items():
            print(name, " | ", info[0])
        print()
    else:
        print("No contacts found.\n")

def search_contact():
    key = input("Search by name or phone: ")
    found = False
    for name, info in contacts.items():
        if key.lower() in name.lower() or key == info[0]:
            print("\nFound Contact:")
            print("Name:", name)
            print("Phone:", info[0])
            print("Email:", info[1])
            print("Address:", info[2], "\n")
            found = True
    if not found:
        print("No match found.\n")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("New phone (leave blank to keep old): ")
        email = input("New email (leave blank to keep old): ")
        address = input("New address (leave blank to keep old): ")
        
        if phone:
            contacts[name][0] = phone
        if email:
            contacts[name][1] = email
        if address:
            contacts[name][2] = address
        
        print("Contact updated.\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        contacts.pop(name)
        print("Contact deleted.\n")
    else:
        print("Contact not found.\n")

def main():
    while True:
        print("----- Contact Book -----")
