from abc import ABC, abstractmethod

class plant(ABC):
    #Attributes
    isAlive = True

    #Constructors
    def __init__ (self):
        self.type = "Plant"

    #Methods

class grass(plant):
    #Attributes

    #Constructors
    def __init__ (self):
        self.type = "Plant"
        
    #Methods

class leaf(plant):
    #Attributes

    #Constructors
    def __init__ (self):
        self.type = "Plant"
        
    #Methods