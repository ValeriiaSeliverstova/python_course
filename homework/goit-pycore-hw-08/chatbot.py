"""
The bot is used for adding contacts to the contacts list.
"""
# Importing the UserDict class
from functools import wraps
from collections import UserDict
from datetime import datetime, timedelta
import pickle

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
            raise ValueError("Phone number must be 10 digits long.")
        super().__init__(value)

    def __str__(self):
        """ Returns the field as a string """
        return self.value
    

class Name(Field):
    """ Class for a Name field"""
    def __init__(self, value):
        """ Initialize a name field with a value."""
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            value = datetime.strptime(value, "%d.%m.%Y")
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
    
    def __str__(self):
        """ Returns the field as a string """
        return self.value.strftime("%d.%m.%Y")

class Record:
    """ Class for contact record in dictionary(Address Book) """
    def __init__(self, name):
        """Initialize a name value as an object of Name Class. """
        self.name = Name(name)
        #Initialize an empty list of phones
        self.phones = []
        self.birthday = None
    
    def __str__(self):
        """Returns the record as a string with the text """
        return f"Contact name: {self.name.value}, phones: {'; '.join(phone.value for phone in self.phones)}"
    
    def add_phone(self, phone: Phone):
        """ Add a phone number to the record. """
        self.phones.append(phone)
        #print(f"Phone number {phone.value} has been added.")

    
    def remove_phone(self, phone):
        """ Remove a phone number from the record """
        #Looking for a phone number in a loop
        for item in self.phones:
            # I know that I do not need to use .value here, but I want to make it more readable for me.
            if item.value == phone:
                self.phones.remove(item)
                print(f"Phone number {phone} has been removed")
                return True
            else:
                print(f"Phone number {phone} not found")
                return False
    
    def edit_phone(self, old_phone, new_phone):
        """ Change a phone number in a record"""
        new_phone = Phone(new_phone)
        #Looking for a phone number in a loop
        for item in self.phones:
            if item.value == old_phone:
                item.value = new_phone.value
                return f"Phone number {old_phone} has been changed to {new_phone}"
                #return self.phones
            else:
                print(f"Phone number {old_phone} not found")
        
    # def find_phone(self, phone):
    #     """Find a phone in a record"""
    #     #Looking for a phone number in a loop
    #     for item in self.phones:
    #         if item.value == phone:
    #             print(f"Phone number {phone} has been found")
    #             return item.value
    #     return False
    
    def add_birthday(self, birthday):
        """Adds a birthday to the record."""
        self.birthday = Birthday(birthday)
    
    def show_birthday(self):
        """Returns the birthday as a string, or indicates that it is not set."""
        if self.birthday:
            return f"{self.name.value}'s birthday is on {self.birthday}"
        else:
            return f"No birthday set for {self.name.value}"
    
class AddressBook(UserDict):
    """ Class for an Address Book"""
    def __init__(self):
        """ constructor of the class"""
        super().__init__()

    def add_record(self, record: Record):
        """ Add a record to the address book. 
            Args:
            record (Record): The record to add."""
        #if isinstance(record, Record):
        self.data[record.name.value] = record
    
    def find(self, name):
        """ Find a record in an address book.
            Args:
            name - string value which will be used for finding  match in dictionary.
        """
        if name in self.data:
            #print(f"{self.data[name]} has been found")
            return self.data[name]
        else:
            return None
    
    def delete(self, name):
        """ Delete a record from an Address Book.
            Args: 
            name - string value which will be used for finding  match in dictionary.
        """
        if name in self.data:
            del self.data[name]
            print(f"Contact has been deleted")
    
    def add_birthday(self, name, birthday):
        """Adds a birthday to a record in the address book."""
        record = self.find(name)
        if not record:
            return f"No contact found with the name {name}. Please add the contact first."
        record.add_birthday(birthday)
        return f"Birthday {birthday} for {name} has been added."

    def show_birthday(self, name):
        """Show the birthday for a specific contact."""
        record = self.find(name)
        if record:
            return record.show_birthday()
        else:
            return f"No contact found with the name {name}."

    def birthdays(self):
        """
        The function get_upcoming_birthdays(users) is used to retrieve a list of upcoming birthdays within the next 7 days.
        """
        today = datetime.today().date()  # Retrieving the current date
        upcoming_birthdays = []  # Initialising the list to store upcoming birthdays
    
        for record in self.data.values():
            if record.birthday:
                contact_birthday = record.birthday.value.date()
                birthday_this_year = contact_birthday.replace(year=today.year)
        
                # If the birthday has already passed this year, consider next year's birthday
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
                # **Check if the birthday is within the next 7 days**
                if 0 <= (birthday_this_year - today).days <= 7:
                    # Adjust for weekends
                    if birthday_this_year.weekday() >= 5:  # 5: Saturday, 6: Sunday
                        birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            
                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "congratulation_date": birthday_this_year.strftime("%d.%m.%Y")
                        })
    
        return upcoming_birthdays

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Return an empty AddressBook if the file does not exist


def input_error(func):
    """
    The function is a decorator that catches exceptions in the decorated function.
    """
    #Protecting the function from exceptions
    wraps(func)
    def inner(*args, **kwargs):
        """
        The function is a wrapper that catches exceptions in the decorated function.
        """
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact does not exist."
        except ValueError as e:
            if func.__name__ == "add_contact":
                return "Give me name and phone please."
            # Catch any ValueError and return its message
            return str(e)
        except IndexError:
            return "Command arguments are missing or invalid."
        except NameError:
            return "Invalid command."
    return inner

@input_error
def parse_input(user_input):
    """
    Parses the user input into a command and its arguments.

    The function splits the user input string into separate words. 
    The first word is treated as the command, and the remaining words 
    are treated as arguments. The command is stripped of leading and 
    trailing whitespace and converted to lowercase to ensure 
    case-insensitive command recognition.

    Parameters:
    user_input (str): The input string entered by the user.

    Returns:
    tuple: A tuple where the first element is the command (str) and the 
    second element is a list of arguments (list of str).
    """
    if not user_input.strip():
            raise ValueError
    cmd, *args = user_input.split() # splitting the input on parts
    cmd = cmd.strip().lower() #Removing spaces and converting everything to lower cases
    return cmd, *args

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    try:
        phone_obj = Phone(phone)
    except ValueError as e:
        return str(e)
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone_obj)
    return message
@input_error
def add_birthday(book: AddressBook, birthday):
        birthday_obj= Birthday(birthday)
        book.add_record.add_birthday(birthday_obj)
        return f"Birthday added for {book.name.value}"

@input_error
def get_all_contacts(book: AddressBook):
    """
    Getting the list of all contacts from the contacts dictionary.
    """
    if not book: #Answer if the dictionary is empty
        return "No contacts found."
    result = []
    for name, record in book.items():
        result.append(f"{name}: {record}")
    return "\n".join(result)

@input_error
def get_contact(args, book: AddressBook):
    """
    Getting a contact from the contacts dictionary.
    """
    #Returning the contact based on the entered contact name from the dictionary
    return f"{args[0]} can be called at: {book[args[0]]}"

@input_error
def execute_command(command, args, contacts):
    """
    Main flow execution based on entered command.
    """
    if command == "hello":
        return "How can I help you?"
    elif command == "add":
        return add_contact(args, contacts)
    elif command == "change":
        if len(args) < 3:
            return "Please provide a name, old phone number, and new phone number."
        name, old_phone, new_phone = args[0], args[1], args[2]
        record = contacts.find(name)
        if record:
            return record.edit_phone(old_phone, new_phone)
        else:
            return f"No contact found with the name {name}."
    elif command == "phone":
        return get_contact(args, contacts)
    elif command == "all":
        return get_all_contacts(contacts)
    elif command == "add-birthday":
        if len(args) < 2:
            return "Please provide both a name and a birthday."
        name, birthday = args[0], args[1]
        return contacts.add_birthday(name, birthday)
    elif command == "show-birthday":
        if len(args) < 1:
            return "Please provide a name."
        return contacts.show_birthday(args[0])
    elif command == "birthdays":
        return contacts.birthdays()
    else:
      raise NameError
    
@input_error
def main():
    """
    The main function of the assistant bot.

    This function initializes the contacts dictionary and starts an 
    infinite loop to interact with the user via the command line. It 
    prompts the user to enter commands and processes them accordingly. 
    The function supports various commands to add, display, and manage 
    contacts.

    Commands supported:
    - "hello": Prints a greeting message.
    - "add [name] [phone]": Adds a new contact with the given name and 
      phone number to the contacts dictionary.
    - "all": Displays all contacts stored in the dictionary.
    - "close" or "exit": Exits the bot with a goodbye message.

    The function also prints an error message for any invalid commands.
    """
    #contacts = AddressBook() #Initializing an empty dictionary
    contacts = load_data()
    print("Welcome to the assistant bot!") #Starting the bot 
    while True: #Starting the loop
        user_input = input("Enter a command: ") #Prompts user to enter the command
        if user_input:
          command, *args = parse_input(user_input) #Calling the parse_input function for adjusting user_input 
          if command in ["close", "exit"]: #ending the program with commands "close"/"exit"
              save_data(contacts)
              print("Good bye!")
              break
          else:
              print(execute_command(command, args, contacts))




# if __name__ == "__main__":
#      main()

addressbook = AddressBook()

#Positive tests:
print(execute_command("hello", [], addressbook))
print(execute_command("add", ["John", "1234567890"], addressbook))
print(execute_command("add", ["Jane", "9876543210"], addressbook))
print(execute_command("all", [], addressbook))
print(execute_command("change", ["John", "1234567890", "1112223333"], addressbook))
print(execute_command("phone", ["John"], addressbook))
print(execute_command("add-birthday", ["John", "11.08.1990"], addressbook))
print(execute_command("show-birthday", ["John"], addressbook))
print(execute_command("birthdays", [], addressbook))

addressbook = AddressBook()

#Negative tests:
print(execute_command("test", [], addressbook))
print(execute_command("add", ["John", "123456789"], addressbook))
print(execute_command("phone", ["John"], addressbook))
print(execute_command("change", ["John", "1234567890", "1112223333"], addressbook))
print(execute_command("add-birthday", ["John", "01.01.2000"], addressbook))
print(execute_command("add", ["David", "1234567890"], addressbook))
print(execute_command("add-birthday", ["David", "01.01.97"], addressbook))
print(execute_command("show-birthday", ["John"], addressbook))
print(execute_command("birthdays", [], addressbook))



# print("*******************************************************")
# field1 = Field("1234") # "1234" is the argument for the constructor of the Field class
# field2 = Field("5678")
# print(field1.value)
# print(field2.value)
# print(field1)
# print(field2)
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
# book = AddressBook()

# # Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
# john_record.add_birthday("01.01.2000")

# # Додавання запису John до адресної книги
# book.add_record(john_record)

# # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# jane_record.add_birthday("12.08.1997")
# book.add_record(jane_record)

# Виведення всіх записів у книзі
#for name, record in book.data.items():
#   print(record)

# Знаходження та редагування телефону для John
#john = book.find("John")
#john.edit_phone("1234567890", "1112223333")

#print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
#found_phone = john.find_phone("5555555555")
#print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
#book.delete("Jane")
#print(book.birthdays())
