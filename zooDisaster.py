from animals import antelope, bear, big_fish, bug, chicken, cow, fox, lion, little_fish, panda, sheep
from plants import leaf, grass


def eatingChain(animalArray):
    global animalEaten
    resultsArray = []
    i = 0
    while len(animalArray) > 1:
        newString = ""
        print(i)
        canEatLeft = False
        canEatRight = False
        hasEaten = False
        if animalArray[i].type == "grass" or animalArray[i].type == "leaf":
            i = i + 1
            continue
        try:
            if animalArray[i].ableToEat(animalArray[i - 1]) is True:
                canEatLeft = True
                print("Can Eat Left")
        except:
            pass

        try:
            if animalArray[i].ableToEat(animalArray[i + 1]) is True:
                canEatRight = True
                print("Can Eat Right")
        except:
            pass

        if canEatLeft is True:
            hasEaten, animalEaten = animalArray[i].eat(animalArray[i - 1])
        if canEatRight is True:
            hasEaten, animalEaten = animalArray[i].eat(animalArray[i + 1])

        if hasEaten is True:
            removeArray = []
            newString = animalArray[i].type + " has eaten " + animalEaten.type
            i = 0
            for j in range(len(animalArray)):
                if animalArray[j].isAlive is False:
                    removeArray.append(j)
            for j in range(len(removeArray)):
                animalArray.pop(removeArray[j])
                j = j - 1
        elif hasEaten is False:
            newString = animalArray[i].type + " Can't eat anything."
            i = i + 1

        resultsArray.append(newString)
    return resultsArray


def generateObjects(animalsToGenerate):
    global newObj
    animalArray = animalsToGenerate.split(",")
    arrayOfObjects = []
    for i in range(len(animalArray)):
        objectName = animalArray[i]
        if objectName == "antelope":
            newObj = antelope()
        if objectName == "bear":
            newObj = bear()
        if objectName == "bug":
            newObj = bug()
        if objectName == "chicken":
            newObj = chicken()
        if objectName == "cow":
            newObj = cow()
        if objectName == "fox":
            newObj = fox()
        if objectName == "lion":
            newObj = lion()
        if objectName == "panda":
            newObj = panda()
        if objectName == "sheep":
            newObj = sheep()
        if objectName == "little-fish":
            newObj = little_fish()
        if objectName == "big-fish":
            newObj = big_fish()
        if objectName == "leaf" or objectName == "leaves":
            newObj = leaf()
        if objectName == "grass":
            newObj = grass()
        arrayOfObjects.append(newObj)
    return arrayOfObjects


def main():
    resultArray = []
    exampleInput = "fox,bug,chicken,grass,sheep"
    objectArray = generateObjects(exampleInput)
    resultArray.append(exampleInput)
    resultArray = resultArray + eatingChain(objectArray)
    for i in range(len(resultArray)):
        print(resultArray[i])
    return


main()
