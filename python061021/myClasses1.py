class MyClass:
   def __init__(self, age, height):
       self.myHeight = height
       self.myAge = age

   def speak_my_height(self):
       print(self.myHeight)

   def _speak_my_age(self):
       print(self.myAge) 
    
class Student:
    def __init__(self, name, age, class_="student"):
        self.name = name
        self.age = age
        self.class_ = class_
    
    def average_score(self, score1, score2, score3):
        result = (score1 + score2 + score3)/3
        return result

         
clare = Student("clare", 57, "st")
print(clare.age)
print(clare.class_)
stewart = Student("stewart", 57)
print(stewart.class_)
num = clare.average_score(20, 21, 22)
print(num)


       

        








