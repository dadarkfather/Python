'''
File:       Booleans.py
Project:    Python
Author:     dadarkfather
Dependencies:   none

A look into how booleans function in Python programming, should be farely easy ig
'''

# I don't really know why I keep importing this because in truth I still actually don't even know what i does
import sys 

def aLookIntoBooleans():
    # Booleans are the same as we know them to be
    print("## A LOOK INTO BOOLEANS ##")
    print("4<5?", 4<5)
    print("4 == 4?", 4 == 4) # Prints if 4 = 4, Works for all other booleans too

    # The above obviously applies to conditional statements
    if "dadark" not in "dadarkfather":
        print("not there")
    else:
        print("'dadark' is ofcourse in 'dadarkfather'")

    # Using bool() you can evaluate any variable or value
    # Honestly, what even is the point in this? 
    # Answer: In python, almost every variable is true ONLY IF it has a value, if empty, then false
    # Strings, lists, tuples, dictionaries etc are true as long as they are not empty
    # numericals are true if not 0
    # The following are true
    print("The following are all true!!!")
    print("bool('Hello'): ", bool("Hello"))
    age = 40
    print("bool(age): ", age)

    # the following are all false
    x = tuple() # X is an empty tuple
    y = str() # Y is an empty string
    z = int() # z is an empty integer

    print("\nThe following should be false as they are empty")
    print("x? ", bool(x), ", y? ", bool(y), ", z? ", bool(z))



    # Functions typically just do what you want them to do, but they can return a bool as well

    def myQuteBoolFunction():
        print("within function scope of a qute boolean function")
        return True
    
    myQuteBoolFunction()



    # As a bit of a side note ^_^, Python has many functions that return a boolean, like the following
    someRandomInt = 34
    print("Is it an integer? ", isinstance(someRandomInt, int))
    # The above function isInstance, checks whether the given var is an instance of that data type