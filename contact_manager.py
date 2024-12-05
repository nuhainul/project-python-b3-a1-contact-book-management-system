import csv
import os
from contact import Contact
from validator import Validator

class ContactManager:
    def __init__(self):
        self.contacts = []
        self.filename = "contacts.csv"
        self.validator = Validator() # to validate 
        self.load_contacts()  # to load already saved contacts in starting

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    self.contacts.append(Contact(
                        row['name'],
                        row['email'],
                        row['phone'],
                        row['address']
                    ))

    def save_contacts(self):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'email', 'phone', 'address'])
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact.get_contact_details())

    def add_contact(self):
        try:
            print("\nAdd New Contact")
            print("-" * 20)

            name = input("Enter Name: ")
            name = self.validator.validate_name(name) # to validate name

            email = input("Enter Email: ")
            email = self.validator.validate_email(email) # to validate email 

            phone = input("Enter Phone Number: ")
            phone = self.validator.validate_phone(phone) # to validate phone

            # Check for duplicate phone numbers
            if any(contact.phone == phone for contact in self.contacts):
                print("Error: This phone number already exists!")
                return

            address = input("Enter Address: ")

            # Add new contact
            new_contact = Contact(name, email, phone, address)
            self.contacts.append(new_contact)
            self.save_contacts()
            print("\nContact added successfully!")
        except Exception as e:
            print(f"Error adding contact: {str(e)}")

    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts found!")
            return

        print("\nAll Contacts")
        print("-" * 50)
        for index, contact in enumerate(self.contacts, 1):
            print(f"{index}. {contact}")
        print("-" * 50)

    def search_contacts(self):
        if not self.contacts:
            print("\nNo contacts to search!")
            return

        search_term = input("\nEnter search term (name or phone): ").lower()
        found_contacts = [
            contact for contact in self.contacts
            if search_term in contact.name.lower() or search_term in contact.phone
        ]

        if found_contacts:
            print("\nSearch Results:")
            print("-" * 50)
            for contact in found_contacts:
                print(contact)
            print("-" * 50)
        else:
            print("\nNo matching contacts found!")

    def remove_contact(self):
        if not self.contacts:
            print("\nNo contacts to remove!")
            return

        self.view_contacts()  # to show contacts before removing
        try:
            index = int(input("\nEnter the number of the contact to remove: ")) - 1
            if 0 <= index < len(self.contacts):
                removed_contact = self.contacts.pop(index)
                self.save_contacts()
                print(f"\nRemoved contact: {removed_contact}")
            else:
                print("\nInvalid contact number!")
        except ValueError:
            print("\nPlease enter a valid number!")
