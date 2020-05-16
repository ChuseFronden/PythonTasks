print("Calculator")
keepgoing = True
firstNumber = int(input("Give the first number: "))
secondNumber = int(input("Give the second number: "))

while keepgoing:
    

    plus = firstNumber + secondNumber
    plus = int(plus)
    minus = firstNumber - secondNumber
    minus = int(minus)
    multiplication = firstNumber * secondNumber
    multiplication = int(multiplication)
    division = firstNumber / secondNumber
    division = float(division)

    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5) Change numbers")
    print("(6) Quit")
    print("Current numbers:", firstNumber, secondNumber)
    calculatorNumber = int(input("Please select something (1-6): "))

    if calculatorNumber == 6:
        keepgoing = False
        print("Thank you!")
    else:
        if calculatorNumber == 1:
         print("The result is:",plus)
    
        elif calculatorNumber == 2:
         print("The result is:", minus)

        elif calculatorNumber == 3:
         print("The result is:", multiplication)

        elif calculatorNumber == 4:
         print("The result is:", division)

        else:
            firstNumber = int(input("Give the first number: "))
            secondNumber = int(input("Give the second number: "))
            continue
            
            
         




