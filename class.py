# creating class in OOP
class MyInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

printInfo = MyInfo("Giwa",16)
print(printInfo)

print(printInfo.name,printInfo.age)

# Acess and modifying attribute

class SchoolMateria:
    def __init__(self):
        self.book = "Stationary"
        self.pen = "Lucky"

giwaMateria = SchoolMateria()
print(giwaMateria.pen,giwaMateria.book)
print(giwaMateria.book)


# uisng dunder
class MyInfo:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f'MyInfo({self.name},{self.age})'
    
person = repr(MyInfo("Giwas",22))
print(person)

#Exercise

class WaterStorex:
    def __init__(self, capacity):
        self.waterCapacity = capacity

    def toFill(self,filling):
        print(f"the capacity is {self.waterCapacity} and the remaining space is {filling}")

waterLevel = WaterStorex(20)
waterLevel.toFill(14)