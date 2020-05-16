def Comparison(number_1, number_2):
      """This function takes two integers."""

      if number_1 == number_2:
          print("The numbers are equal.")
      elif number_1 > number_2:
          print("The first number is larger.")
      else:
          print("The second number is larger.") 

def main():
  value1 = 10
  value2 = 12
  Comparison(value1,value2)

if __name__ == "__main__":
    main()