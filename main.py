from contact_manager import ContactManager

def main():
    manager = ContactManager()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Remove Contact")
        print("0. Exit")

        choice = input("\nEnter your choice (0-4): ")

        if choice == "1":
            manager.add_contact()
        elif choice == "2":
            manager.view_contacts()
        elif choice == "3":
            manager.search_contacts()
        elif choice == "4":
            manager.remove_contact()
        elif choice == "0":
            print("\nThank you for using Contact Management System!")
            break
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()
