# Contact Book Program

contacts = {}

def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()
    
    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print(f"\n✅ Contact '{name}' added successfully!\n")

def view_contacts():
    if not contacts:
        print("\n📂 No contacts found!\n")
    else:
        print("\n📒 Contact List:")
        for name, details in contacts.items():
            print(f"- {name} | {details['Phone']}")
        print()

def search_contact():
    search = input("Enter Name or Phone Number to search: ").strip()
    found = False
    for name, details in contacts.items():
        if search.lower() in name.lower() or search == details['Phone']:
            print(f"\n🔎 Found Contact:\nName: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}\n")
            found = True
    if not found:
        print("\n❌ Contact not found!\n")

def update_contact():
    name = input("Enter the Name of the contact to update: ").strip()
    if name in contacts:
        print("\nEnter new details (leave blank to keep current value):")
        phone = input(f"Phone [{contacts[name]['Phone']}]: ").strip()
        email = input(f"Email [{contacts[name]['Email']}]: ").strip()
        address = input(f"Address [{contacts[name]['Address']}]: ").strip()

        if phone:
            contacts[name]['Phone'] = phone
        if email:
            contacts[name]['Email'] = email
        if address:
            contacts[name]['Address'] = address

        print(f"\n✅ Contact '{name}' updated successfully!\n")
    else:
        print("\n❌ Contact not found!\n")

def delete_contact():
    name = input("Enter the Name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"\n🗑️ Contact '{name}' deleted successfully!\n")
    else:
        print("\n❌ Contact not found!\n")

def menu():
    while True:
        print("======= 📘 Contact Book =======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("\n👋 Exiting Contact Book. Goodbye!\n")
            break
        else:
            print("\n⚠️ Invalid choice! Try again.\n")

# Run the program
menu()
