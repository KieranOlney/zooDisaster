from animals import antelope, bear, big_fish, bug, chicken, cow, fox, lion, little_fish, panda, sheep
from plants import leaf, grass

def objectFromString(objectName):
    try:
        animal = globals()[objectName]()
    except:
        print("Exception Occured :",objectName,"is not in my known organisms")
    return animal

def objectListFromString(inputString):
    animalArray = inputString.split(",")
    animalObjArray = []
    for animal in animalArray:
        animalObjArray.append(objectFromString(animal))
    return animalObjArray

def checkAliveAnimals(animals):
    aliveAnimals = []
    for animal in animals:
        if animal.isAlive is True:
            aliveAnimals.append(animal)
        else:
            continue
    return aliveAnimals

def checkAnimalEdible(hunter,prey):
    if hunter.type == "grass" or hunter.type == "leaf":
        return False
    try:
        if hunter.ableToEat(prey) is True:
            return True
        return False
    except:
        print("Exception Occured: Error in handling the Is animal Able to Eat Check",hunter.type)

def checkAnimalsAbleToEat(animals):
    anyAbleToEat = False
    if len(animals) == 1:
        return anyAbleToEat
    i = 0
    for i in range(len(animals)):
        if anyAbleToEat == True:
            break
        if i-1 < 0:
            if checkAnimalEdible(animals[i],animals[i+1]) is True:
                anyAbleToEat =  True
            continue
        elif i+1 >= len(animals):
            if checkAnimalEdible(animals[i],animals[i-1]) is True:
                anyAbleToEat =  True
            continue
        else:
            if checkAnimalEdible(animals[i],animals[i-1]) is True:
                anyAbleToEat =  True
            elif checkAnimalEdible(animals[i],animals[i+1]) is True:
                anyAbleToEat =  True
    return anyAbleToEat

def eatingChain(inputString):
    chainOutput = []
    chainOutput.append(inputString)
    animals = objectListFromString(inputString)
    anyAbleToEat = checkAnimalsAbleToEat(animals)
    while anyAbleToEat is True:
        for i in range(len(animals)):
            if i-1 < 0:
                if checkAnimalEdible(animals[i],animals[i+1]) is True:              
                    chainOutput.append(animals[i].eat(animals[i+1]))
                    break
            elif i+1 > len(animals):
                if checkAnimalEdible(animals[i],animals[i-1]) is True:
                    chainOutput.append(animals[i].eat(animals[i-1]))
                    break
            else:
                if checkAnimalEdible(animals[i],animals[i-1]) is True:
                    chainOutput.append(animals[i].eat(animals[i-1]))
                    break
                elif checkAnimalEdible(animals[i],animals[i+1]) is True:
                    chainOutput.append(animals[i].eat(animals[i+1]))
                    break
        animals = checkAliveAnimals(animals)
        anyAbleToEat = checkAnimalsAbleToEat(animals)
    finalString = ""
    for i in range(len(animals)):
        finalString += animals[i].type
        if i+1 < len(animals):
            finalString +=","
    chainOutput.append(finalString)
    return chainOutput

def main():
    exampleInput = "fox,bug,chicken,grass,sheep"
    print(eatingChain(exampleInput))
    return

main()