givenName = input("Give name: ")

if givenName == "John":
    passWord = input("Give password: ")
    if passWord == "ABC123":
        print("Both inputs are correct!")

    else:
         print("The password is incorrect.")

else:
    print("The given name is wrong.")