import random
import sys
import os

'''The two underscores are needed to make the variable private'''
class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0


    '''Custom Constuctor'''
    def __init__(self, name, height, weight, sound):
        self.__name = name;
        self.__height = height;
        self.__weight = weight;
        self.__sound = sound;


    '''Gettter and setter functions, always use self'''
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def toString(self):
        return "The name of Animal: {}\nHeight: {}\nWeight: {}\nSound: {}".format(self.__name,
                                                                                  self.__height,
                                                                                    self.__weight,
                                                                                  self.__sound)

''' Dealing with inheritance '''
class Dog(Animal):
    __owner = None

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        self.__animal_type = None
        super(Dog, self).__init__(name, height, weight, sound)

    def toString(self):
         return "The Owner: " + self.__owner + "\nThe Name: " + self.getName();



Turtle = Animal("MrMarco", 22, 200, "WROOF")
print(Turtle.toString())


print("\n\n")
spot = Dog("Spot", 53, 27, "Ruff", "Derek")
print(spot.toString())


# List Comprehensions, its simply placing element, but using a for loop

arr = [1,2,3,4,5,6]

squares = [n*n for n in arr]
print(squares)

nums = [5,10,15,20]

myList = [n for n in nums]
print(myList)

'''Place elements only if the current element is even'''

theList = [x for x in nums if x%2 == 0]
print(theList)

# form pairs
myLetters = ['a', 'b', 'c', 'd', 'e', 'f']
myNums = [1, 2, 3, 4]

thePairList = [(ch, val) for ch in myLetters for val in range(4)]
print(thePairList);

thePairList = [(ch, val) for ch in "Hi" for val in range(3)]
print(thePairList);

'''What the hell are generators?'''
numsArr = [2, 3, 4]


def squareAll(numsArr):
    result = []
    for m in numsArr:
        result.append(m*m)
    return result


numsArr = squareAll(numsArr)
print(numsArr)


def squareAllGen(numsArr):
    for m in numsArr:
        yield(m*m)


'''Note that we get an generator object'''
numsArr = squareAllGen(numsArr)

print(next(numsArr))
print(next(numsArr))
print(next(numsArr))


