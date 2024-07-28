#Task 1
from pathlib import Path # Import the Path class from the pathlib module.
def total_salary(path):
    """
    This function calculates the total and average salary from a file.

    Args:
        path (str or Path): The path to the file with salary data.
    
    Returns:
        tuple: A tuple containing the total salary and the average salary.
    """
    file_path = Path(path)  # Convert the path to a Path object.
    if file_path.exists(): # Check if the file exists.
        total = 0 # Initialize the total salary to 0.
        count = 0 # Initialize the count to 0.
        with open(path, "r", encoding = "utf-8") as file: # Open the file in read mode.
            for line in file: # Iterate over each line in the file.
                line = line.strip() # Remove any leading or trailing whitespace.
                try: # Catch exceptions 
                    name,salary = line.split(",") # Split the line into name and salary.
                    total += int(salary) # Add the salary to the total.
                    count += 1 # Increment the count.
                except ValueError: 
                    print(f"Invalid data: {line}")
            if count > 0: # Avoid division by zero.
                average = total / count # Calculate the average salary.
            return total, average # Return the total and average salary in tuple.
    else: # If the file does not exist.
       return "File does not exist"
    
path = Path('salary.txt')
total_salary(path)
