contacts = {}

while True:
    print("\n===CONTACT BOOK===")
    print("1. View contact")
    print("2. Add contact")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice =input("choose an option:")

    if  choice =="1":
        if len(contacts) == 0:
            print("No contacts found")
        else:
            print("\nContacts:")
            for name, phone, in contacts.items():
                print(name, "-", phone)        
    elif choice =="2":
        name =input("Enter contact name:")
        phone = input("Enter phone number")
        contacts[name]= phone
        print("contact added successfully!")

    elif choice =="3":
        name =input("Ente conact name to search:")

        if name in contacts:
            print(name,"-", contacts[name])
        else:
            print("Contact not found.")

    elif choice =="4":
        name = input("Enter contact name to delete:")

        if name in contacts:
            del contacts[name]
            print("contact deleted successfully!")
        else:
            print("contact not found.")

    elif choice =="5":
        print("Goodbye!")
        break
    else:
        print("invalid choice.please try again")            


                 