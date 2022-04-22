from abc import ABC, abstractmethod
from plants import *
from animals import *

class animal(ABC):
    #Attributes
    isAlive = True
    canEat = []

    #Contructors
    def __init__ (self,canEat):
        self.type = "Animal"
        self.canEat = canEat

    #Methods
    def eat(self,toEat):
        print(self.type+"ate"+toEat.type)
        for i in range(len(self.canEat)):
            if toEat == self.canEat[i]:
                toEat.isAlive = False
                return True,toEat
        return False,toEat
    
    def ableToEat(self,toEat):
        print(self.type+" Tried To Eat")
        for i in range(len(self.canEat)):
            testingObj = self.canEat[i]
            print(testingObj)
            print(testingObj.type)
            if toEat == testingObj:
                print(self.type+"can eat this")
                return True
            print("Could not eat",testingObj.type)
        return False

class mammal(animal):
    #Attributes

    #Contructors
    def __init__ (self,canEat):
        self.type = "Mammal"
        super().__init__(canEat)

    #Methods

class bird(animal):
    #Attributes

    #Contructors
    def __init__ (self,canEat):
        self.type = "Bird"
        super().__init__(canEat)

    #Methods

class insect(animal):
    #Attributes

    #Contructors
    def __init__ (self,canEat):
        self.type = "Insect"
        super().__init__(canEat)

    #Methods

class fish(animal):
    #Attributes

    #Contructors
    def __init__ (self,canEat):
        self.type = "Fish"
        super().__init__(canEat)

    #Methods

class antelope(mammal):
    #Attributes
    canEat = [grass]

    #Constructors
    def __init__ (self):
        self.type = "Antelope"
        super().__init__(self.canEat)

    #Methods



class bug(insect):
    #Attributes
    canEat = [leaf]

    #Constructors
    def __init__ (self):
        self.type = "Bug"
        super().__init__(self.canEat)

    #Methods

class chicken(bird):
    #Attributes
    canEat = [bug]

    #Constructors
    def __init__ (self):
        self.type = "Chicken"
        super().__init__(self.canEat)

    #Methods

class cow(mammal):
    #Attributes
    canEat = [grass]

    #Constructors
    def __init__ (self):
        self.type = "Cow"
        super().__init__(self.canEat)

    #Methods

class lion(mammal):
    #Attributes
    canEat = [cow,antelope]

    #Constructors
    def __init__ (self):
        self.type = "Lion"
        super().__init__(self.canEat)

    #Methods

class panda(mammal):
    #Attributes
    canEat = [leaf]

    #Constructors
    def __init__ (self):
        self.type = "Panda"
        super().__init__(self.canEat)

    #Methods

class sheep(mammal):
    #Attributes
    canEat = [grass]

    #Constructors
    def __init__ (self):
        self.type = "Sheep"
        super().__init__(self.canEat)

    #Methods

class little_fish(fish):
    #Attributes
    canEat = []

    #Constructors
    def __init__ (self):
        self.type = "Little-Fish"
        super().__init__(self.canEat)

    #Methods

class big_fish(fish):
    #Attributes
    canEat = [little_fish]

    #Constructors
    def __init__ (self):
        self.type = "Big-Fish"
        super().__init__(self.canEat)

    #Methods

class fox(mammal):
    #Attributes
    canEat = [chicken,sheep]

    #Constructors
    def __init__ (self):
        self.type = "Fox"
        super().__init__(self.canEat)

    #Methods

class bear(mammal):
    #Attributes
    canEat = [big_fish,bug,chicken,cow,leaf,sheep]

    #Constructors
    def __init__ (self):
        self.type = "Bear"
        super().__init__(self.canEat)

    #Methods