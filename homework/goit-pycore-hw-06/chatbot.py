# Importing the UserDict class
from collections import UserDict

class Field:
    """A base class for all fields in the address book."""
    def __init__(self, value):
        """ Initialize a field with a value. """
        self.value = value

    def __str__(self):
        """Returns the field as a string"""
        return str(self.value)

class Phone(Field):
    """ Class for a phone number field """
    def __init__(self, value):
        """Initialize a phone number field with a value."""
        #Validation of phone number (only digits and only 10 symbols)
        if (not value.isdigit()) or (len(value) != 10):
            raise ValueError("Phone number must be digit")
        super().__init__(value)

    def __str__(self):
        """ Returns the field as a string """
        return self.value
    

class Name(Field):
    """ Class for a Name field"""
    def __init__(self, value):
        """ Initialize a name field with a value."""
        super().__init__(value)

class Record:
    """ Class for contact record in dictionary(Address Book) """
    def __init__(self, name):
        """Initialize a name value as an object of Name Class. """
        self.name = Name(name)
        #Initialize an empty list of phones
        self.phones = []
    
    def __str__(self):
        """Returns the record as a string with the text """
        return f"Contact name: {self.name.value}, phones: {'; '.join(phone.value for phone in self.phones)}"
    
    def add_phone(self, phone):
        """ Add a phone number to the record. """
        self.phones.append(Phone(phone))
        print(f"Phone number {phone} has been added")
    
    def remove_phone(self, phone):
        """ Remove a phone number from the record """
        #Looking for a phone number in a loop
        for item in self.phones:
            # I know that I do not need to use .value here, but I want to make it more readable for me.
            if isinstance(item, Phone) and item.value == phone:
                self.phones.remove(item)
                print(f"Phone number {phone} has been removed")
                return True
            else: 
                print(f"Phone number {phone} not found")
    
    def edit_phone(self, phone, new_phone):
        """ Change a phone number in a record"""
        #define value "phone" and "new_phone" as an objects of Phone Class
        self.phone = Phone(phone)
        self.new_phone = Phone(new_phone)
        #Looking for a phone number in a loop
        for item in self.phones:
            if isinstance(item, Phone) and item.value == phone:
                item.value = new_phone
                print(f"Phone number {phone} has been changed to {new_phone}")
                return self.phones
            else:
                print(f"Phone number {phone} not found")
        
    def find_phone(self, phone):
        """Find a phone in a record"""
        #Looking for a phone number in a loop
        for item in self.phones:
            if isinstance(item, Phone) and item.value == phone:
                print(f"Phone number {phone} has been found")
                return item.value
        return False
    
class AddressBook(UserDict):
    """ Class for an Address Book"""
    def __init__(self):
        """ constructor of the class"""
        super().__init__()

    def add_record(self, record):
        """ Add a record to the address book. 
            Args:
            record (Record): The record to add."""
        if isinstance(record, Record):
            self.data[record.name.value] = record
            print(f"Record for {record} has been added")
    
    def find(self, name):
        """ Find a record in an address book.
            Args:
            name - string value which will be used for finding  match in dictionary.
        """
        if name in self.data:
            print(f"{self.data[name]} has been found")
            return self.data[name]
        else:
            return False
    
    def delete(self, name):
        """ Delete a record from an Address Book.
            Args: 
            name - string value which will be used for finding  match in dictionary.
        """
        if name in self.data:
            del self.data[name]
            print(f"Contact has been deleted")
    
# print("*******************************************************")
# field1 = Field("1234") # "1234" is the argument for the constructor of the Field class
# field2 = Field("5678")
# print(field1.value)
# print(field2.value)
# print("*******************************************************")
# phone1 = Phone("1234567890")
# print(phone1.value)
# print("*******************************************************")
# name1 = Name("Valeriia")
# print(name1.value)
# print("*******************************************************")
# record1 = Record("valeriia")
# record1.add_phone("1234567890")
# record1.add_phone("0987654321")
# print("*******************************************************")
# record1.remove_phone("1234567890")
# record1.remove_phone("0987654322")
# print("*******************************************************")
# record1.edit_phone("0987654321", "0987654322")
# record1.edit_phone("0987654321", "0987654322")
# print("*******************************************************")
# record1.find_phone("0987654322")
# print("*******************************************************")
# address_book = AddressBook()
# address_book.add_record(record1)
# print("*******************************************************")
# address_book.find("valeriia")
# print("*******************************************************")
# address_book.delete("valeriia")


# print("*******************************************************")

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")