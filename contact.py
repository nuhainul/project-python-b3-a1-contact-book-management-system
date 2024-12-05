class Contact:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
    
    def get_contact_details(self):
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address
        }
    
    def __str__(self):
        return f"Name: {self.name} | Phone: {self.phone} | Email: {self.email} | Address: {self.address}"
