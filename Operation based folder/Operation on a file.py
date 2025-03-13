# file = open("File.txt","r")
# print(file.read(12))
# file.close()

# file = open("File.txt","r")
# print(file.read())
# file.close()

# ofile = open("File.txt","a")
# ofile.write(" HELLO")
# ofile.close()

# filea = open("File.txt","r")
# fileb = open("Updated-file.txt","w")

# for line in filea.readlines():
#     if not (line.startswith ("Hello")):
#         print(line)
#         fileb.write(line)

# filea.close()
# fileb.close()

fileA = open("FileOne.txt","r")
fileb = open("Updated file.txt","w")

count = fileA.readlines()
type(count)

for i in range (1,len(count) + 1):
        if (i % 2 != 0):
            fileb.write(count[i-1])
        else:
            pass

var = open("Updated file.txt","r")
print(var.read())

fileA.close()
fileb.close()