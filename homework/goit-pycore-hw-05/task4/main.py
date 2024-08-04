"""
The bot is used for adding contacts to the contacts list.
"""

from functools import wraps

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
        except ValueError:
            return "Give me name and phone please."
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
def add_contact(args, contacts):
    """
    Adds a new contact to the contacts dictionary.

    The function takes a list of arguments and a dictionary of contacts. 
    It expects the list of arguments to contain exactly two elements: 
    the contact's name and phone number. If the correct number of arguments 
    is provided, the contact is added to the dictionary. If the arguments 
    are incorrect, an error message is returned.

    Parameters:
    args (list): A list containing two elements: the contact's name (str) 
                 and the contact's phone number (str).
    contacts (dict): A dictionary where the keys are contact names (str) 
                     and the values are phone numbers (str). The dictionary 
                     is updated with the new contact.

    Returns:
    str: A confirmation message if the contact is added successfully, or 
         an error message if the number of arguments is incorrect.
    """
    #Below code is commented because decorator is used instead
    #if len(args) != 2: # Checks if there are 2 values in args list
        #return "Error: Please provide a name and a phone number."
    name, phone = args #Assigning first value in args to "name" and 2nd value to "phone"
    contacts[name] = phone #Assigning name as a key, and phone as a value in dictionary]
    return "Contact added."

@input_error
def get_contact(args, contacts):
    """
    Getting a contact from the contacts dictionary.
    """
    #Returning the contact based on the entered contact name from the dictionary
    return f"{args[0]} can be called at: {contacts[args[0]]}"

@input_error
def get_all_contacts(contacts):
    """
    Getting the list of all contacts from the contacts dictionary.
    """
    if not contacts: #Answer if the dictionary is empty
        return "No contacts found."
    return contacts

@input_error
def execute_command(command, args, contacts):
    """
    Main flow execution based on entered command.
    """
    if command == "hello":
        return "How can I help you?"
    elif command == "add":
        return add_contact(args, contacts)
    elif command == "all":
        return get_all_contacts(contacts)
    elif command == "get":
        return get_contact(args, contacts)
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
    contacts = {} #Initializing an empty dictionary
    print("Welcome to the assistant bot!") #Starting the bot 
    while True: #Starting the loop
        user_input = input("Enter a command: ") #Prompts user to enter the command
        if user_input:
          command, *args = parse_input(user_input) #Calling the parse_input function for adjusting user_input 
          if command in ["close", "exit"]: #ending the program with commands "close"/"exit"
              print("Good bye!")
              break
          else:
              print(execute_command(command, args, contacts))
if __name__ == "__main__":
    main()
