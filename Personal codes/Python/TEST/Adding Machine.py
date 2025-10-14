a = int(input("enter 1st number "))
a += int(input("enter next number "))
b = input("Type the command(+ / =):\t")
while b != '=':
    a += int(input("enter next number "))
    b = input("Type the command(+ / =):\t")

print("The sum of the numbers are: ", a)
