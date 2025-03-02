class Parent:
  def __init__ (self,name,age,mood):
    self.name=name
    self.age=age
    self.mood=mood
  def display(self):
    print("name is",self.name,"and age is",self.age) 

class Child(Parent):
  def __init__ (self,name,age,mood,eyeColour,hairColour):
    self.eyeColour=eyeColour
    self.hairColour=hairColour
    super().__init__ (name,age,mood)


object = Child("Steve",17,"Neutral","Navy Blue","Brown")

object.display()