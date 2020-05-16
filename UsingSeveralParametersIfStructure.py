firstNumber = input("Give a number: ")
firstNumber = int(firstNumber)
secondNumber = input("Give another number: ")
secondNumber = int(secondNumber)

firstEven = firstNumber % 2
firstEven = int(firstEven)

secondEven = secondNumber % 2
secondEven = int(secondEven)

if (firstEven == 0) and (secondEven == 0):
    print("Both numbers are even.")
elif (firstEven == 0) and (secondEven == 1):
    print("One of the numbers is even.")
elif (firstEven == 1) and (secondEven == 0):
     print("One of the numbers is even.")
else:
    print("Both numbers are odd.")