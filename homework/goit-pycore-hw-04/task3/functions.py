import sys # Import the sys module
from pathlib import Path # Import the Path class from the pathlib module
from colorama import init, Fore, Back, Style # Import the init, Fore, Back, and Style classes from the colorama module

def get_directory_structure(absolute_path, level=0):
    directory = Path(absolute_path)
    if not directory.is_dir():
        print(Fore.RED + "Error: The specified path is not a directory.")
        return
    indentation = '    ' * level
    try:
        for item in directory.iterdir():
            if item.name.startswith('.'):
                continue
            if item.is_dir():
                print(indentation + Fore.BLUE + str(item.name))
                get_directory_structure(item, level + 1)
            else:
                print(indentation + Fore.GREEN + str(item.name))
    except:
        print(Fore.RED + "Error: The specified path does not exist.")

absolute_path = sys.argv[1]
get_directory_structure(absolute_path)