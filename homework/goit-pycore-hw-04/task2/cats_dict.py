from pathlib import Path # Import the Path class from the pathlib module.
def get_cats_info(path):
    """
    This function reads a file with cat information and returns a list of dictionaries.

    Args:
    path (str or Path): The path to the file with cat information.

    Returns:
    list: A list of dictionaries with cats information.

    """
    file_path = Path(path) # Convert the path to a Path object.
    cats_dict_list = [] # Initialize an empty list to store the dictionaries.
    if path.exists(): # Check if the file exists.
        with open (path, "r", encoding = "utf8") as file: # Open the file in read mode.
            for line in file: # Go over each line in the file.
                line = line.strip()     # Remove any leading or trailing whitespace.
                try:  # Catch exceptions.
                    id, name, age = line.split(",") # Split the line into id, name, and age.
                    cat_dict = { # Create dictionary with cat information.
                        "ID": id,
                        "Name": name,
                        "Age": age
                    }
                    cats_dict_list.append(cat_dict) # Add the dictionary to the list.
                except ValueError: # Handling error.
                    print(f"Invalid data: {line}")
        return cats_dict_list # Return the list of dictionaries.
    else:
        return "File does not exist"

path = Path('cats.txt')
get_cats_info(path)
