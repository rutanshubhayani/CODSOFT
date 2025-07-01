
contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append([name, phone, email, address])
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\nContact List:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact[0]} - {contact[1]}")
    print()

def search_contact():
    key = input("Enter name or phone number to search: ").lower()
    found = False
    for contact in contacts:
        if key in contact[0].lower() or key in contact[1]:
            print("\nContact Found:")
            print(f"Name: {contact[0]}")
            print(f"Phone: {contact[1]}")
            print(f"Email: {contact[2]}")
            print(f"Address: {contact[3]}\n")
            found = True
            break
    if not found:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ").lower()
    for contact in contacts:
        if contact[0].lower() == name:
            print("Leave field empty to keep current value.")
            new_name = input(f"New name ({contact[0]}): ") or contact[0]
            new_phone = input(f"New phone ({contact[1]}): ") or contact[1]
            new_email = input(f"New email ({contact[2]}): ") or contact[2]
            new_address = input(f"New address ({contact[3]}): ") or contact[3]
            contact[:] = [new_name, new_phone, new_email, new_address]
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").lower()
    for i, contact in enumerate(contacts):
        if contact[0].lower() == name:
            del contacts[i]
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")

def menu():
    while True:
        print("----- Contact Book -----")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

menu()