contacts = {}

def add_contact():
    name = input("Enter the contact's name: ")
    number = input("Enter the contact's phone number: ")
    contacts[name] = number
    print(f"Contact {name} added successfully.")

def edit_contact():
    name = input("Enter the name of the contact to edit: ")
    if name in contacts:
        new_number = input("Enter the new phone number: ")
        contacts[name] = new_number
        print(f"Contact {name} edited successfully.")
    else:
        print(f"Contact {name} not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

def search_contact():
    name = input("Enter the name of the contact to search: ")
    if name in contacts:
        print(f"Contact {name}: {contacts[name]}")
    else:
        print(f"Contact {name} not found.")

def view_all_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("Contacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")

while True:
    print("\nOptions:")
    print("1. Add Contact")
    print("2. Edit Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. View All Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        edit_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        search_contact()
    elif choice == '5':
        view_all_contacts()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")


