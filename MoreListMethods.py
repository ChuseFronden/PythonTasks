# -*- coding: cp1252 -*-
import pickle
filename = open("words.txt","r")
content = filename.readlines()
content.sort()

print("Words in an alphabetical order: ")
for i in content:
	print(i, end = '')

filename.close()