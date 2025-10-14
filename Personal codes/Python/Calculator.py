print("""\tHello user this a user freindly calculator
      Just follow the instructions.\n """)
Work = input('''Press ,
          \t\b + \tfor addition
          \t\b - \tfor substraction
          \t\b * \tfor multiplication
          \t\b / \tfor division
          \t\b sq\tfor square
          \nWhat you want to do\t''')
if Work == '+':
    print("\n\tYou want to make some additon\n")
    a = float(input("enter 1st number: \t"))
    a += float(input("enter next number: \t"))
    b = input("""Type the command
              ('+' to add anoer number)
              ('=' to get the result)
              \tSo your command is:\t """)
    while b != '=':
        a += float(input("enter next number: \t"))
        b = input("Type the command(+ / =):\t")
    print('\nThe result is\t', a)
elif Work == '-':
    print("\n\tYou want to make some substraction\n")
    a = float(input("enter 1st number: \t"))
    a -= float(input("enter next number: \t"))
    b = input("""Type the command
              ('-' to substract another number)
              ('=' to get the result)
              \tSo your command is:\t """)
    while b != '=':
        a -= float(input("enter next number: \t"))
        b = input("Type the command(- / =):\t")
    print('\nThe result is\t', a)
elif Work == '*':
    print("\n\tYou want to make some multipication\n")
    a = float(input("enter 1st number: \t"))
    a *= float(input("enter next number: \t"))
    b = input("""Type the command
              ('*' to multiply another number)
              ('=' to get the result)
              \tSo your command is:\t """)
    while b != '=':
        a *= float(input("enter next number: \t"))
        b = input("Type the command( * / =):\t")
    print('\nThe result is\t', a)
elif Work == '/':
    print("\n\tYou want to make some divition")
    a = float(input("enter divident: \t"))
    a /= float(input("enter divisor: \t"))
    b = input("""Type the command
              ('/' to divide by another number)
              ('=' to get the result)
              \tSo your command is:\t """)
    while b != '=':
        a /= float(input("enter divisor: \t"))
        b = input("Type the command( / or =):\t")
    print('\nThe result is\t', a)
elif Work == 'sq':
    print("\n\tYou want to know the squre of a number ")
    a = float(input("\nEnter the number\t"))
    print('\nThe result is\t', a**2, '\n')

print('\n\tThanks for using our programm\n')
