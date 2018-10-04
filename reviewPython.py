
# For random generator
import random;
import sys;
import os;

print("Hello World");

'''
MultiLine 
comment

Note:
%c for character
%d for integer
$f for floating point
%s for string
%u for unsigned integer

To concatenate string we need to use a comma
example: print("The cat ran ", numOfMiles, "in one day" );
'''

#Singlecommment

'''
We have five data types in Python

numbers
strings
list, this is essentially an array
tuples, this is an array where every single element is constant 
Dictionaries
'''


numOfMiles = 3;
print("The cat ran", numOfMiles, "miles in one day" );

print("Hello my name is:", 2+2, "I am hungry");

name = "Bob";
print(name);

number = 2+5;
print(number);

quote = "The turtle is hungry";
print(quote);

# Array
myList = ["Cat", "Frog", "Ninja"];

# Insert will add an element and then shift over the rest of the elements.
myList.insert(1, "Pickle");

print(myList);

myList.sort();
print(myList);

'''What is the size of the array'''
size = len(myList);

print("The size of my Array", size);


'''What is tuple?'''
'''A list with only constant elements'''
theTuple = (1, 2, 3, 4, 5);


'''Convert the tuple into a list and 
do modifications and then make it back into a tuple'''
theTupleList = list(theTuple);

theTupleList[2] = 99;

theTuple = tuple(theTupleList);
print(theTuple);

sizeTuple = len(theTuple);

print("The size of our tuple is: ", sizeTuple);




'''
    Lets make a Map(Dictionary),
    Every element will have a key and then a value
'''

myMap = {"cat": "mrCat",
         "dog": "myDog"}

# print everything in our map
print(myMap);

# Access a specific value
print(myMap["dog"]);


# Note that we use elif, and note colon symbol
age = -2;

if(age >= 16):
    print("YOU can drive");
elif(age >= 21):
    print("You can drink");
else:
    print("Marco");
    print("Car");


''' How do we work with for loops, we will not include 10 '''
for x in range(1,10):
    print(x , ' ');

print("\n\n");
''' Let print an array using a for loop'''
theArray = [6,5,4,3,2];
for m in range(0,5):
    print(theArray[m], " ");


'''For each loop'''
i = 0;

for y in myMap:
    print("Item: ", y, " Value = ", myMap[y])
    i += 1;


print(i);

'''Lets work with a while loop 
    This random value will get us a random element: [0, 19]
'''
randNum = random.randrange(0,20);

while(randNum != 10):
    print(randNum)
    randNum = random.randrange(0,20);

print("\nWe now have that the randNum equals to: ", randNum, "\n\n");


'''Lets work with functions'''

def add(numOne, numTwo):
    sumNum = numOne + numTwo;
    return sumNum;

print(add(2,3));


'''How do we get input from the user'''
print("What is your name: ")

name = sys.stdin.readline();

print("\n\n",name);

'''File I/O

Lets begin by writing to a file, file mode should be 'wb'    '''

myFile = open("Testing.txt", "wb")
print(myFile.name)

myFile.write(bytes("I am now writing into the file, yay\n", 'UTF-8'))

myFile.close()


'''We are done with writing to a file
we will now read the text file'''

myReader = open("Testing.txt", "r+")

myReaderText = myReader.read()

print(myReaderText)

myReader.close()

# Dealing with the print and percentages
print("Today was a %s day and I scored %d points and won $%.2f" % ("Happy", 10, 22.45453))

myName = "Marco"
flag = True
# Note that we can also print using format and curly braces
print("Hello, {} are you hungry: {}".format(myName, flag))

















