import sqlite3

# Create a database connection
conn = sqlite3.connect('contacts.db')

# Create a contacts table
conn.execute('''CREATE TABLE IF NOT EXISTS contacts
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             phone TEXT NOT NULL,
             email TEXT);''')


# Insert a new contact
def insert_contact(name, phone, email):
    conn.execute("INSERT INTO contacts (name, phone, email) \
                  VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()


# Retrieve all contacts
def get_contacts():
    cursor = conn.execute("SELECT id, name, phone, email from contacts")
    contacts = []
    for row in cursor:
        contacts.append(row)
    return contacts


# Update a contact
def update_contact(id, name, phone, email):
    conn.execute("UPDATE contacts set name = ?, phone = ?, email = ? where id = ?",
                 (name, phone, email, id))
    conn.commit()


# Delete a contact
def delete_contact(id):
    conn.execute("DELETE from contacts where id = ?", (id,))
    conn.commit()


# Get user input and execute appropriate function
while True:
    print("Select an option:")
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Update a contact")
    print("4. Delete a contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter the contact's name: ")
        phone = input("Enter the contact's phone number: ")
        email = input("Enter the contact's email address: ")
        insert_contact(name, phone, email)
        print("Contact added successfully!")
    elif choice == '2':
        contacts = get_contacts()
        for contact in contacts:
            print(contact)
    elif choice == '3':
        id = input("Enter the ID of the contact you want to update: ")
        name = input("Enter the contact's new name (leave blank to keep the current name): ")
        phone = input("Enter the contact's new phone number (leave blank to keep the current phone number): ")
        email = input("Enter the contact's new email address (leave blank to keep the current email address): ")
        update_contact(id, name, phone, email)
        print("Contact updated successfully!")
    elif choice == '4':
        id = input("Enter the ID of the contact you want to delete: ")
        delete_contact(id)
        print("Contact deleted successfully!")
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
conn.close()
