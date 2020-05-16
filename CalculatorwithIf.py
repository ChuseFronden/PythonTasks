print("Calculator")

firstNumber = input("Give the first number:")
firstNumber= int(firstNumber)
secondNumber = input("Give the second number:")
secondNumber = int(secondNumber)

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

calculatorNumber = input("Please select something (1-4): ")

calculatorNumber = int(calculatorNumber)
if calculatorNumber == 1:
    print("The result is:",plus)
elif calculatorNumber == 2:
    print("The result is:", minus)
elif calculatorNumber == 3:
    print("The result is:", multiplication)
elif calculatorNumber == 4:
    print("The result is:", division)
else:
    print("Selection was not correct.")