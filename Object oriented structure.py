# class employee:
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __del__(self):
#         print("the object has been deleted")
# Obj1= employee("David",32)
# del Obj1

class Library:

    def __init__(self,list,name):
        self.bookslist = list
        self.name = name
        self.DPL = {}

    def __displaybooks__(self):
        print(f"We have following books in our library:{self.name}")
        for book in self.bookslist:
            print(book)

    def addBook(self,book):
        self.bookslist.append(book)
        print("Book is added to the book list")

    def returnbook(self,book):
        self.DPL.pop(book)
