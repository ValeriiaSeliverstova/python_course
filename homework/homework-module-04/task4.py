from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    """
    The function get_upcoming_birthdays(users) is used to retrieve a list of upcoming birthdays within the next 7 days.
    """
    today = datetime.today().date()  # Retrieving the current date
    upcoming_birthdays = []  # Initialising the list to store upcoming birthdays
    
    for user in users:
        user_birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        birthday_this_year = user_birthday.replace(year=today.year)
        
        # If the birthday has already passed this year, consider next year's birthday
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # **Check if the birthday is within the next 7 days**
        if 0 <= (birthday_this_year - today).days <= 7:
            # Adjust for weekends
            if birthday_this_year.weekday() >= 5:  # 5: Saturday, 6: Sunday
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

# Example usage
users = [
    {"name": "John Doe", "birthday": "1985.07.12"},
    {"name": "Jane Smith", "birthday": "1990.12.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
