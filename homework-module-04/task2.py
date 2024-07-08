#Task2
import random #Required for generating random numbers'
def get_numbers_ticket(min, max, quantity):
    """
    The function is used to generate a set of unique random numbers for lotteries. 
    This function returns a random set of numbers within the specified parameters, 
    ensuring that all numbers in the set are unique.

      Parameters:
    min (int): The minimum value in the range.
    max (int): The maximum value in the range.
    quantity (int): The number of unique random numbers to generate.

    Returns:
    random_numbers (list): A list of unique random numbers within the specified range.
    str: An error message if the input values are invalid.
    """
    if min >= 1 and max <= 1000 and 1 <= quantity <= 1000: #Checks if the input values are in the required range
        random_numbers = sorted(random.sample(range(min, max), k=quantity)) #generates unique random numbers in sorted list
        return random_numbers #Returns the list of random numbers
    else:
        return "Invalid input. Please enter valid values for min, max and quantity" #Returns this message if the input values are not in the required range
min = int(input("Enter the minimum value: "))
max = int(input("Enter the maximum value: "))
quantity = int(input("Enter the quantity of numbers: "))
print(get_numbers_ticket(min, max, quantity))
