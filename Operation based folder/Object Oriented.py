# class occupant:
#     job = "worker"
# ob = occupant()
# print("He is a", ob.job)

# class choices:
#     choice = "Eat"
# object = choices()
# print("what to", object.choice)

class parrot:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def dancing(self):
        print(self.name,"is dancing")

    def info(self):
        print(self.name,"is",self.age,"years old")

bluey = parrot("bluey",5)

bluey.dancing()
bluey.info()

Bingo = parrot("Bingo",23)

Bingo.dancing()
Bingo.info()