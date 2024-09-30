import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    
    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\nYour Contacts:")
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Search contacts by name
def search_contact(contacts):
    search_name = input("Enter the name to search: ").lower()
    found_contacts = [c for c in contacts if search_name in c['name'].lower()]
    
    if found_contacts:
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contact found with that name.")

# Update a contact
def update_contact(contacts):
    view_contacts(contacts)
    contact_num = int(input("\nEnter the contact number to update: ")) - 1
    
    if 0 <= contact_num < len(contacts):
        name = input("Enter new name (or press Enter to keep it the same): ")
        phone = input("Enter new phone number (or press Enter to keep it the same): ")
        email = input("Enter new email address (or press Enter to keep it the same): ")
        
        if name:
            contacts[contact_num]['name'] = name
        if phone:
            contacts[contact_num]['phone'] = phone
        if email:
            contacts[contact_num]['email'] = email
        
        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Invalid contact number.")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    contact_num = int(input("\nEnter the contact number to delete: ")) - 1
    
    if 0 <= contact_num < len(contacts):
        contacts.pop(contact_num)
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Invalid contact number.")

def menu():
    contacts = load_contacts()
    while True:
        print("\nMenu:")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
