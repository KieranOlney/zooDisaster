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
        print(self.type,"ate",toEat.type)
        for i in range(len(self.canEat)):
            if toEat == self.canEat[i]:
                toEat.isAlive = False
                return True,toEat
        return False,toEat
    
    def ableToEat(self,toEat):
        for i in range(len(self.canEat)):
            testPrey = self.canEat[i]
            print(self.type,"Tried To Eat",testPrey)
            if toEat.type == testPrey:
                print(self.type+"can eat this")
                return True
            print("Could not eat",testPrey)
        return False

class mammal(animal):
    #Attributes

    #Contructors
    def __init__ (self,canEat):
        super().__init__(canEat)
        self.type = "mammal"


    #Methods

class bird(animal):
    #Attributes

    #Contructors
    def __init__ (self,canEat):
        super().__init__(self.canEat)
        self.type = "bird"

    #Methods

class insect(animal):
    #Attributes

    #Contructors
    def __init__ (self,canEat):
        super().__init__(self.canEat)
        self.type = "insect"

    #Methods

class fish(animal):
    #Attributes

    #Contructors
    def __init__ (self,canEat):
        super().__init__(self.canEat)
        self.type = "fish"

    #Methods

class antelope(mammal):
    #Attributes
    canEat = ["grass"]

    #Constructors
    def __init__ (self):
        super().__init__(self.canEat)
        self.type = "antelope"

    #Methods



class bug(insect):
    #Attributes
    canEat = ["leaf"]

    #Constructors
    def __init__ (self):
        super().__init__(self.canEat)
        self.type = "bug"

    #Methods

class chicken(bird):
    #Attributes
    canEat = ["bug"]

    #Constructors
    def __init__ (self):
        super().__init__(self.canEat)
        self.type = "chicken"

    #Methods

class cow(mammal):
    #Attributes
    canEat = ["grass"]

    #Constructors
    def __init__ (self):
        super().__init__(self.canEat)
        self.type = "cow"

    #Methods

class lion(mammal):
    #Attributes
    canEat = ["cow","antelope"]

    #Constructors
    def __init__ (self):
        super().__init__(self.canEat)
        self.type = "lion"

    #Methods

class panda(mammal):
    #Attributes
    canEat = ["leaf"]

    #Constructors
    def __init__ (self):
        super().__init__(self.canEat)
        self.type = "panda"

    #Methods

class sheep(mammal):
    #Attributes
    canEat = ["grass"]

    #Constructors
    def __init__ (self):
        super().__init__(self.canEat)
        self.type = "sheep"

    #Methods

class little_fish(fish):
    #Attributes
    canEat = []

    #Constructors
    def __init__ (self):
        super().__init__(self.canEat)
        self.type = "little_Fish"

    #Methods

class big_fish(fish):
    #Attributes
    canEat = ["little_fish"]

    #Constructors
    def __init__ (self):
        super().__init__(self.canEat)
        self.type = "big_Fish"

    #Methods

class fox(mammal):
    #Attributes
    canEat = ["chicken","sheep"]

    #Constructors
    def __init__ (self):
        super().__init__(self.canEat)
        self.type = "fox"


    #Methods

class bear(mammal):
    #Attributes
    canEat = ["big_fish","bug","chicken","cow","leaf","sheep"]

    #Constructors
    def __init__ (self):
        super().__init__(self.canEat)
        self.type = "bear"


    #Methods