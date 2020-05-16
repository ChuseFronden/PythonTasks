# -*- coding: cp1252 -*-

import mymodule

def main():
    value = "Exampleline"
    final = mymodule.printme()
    print("I got: ", value)
    print("The parameter was ", final ,"characters long.")

    

if __name__ == "__main__":
      main()