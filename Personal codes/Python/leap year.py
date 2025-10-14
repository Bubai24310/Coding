year = int(input("Enter a year: "))

if year >= 1582:
    if year % 400 != 0:
        print("The year", year, "is a common year")
    else:
        print("The year", year, "is a leap year")
else:
    print("Not within the Gregorian calendar period")
