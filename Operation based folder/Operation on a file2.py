# import os
# file = open ("Fluent.txt","r")
# data = file.readlines()
# print("Words in this files are.")
# for line in data:
#     word = line.split()
#     print (word)
# file.close ()

import os

file = open ("null1.txt","x")
file.close()

if os.path.exists("null1.txt"):
  os.remove ("null1.txt")
  print("File removed")
else:
  print("the file does not exist")
none = open("null1.txt","w")
none.close()
os.remove("null1.txt")

os.rmdir('null')