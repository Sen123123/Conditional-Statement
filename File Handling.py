file = open("File.txt","r")
print(file.read())

file1 = open("File.txt","w")
file1.write("Hello world")

file1.close()
file.close()

file2 = open("File.txt","a")
file2.write(". Hello Earth")

file2.close()

file3 = open("File.txt","r")

Content = file3.read()
Colist = Content.split("\n")
Counter = 0

for i in Colist:
    if i:
        Counter+= 1

print("There are this much amout of files in ",Counter)


