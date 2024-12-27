import json

def main_menu():
    print("Welcome to Contacts")
    print("Please select an option below:")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Remove Contact")
    print("4. Exit")

    while True:
        try:
            choice = int(input("Enter your choice (1/2/3/4):"))
            if choice in [1,2,3,4]:
                return choice
            else:
                print("Invalid choice. Please select 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#**********************************************************

#View Contact Function:
def view_contacts():
    try:
        # Load existing contacts
        with open("contacts.json", "r") as file:
            contacts = json.load(file)

        if not contacts:
            print("No contacts found.")
            return
        
        # Display all contact names
        print("Contacts:")
        for contact in contacts:
            print(f"- {contact['name']}")

        # Ask user for a specific contact
        while True:
            name_to_view = input("Enter the name of the contact to view details (or type 'exit' to return to the main menu): ").strip()

            if name_to_view.lower() == 'exit':
                return  # Exit to the main menu

            # Search for the contact
            found = False
            for contact in contacts:
                if contact["name"] == name_to_view:
                    print(f"Name: {contact['name']}")
                    print(f"Phone: {contact['phone']}")
                    print(f"Email: {contact['email']}")
                    found = True
                    break
            
            if not found:
                print(f"No contact found with the name '{name_to_view}'. Please try again.")

    except (FileNotFoundError, json.JSONDecodeError):
        print("No contacts file found or the file is empty.")

#**********************************************************

#Add Contact Function
def add_contact():
    # Full Name
    while True:
        try:
            full_name = input("Please enter the full name (First Last): ").strip()

            #Check if input is empty or spaces:
            if not full_name:
                raise ValueError("Name cannot be empty or just spaces.")
            
            #Split name into parts
            name_parts = full_name.split()
            if len(name_parts) < 2:
                raise ValueError("Please provide both first and last name separated by a space.")
            
            #Make sure all parts contain only alphabetic characters
            if not all(part.isalpha() for part in name_parts):
                raise ValueError("Names should only contain letters.")
            break #If everything works, exit the loop

        except ValueError as e:
            print(f"Invalid input: {e}")

    # Phone Number
    while True:
        phone_number = input("Enter the phone number (digits only): ").strip()
        if phone_number.isdigit():
            break
        else:
            print("Invalid input. Please enter digits only.")

    # Email
    while True:
        email = input("Enter the email address: ").strip()
        if "@" in email and "." in email.split("@")[-1]:
            break
        else:
            print("Invalid input. Please enter a valid email address.")

    # Save Contact
    new_contact = {"name": full_name, "phone": phone_number, "email": email}

    try:
        # Load existing contacts
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or is empty, start with an empty list
        contacts = []

    # Add the new contact
    contacts.append(new_contact)

    # Write updated contacts back to the file
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

    # Print Confirmation
    print(f"Contact added: {full_name}, Phone: {phone_number}, Email: {email}")

#**********************************************************

#Remove Contact Function:
def remove_contact():
    try:
        # Load existing contacts
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
        
        # Check if there are no contacts
        if not contacts:
            print("No contacts available to delete.")
            return
        
        # Display contacts
        print("Available contacts to delete: ")
        for contact in contacts:
            print(f"- {contact['name']}")
        
        while True:
            # Ask for the contact to remove
            name_to_remove = input("Enter the name of the contact to remove: ").strip()
            found = False

            # Search and remove the contact
            for contact in contacts:
                if contact['name'] == name_to_remove:  # Compare names
                    contacts.remove(contact)  # Remove the matching contact
                    found = True  # Set flag to True
                    print(f"Contact '{name_to_remove}' removed successfully.")
                    break  # Exit loop after removing
            
            if found:
                # Save updated contacts
                with open("contacts.json", "w") as file:
                    json.dump(contacts, file, indent=4)
                break  # Exit the outer while loop
            else:
                print(f"No contact found with the name '{name_to_remove}'. Please try again.")

    except (FileNotFoundError, json.JSONDecodeError):
        print("No contacts file found or the file is empty.")


#Main Program Loop

if __name__ == "__main__":
    while True:
        choice = main_menu()

        if choice == 1:
            view_contacts()
        elif choice ==2:
            add_contact()
        elif choice == 3:
            remove_contact()
        elif choice == 4:
            print("Thanks for using Contact Book")
            break
