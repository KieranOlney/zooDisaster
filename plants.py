from abc import ABC, abstractmethod

class plant(ABC):
    #Attributes
    isAlive = True

    #Constructors
    def __init__ (self):
        self.type = "plant"

    #Methods

class grass(plant):
    #Attributes

    #Constructors
    def __init__ (self):
        self.type = "grass"
        
    #Methods

class leaf(plant):
    #Attributes

    #Constructors
    def __init__ (self):
        self.type = "leaf"
        
    #Methods