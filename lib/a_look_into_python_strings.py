'''
File:		A look into python strings because I don't have anything better to do
Author:		dadarkfather ()
Project:	Python
Dependencies:	none

SUMMARY:
	File contains all the basics about and on python strings and their manipulation. Nothing 
	of significant note to be found here honestly.

	Delves deep from the very basics to slicing, modifiying, formatting, Escape Characters, string
	Methods etc...
'''

# I honestly do not know what this import is for tbh?? Check main for explaination
import sys

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




    ################### A LOOK INTO SLICING STRINGS ###################
    # I honestly like how that sounds hehehe, slicing strings, I feel like Jason Vor-something, that gut with the hockey mask and chain saw yk

    print("### A LOOK INTO STRING SLICING ###")

    # Slicing
    # Given a string, specify the start location and end location separated by a colon
    # It is kinda like printing everything between print(greeting[2]) + print(greeting[5])
    # Remember, strings are arrays, so they use indexing beginning at 0
    # Remember, the last string is not included
    greeting = "Hello, dadarkfather"
    print(greeting[2:5]) # Prints llo

    # Exclude start character to start at the first string/char
    print(greeting[:5]) # Prints from benninging till [5]: Hello
    # Same logic applies for printing till end
    print(greeting[5:]) # Prints from 5 till end: , dadarkfather

    ### NEGATIVE INDEXING ###
    # Use negative indexing to print from the end of the string (Will not print in reverse tho)
    print(greeting[-5:-2]) # Prints: ath
    # What is going on in the above exactly???
    # Let me break it down for you dummy, starting from the last character you move 5 (from right to left basically -5) This is the starting position 
    # From the last char, move 2 (from right to left) basically -2. This will be your ending position,




        ################### A LOOK INTO MODIFYING STRINGS ###################

    print("### A LOOK INTO STRING MODIFICATIONS ###\n")

    # UPPER CASE 
    theBest = "is dadarkfather"
    print("To upper case function: ", theBest.upper(), "\n") # Self explanitory

    # LOWER CASE 
    print("To lower case function: ", theBest.lower(), "\n") # You get it

    # Removing whitspaces
    print("Removing whitespaces: ", theBest.strip(), "\n")

    # Replacing Strings/ chars: with this you can replace a char or a string with given string or character
    print("Replacing a string because why not result: ", theBest.replace("is", 'it is him'))

    if 'it is him ' in theBest:
        theBest.replace("it is him", "is ")
        print("Bringing it back to normal: ", theBest)

    # Splitting a string where you wanna
    # Splits at indicated location, returns list
    # The below splits it at any whitespace in the string
    print("Splitting a string result: ", theBest.split(" ")) # Returns ["is", "dadarkfather"]



        ################### A LOOK INTO CONCATENATION OF STRINGS ###################
    # You can use + operator to concatenate strings
    # It's string concatenation as you already know it (*/ω＼*)
    print("I" + " am bored" + "... It's too easy honestly ")


        ################### A LOOK INTO FORMATTING STRINGS ###################

    # print(" uhhhh" + 34) where 34 is not a string is illegal, but can be overcome by using f-strings and/or format() method


    print("\n### A LOOK INTO STRING FORMATTING ###\n")

    # To specify a string as an f-string, put f in front of the string literal and add braces as placeholders for variables and other operations
    awesomenessRating = float(9001) #(⊙_⊙;) I-It's IT'S OVER 9 000 !!!!
    randomDummyAskingQuestion = f"Random dummy: what is dadarkfathers awesomeness rating? Is it below {awesomenessRating - 1}"
    print(randomDummyAskingQuestion)
    # The placeholder can contain anything that isn't a string!
    # You can also modify the results by using a modifier in the placeholder 
    randomDummyAskingQuestion = f"Random dummy: what is dadarkfathers awesomeness rating? Is it below {awesomenessRating - 1: .2f}"
    # The above displays with 2 decimal places

        ################### A LOOK INTO ESCAPE CHARACTERS WITH STRINGS ###################
    # Same as other programming languages really, don't need to think too much about this 

    # You can, like other languages look at the various functions available for string manipulation