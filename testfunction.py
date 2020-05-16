def getlength(testme):
      if len(testme) < 42:
          return 0
      else:
          return 1

result = getlength("ohgodwhydoesthisstringhavetobesolongicanteverrememberthis")
if result == True:
    print("This string is long enough.")
else:
 print("This string is too short.")