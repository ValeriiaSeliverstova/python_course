import sys
from pathlib import Path
from colorama import init, Fore, Back, Style

def get_directory_structure(absolute_path, level=0):
    directory = Path(absolute_path)

    indentation = '   ' * level
    for item in directory.iterdir():
        if item.name == '.DS_Store':
            continue
        if item.is_dir():
            print(indentation + Fore.BLUE + str(item.name))
            get_directory_structure(item, level + 1)
        else:
            print(indentation + Fore.GREEN + str(item.name))

absolute_path = sys.argv[1]
get_directory_structure(absolute_path)