# contact_manager/validator.py

class Validator:
    def validate_name(self, name):
        """Validates the contact name."""
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if any(char.isdigit() for char in name):
            raise ValueError("Name cannot contain numbers")
        return name.strip()  # Trim whitespace

    def validate_phone(self, phone):
        """Validates the contact phone number."""
        cleaned_phone = ''.join(filter(str.isdigit, phone))  # Keep only digits
        if not cleaned_phone:
            raise ValueError("Phone number must contain digits")
        if len(cleaned_phone) < 10:
            raise ValueError("Phone number must be at least 10 digits long")
        return cleaned_phone  # Return the cleaned phone number

    def validate_email(self, email):
        """Validates the contact email."""
        if not '@' in email or not '.' in email.split('@')[-1]:  # Simple email format validation
            raise ValueError("Invalid email format")
        return email.strip()  # Trim whitespace
