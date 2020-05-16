def tester(givenstring):
   if len(givenstring) < 10:
        return 0
   
   else:
        return 1



def main():
    text = input("Write something (quit ends): ")
    result = tester(text)
    if result == True:
     print("Too short")

    else:
     print(text)
   
   
    
if __name__ == "__main__":
    main()
 

