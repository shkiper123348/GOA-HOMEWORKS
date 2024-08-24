number1 = int(input("Enter Number 1-50: "))
while number1  != 20:
    number2 = int(input("Enter Number : "))

    if number1 == number2:
        print ("you won")

    elif number1 < number2:
        print ("guess lower")

    else:
        print ("guess higher")