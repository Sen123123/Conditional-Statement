class Grade:
    def __init__ (self):
        self.__number = 9002

    def display(self):
        print("The Grade is",self.__number)

    def setNumber(self,number):
        self.__number = number

ob = Grade()
ob.display()

ob.__number = 56

# ob.self_number = 56
# self.__number = 56

ob.display()
ob.setNumber(57)
ob.display()