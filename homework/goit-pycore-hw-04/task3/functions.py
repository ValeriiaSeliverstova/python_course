import sys # Import the sys module
from pathlib import Path # Import the Path class from the pathlib module
from colorama import init, Fore, Back, Style # Import the init, Fore, Back, and Style classes from the colorama module

def get_directory_structure(absolute_path, level=0):
    """
    The function takes an absolute path to a directory and prints the directory structure in the following format:
    directory
        subdirectory
            subdirectory
        file
        file

    Parameters:
    absolute_path (str): The absolute path to the directory.
    level (int): The level of indentation to be used in the output.

    Returns:
    A structure of the specified directory.
    """
    directory = Path(absolute_path) # Create a Path object from the specified path
    if not directory.is_dir(): # Check if the specified path is a directory
        print(Fore.RED + "Error: The specified path is not a directory.")
        return
    indentation = '    ' * level # Create the indentation string based on the level
    try:
        for item in directory.iterdir(): # Iterate over the items in the directory
            if item.name.startswith('.'): # Skip hidden files and directories
                continue
            if item.is_dir(): # Check if the item is a directory
                print(indentation + Fore.BLUE + str(item.name))
                get_directory_structure(item, level + 1) # Recursively call the function to print the subdirectory structure
            else:
                print(indentation + Fore.GREEN + str(item.name))
    except:
        print(Fore.RED + "Error: The specified path does not exist.")

absolute_path = sys.argv[1] # Get the absolute path from the command line arguments
get_directory_structure(absolute_path)