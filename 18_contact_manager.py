contacts = [
    {
        "name": "Mona",
        "phone": "09123456789",
        "email": "mona@example.com"
    },
    {
        "name": "Neda",
        "phone": "09121234567",
        "email": "neda@example.com"
    },
    {
        "name": "Arman",
        "phone": "09141237896",
        "email": "arman@example.com"
    }
]


while True:
    print("\n===== Contact Manager =====")
    print("1. Show contact list")
    print("2. Add contact")
    print("3. Remove contact")
    print("4. Search contact")
    print("5. Update contact")
    print("6. Exit")

    choice = input("Choose option: ")

    # Show contacts
    if choice == "1":

        for contact in contacts:
            print(
                contact["name"], "|",
                contact["phone"], "|",
                contact["email"]
            )

    # Add contact
    elif choice == "2":

        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        new_contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(new_contact)

        print(f"{name} added!")

    # Remove contact
    elif choice == "3":

        name = input("Enter contact name to remove: ")

        found = False

        for contact in contacts:
            if contact["name"] == name:
                contacts.remove(contact)
                print(f"{name} removed!")
                found = True
                break

        if not found:
            print(f"{name} is not in your contact list.")

    # Search contact
    elif choice == "4":

        name = input("Enter name to search: ")

        found = False

        for contact in contacts:
            if contact["name"] == name:
                print("\nContact found:")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])

                found = True
                print(f"{name} is found!")
                break

        if not found:
            print(f"{name} is not in your contact list.")

    # Update contact
    elif choice == "5":

        name = input("Enter contact name to update: ")

        found = False

        for contact in contacts:
            if contact["name"] == name:

                new_phone = input("Enter new phone number: ")
                new_email = input("Enter new email: ")

                contact["phone"] = new_phone
                contact["email"] = new_email

                print(f"{name} updated!")

                found = True
                break

        if not found:
            print(f"{name} is not in your contact list.")

    # Exit
    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option!")