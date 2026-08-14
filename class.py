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
       # print(f"the capacity is {self.waterCapacity} and the remaining space is {filling}")
       if (filling > self.waterCapacity):
           print("The water will spill. Acction blocked")
       else:
            print(f"the capacity is {self.waterCapacity} and the remaining space is {self.waterCapacity-filling}")
waterLevel = WaterStorex(20)
waterToFill = waterLevel.toFill(41) 

# initialize with passed argument
class CardboardCup:
    def __init__(self,owner,size):
        self.owner = owner
        self.size = size
        self.isClean = True

cup1 = CardboardCup("Giwa",22)
print(cup1.isClean)

# inheritance and super
class Animal:
     def eat(sef):
         print("Eating")

class Dog(Animal):
    def bark(self):
        print("The dog is barking")

class Cat(Animal):
    def meow(self):
        print("The cat is meowing")

dog = Animal()
dog.eat()
dog = Dog()
dog.bark()
cat = Animal()
cat.eat()
cat = Cat()
cat.meow()


class CardboardCup:
    def __init__(self,size):
        self.size = size
        self.isClean = False
        self.contents_ounces = 0.0

class ChildClass(CardboardCup):
    def child(self):
        pass

cup = ChildClass("Large")
print(cup.size)
print()

class StudentName:
    def initialName(self):
        return "Giwa"

class finalName(StudentName):
    def final(self):
        return "Giwa Toheeb"

student = StudentName()
print(student.initialName()) 

student = finalName()
print(student.final())


class SchoolName:
    def __init__ (self,schName):
        self.schName = schName
        self.institution = "Unilorin"
        self.isService = True

class SecSchool(SchoolName):
    pass

school1 = SchoolName("Ajoke")
print(school1.schName)
print(school1.isService)

school = SecSchool("Ajoke Model School")
print(school.schName)
print(school.isService)
print(school.institution)
print(school1.institution)
print()

institution = SecSchool("Whatever I decide")
print(institution.institution)