# def intro(name): 

#   print("Is you name,",name)

# name=input("Enter your name")

# intro(name)

def rf(x):
    if x == 1:
        return x
    else:
        return x*rf(x-1)
a = int(input("Enter a number"))
print("The factorial of ",a, "is ", rf(a))
