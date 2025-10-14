from datetime import date


def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - (
        (today.month, today.day) < (birth_date.month, birth_date.day)
    )
    return age


# Input: Enter your birth year, month, and day
year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))

birth_date = date(year, month, day)
age = calculate_age(birth_date)

print(f"You are {age} years old.")
