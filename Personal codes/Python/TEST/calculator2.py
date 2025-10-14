print("\n\tHello user this a user freindly calculator , just follow the instructions.\n ")
Work = input('''Press ,\n 
          \t\b + \tfor addition
          \t\b - \tfor substraction
          \t\b * \tfor multiplication
          \t\b / \tfor division
          \t\b sq\tfor square 
          \nWhat you want to do\t''')
if Work == '+':
    print("\n\tYou want to make some additon")
    a = float(input("\nEnter the first number\t"))
    b = float(input("\nEnter the second number\t"))
    print('\nThe result is\t',a + b,'\n')
elif Work == '-':
    print("\n\tYou want to make some substraction")
    a = float(input("\nEnter the first number\t"))
    b = float(input("\nEnter the second number\t"))
    print('\nThe result is\t',a - b,'\n')
elif Work == '*':
    print("\n\tYou want to make some multipication")
    a = float(input("\nEnter the first number\t"))
    b = float(input("\nEnter the second number\t"))
    print('\nThe result is\t',a * b,'\n')
elif Work == '/':
    print("\n\tYou want to make some divition")
    a = float(input("\nEnter the\t\bDividend\t"))
    b = float(input("\nEnter the\t\bDivisor\t"))
    print('\nThe result is\t',a / b,'\n')
elif Work == 'sq':
    print("\n\tYou want to know the squre of a number ")
    a = float(input("\nEnter the number\t"))
    print('\nThe result is\t',a**2,'\n')

print('\n\tThanks for using our programm\n')