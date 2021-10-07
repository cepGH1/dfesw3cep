class Pracclass:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    def the_first_prog(self, aNum):
        print(aNum)


fiona = Pracclass("fiona", "XS")
for myItem in Pracclass.__dict__:
    print(myItem)

clare = Pracclass("clare", "S")

if fiona.size==clare.size:
    print(fiona.name, " can borrow ", clare.name, "'s clothes")
else:
    print("Nope")

print(fiona.__dict__)


