"""
The bot is used for adding contacts to the contacts list.
"""

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
    cmd, *args = user_input.split() # splitting the input on parts
    cmd = cmd.strip().lower() #Removing spaces and converting everything to lower cases
    return cmd, *args 

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
    if len(args) != 2: # Checks if there are 2 values in args list
        return "Error: Please provide a name and a phone number."
    name, phone = args #Assigning first value in args to "name" and 2nd value to "phone"
    contacts[name] = phone #Assigning name as a key, and [hone as a value in dictionary]
    return "Contact added."

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
        command, *args = parse_input(user_input) #Calling the parse_input function for adjusting user_input 
        if command in ["close", "exit"]: #ending the program with commands "close"/"exit"
            print("Good bye!")
            break
        elif command == "hello": #Answer on command "hello"
            print("How can I help you?")
        elif command == "add": #Answer on command "add"
            print(add_contact(args, contacts))
        elif command == "all": #Answer on command "all"
            if not contacts: #Answer if the dictionary is empty
                print("No contacts found.")
            print(contacts)
        else: #Handling not expected commands
            print("Invalid command.")
if __name__ == "__main__":
    main()
