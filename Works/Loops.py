# for a in range (1,11):
#   for a in range (1,7):
#     print ("39 x",a,"=",39*a)

num=int(input("Enter the number: "))
for i in range(1,num+1):
    for j in range(i):
       print("*", end=" ")
    print()