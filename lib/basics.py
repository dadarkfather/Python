"""
File:           Basics_py
Author:         dadarkfather (119955277+dadarkfather@users.noreply.github.com)
Project:        python
Dependencies:   none

Summary:
    This file contains basic and fundamentals of python all wrapped and contained in functions for easy reading
    and because I come from c++ so thats how I like to do things you know.
""" 

def theBasicStuff():
    import sys

    print("Hello World!"); # Aww, my first python script
    print(sys.version)

    """
    SYNTAX: Checking Python syntax
    """

    # Indentation
    print("Is 5 > 2?")
    if 5 > 2:
        print("Obviously, ofcourse it is")

    ######## USING VARIABLES ######## 
    # There is no commands for creating them, just make one
    # int something = 34 WRONG
    something = 34 # new int var 
    anotherThing = 34.2 # double var type
    name = "A name of something" # String var created
    Name = "The same name as name???" # This is a completely different variable as variable names are case sensitive
    nameAgain = "Another name of something" # Still a string, string use either "" or '' doesn't matter
    # anotherThingAgain(34) WRONG: can't use () to initialize
    # name WRONG: variables can only be created with a value
    sur, na, m = "f", "ar", "ther" # This here witchcraftery is the creation of 3 variables at the same time, initialized contiguously
    x = y = z = "What is going on with python honestly" # This kinda explains itself, all have same value

    # The below is a list or a tuple, I'm not really quite sure myself to be honestly speaking
    cars = ["Delorian", "BMW", "Mazda", "Volkwagen"]
    s, d, a, g = cars # we can unpack the list or whatever it is and assign it into each value and stuff

    c = 4j # Python also includes a data type known as a complex, as in complex numbers
    com = complex(3 + 45j) # Which like other data types can be explicitly declared like so


    print("A list of cars: ", cars, "\n") # printing the list or whatever this is
    print("The best car of them all is: ", s)
    
    # A look at casting
    variableSomething = str(34) # 34 is converted into a string

    # Get type of a var
    print("Value of variableSomething", variableSomething)
    print(type(variableSomething))

    # There is a whole lot of things that you can do with print and variables
    print(s + d + a + " ") # Stuff like this basically you know

    # This is what a function in Python looks like my guy, don't forget the 'def' part.
    def someFunctionIGuess():
        # You can use global variables.
        print("\nGlobal variable in function", cars)
        # You can use varibles within also
        x = "something in here I suppose!"
        print("\nLocal variable in function: ", x)
        # BUT you can declare a variable in here and have it become global through the global keyword
        global newGlobalVar # first you must declare the var then you can use it, this 
        newGlobalVar = "I am global even though I am here"
        print("\nExplicitly defined global variable in function: ", newGlobalVar)

    # Nice, you defined your function now to call it, else newGlobalVar won't be recognized
    someFunctionIGuess()

    print("\nExplicity defined global variable outside of function: ", newGlobalVar)

    print("A look at numbers in python: ", type(3 + 4j))



    import random

    print("A random number because why not: ", random.randrange(0, 10, 2))


def pythonStrings():
    # A look at a multilined string
    mLString = """Hello,
    
    Its not so very nice to meet you.
    okay, thats it.
    
    cool"""

    # The multi lined strings also work with single quotes as well '''
    print(mLString)

    # Strings are arrays
    # A 'char' data type does not exist, but it's equivalent is a string of length 1
    movieName = "Dadarkfather begins"
    print(movieName[1]) # Prints D

    # Looping through a string
    for x in movieName:
        print(x + "\n") # Prints each letter in new line

    #lenght of string
    print(len(movieName))

    # Check / Search string
    print("dadarkfather" in movieName)

    # Conditional expression on string
    if "begins" in movieName:
        print("I believe this is the first movie of an awesome series")
    
    # Check if not the case
    print("rises" not in movieName)

    # Negative conditional expression
    if "continues to dominate" not in movieName: # As in Dadarkfather continues to dominate
        print("It's either the first movie or the last one")
        
        if "rises" not in movieName:
            print("This is definately the first movie for sure, I am sure of it now")
        
    #################### THAT WAS A LOOK AT ONLY THE BASICS OF STRINGS, NOW MOVING ON TO EVEN MORE STRINGS AND STUFF ############
