#Task 1
from datetime import datetime #Required for using datetime objects
date_given = input("Enter the date in format YYYY-MM-DD: ") #Prompts the user to enter a date in the specified format
def get_days_from_today(date_given):
    """
    Task 1: The function get_days_from_today(date) is used to calculate the number of days 
    between a specified date(entered as input) and the current date.

    Parameters:
    date_given (str): The date (input value in specified format) to calculate the difference from the current date.
    Returns:
    int: The number of days between the current date and the entered date.    
    """
    try:
        date_given_object = datetime.strptime(date_given, "%Y-%m-%d") #Converts the entered date to a datetime object
    except:
        return str("Invalid date format. Please enter the date in format YYYY-MM-DD") #Returns this message if the entered date is not in the correct format
    date_now = datetime.now() #Gets the current date and time
    dates_difference = date_now - date_given_object #Calculates the difference between the current date and the entered date
    return int(dates_difference.days) #Returns the number of days between the current date and the entered date
print(get_days_from_today(date_given))
