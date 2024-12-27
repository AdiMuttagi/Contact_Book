# Contact Book

## Description:
The Contact Book is a Python-based program that allows users to manage their personal contacts. It supports adding, removing, viewing, and searching contacts, with all data stored in a JSON file for persistence.

## Features:
- **Add Contact**:
  - Input contact details (name, phone number, and email).
  - Prevents duplicate contacts by checking names.
- **Remove Contact**:
  - Search for a contact by name and delete it.
- **View Contacts**:
  - Displays a list of all contact names.
  - Allows viewing details of a selected contact.
- **Exit Program**:
  - Saves all changes and exits gracefully.

## How to Run:
1. Clone this repository or download the project files.
2. Ensure you have Python 3 installed on your system.
3. Open a terminal in the project directory.
4. Run the program

## Areas of Improvement
1. Edit Contacts: Add functionality to allow users to edit individual contact details (e.g., phone number, email) without deleting and re-adding the contact.
2. Sort Contacts Alphabetically: Implement sorting to display contact names in alphabetical order when viewing the contact list.
3. Enhanced Search: Improve search functionality to support partial matches (e.g., typing "John" would display "John Doe").
4. Validation Enhancements: Add more robust validation for phone numbers and emails to ensure consistent formatting (e.g., 123-456-7890 for phone numbers).
5. Better User Experience: Include menu shortcuts (e.g., pressing 1 or v for "View Contacts") to make navigation faster.
6. Error Handling: Improve error handling for cases like corrupted JSON files or write failures during save operations.
7. Backup Support: Add the ability to export and import contacts in other formats (e.g., CSV or XML) for backup purposes.
