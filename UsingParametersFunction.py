# -*- coding: cp1252 -*-

def poweroftwo(value):
    result = 2**value

    result = int(result)
    return result
    

def main():
    number = int(input("Give a number: "))

    final_result = poweroftwo(number)
    print("The result is",final_result)


if __name__ == "__main__":
    main()