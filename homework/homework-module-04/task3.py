import re
def normalize_phone(phone_number):
    """
    The function normalize_phone(phone_number) is used to normalize phone numbers according to the "+380XXXXXXXXX" format.
    Parameters:
    phone_number (str): The phone number to be normalized.
    Returns:
    str: The normalized phone number in the "+380XXXXXXXXX" format.
    """
    cleaned_number = re.sub(r'[^\d+]', '', phone_number) #re removes all characters except digits and +
    # Ensure the number starts with +380 if it doesn't start with +

    if cleaned_number.startswith('0'):
        cleaned_number = '+38' + cleaned_number 
    elif cleaned_number.startswith('380'):
        cleaned_number = '+' + cleaned_number
    elif not cleaned_number.startswith('+'):
        cleaned_number = '+38' + cleaned_number
    elif cleaned_number.startswith('+') and not cleaned_number.startswith('+380'):
        cleaned_number = '+38' + cleaned_number.lstrip('+')
    
    return cleaned_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
