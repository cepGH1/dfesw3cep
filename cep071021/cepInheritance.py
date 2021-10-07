from abc import ABC, abstractmethod

class Bird(ABC):
    fly = True
    babies = 0
    def noise(self):
        return "squawk"
    def reproduce(self):
        self.babies += 1
    @abstractmethod
    def eat(self):
        pass

    extinct = False

class Eagle(Bird):
    def eat():
        return "rabbits"
class Sparrow(Bird):
    def eat():
        return "seeds"

class Dodo(Bird):
    Fly = False
    extinct = True

    def eat(self):
        return "Nom nom"

    def reproduce(self):
        if not self.extinct:
            self.babies += 1

gerald = Dodo()

print(gerald.__dict__)

myEagle = Eagle
print(myEagle.babies)
myEagle.babies = 2
print(myEagle.babies)
mySparrow = Sparrow()
print(mySparrow.babies)