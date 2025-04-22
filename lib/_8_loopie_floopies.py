'''
File:           Loops (that's what is means... ⊙.☉)
Date:           18 April 2025
Project:        Python
Author:         dadarkfather
Dependencies:   zErO

just a look at while and for loops really, nothing special
'''

def loopiesAndFloopies():
    # There are 2 types of loops in Python, while loops & for loops
    import random # To generate random number to break loop at random number

    print("### A LOOK AT WHILE LOOPS ###")

    # A look at a simple while loop, this is as simple as it can get honestly
    i = int(0)
    name = str("dadarkfather")
    print("\nPrinting all values while var i < 10")
    while i < 10:
        print(f"current iteration: { i + 1} :: i value: {i}")
        i += 1
    
    # BREAK: Using break statement we can break a while loop in certain conditions even if true
    # Future darkfather here (ʘ ͜ʖ ʘ)... again... break makes it so that it seems as if the loop is finished when in actuality it isn't
    randomNumber = int(random.randrange(0, 10))
    print(f"\nUsing random number {randomNumber} to break statement within while loop:\n")
    j = int(0)
    while j < 10:
        print(f"Current iteration: {j + 1} :: Current i value: {j}")
        if j == randomNumber:
            print(f"Breaking at random number {randomNumber}")
            break
        j += 1
    
    # CONTINUE: A look at the continue statement
    # Basically, as stupid as it may seem (￣m￣） it just makes it continue like nothing ever happened
    # HOLD UP Σ(っ °Д °;)っ Future darkfather here (ʘ ͜ʖ ʘ) (a few minutes after typing a above) here's what continue actually does
    # Within a block of code, the continue statement skips ALL code below it and if in a loop will go to beginning of the loop
    # If in a function, it will skip all below code return function... That is why you get infinite loop if skipping counter var
    # in a loop 
    print("\nContinuing at a random iteration")
    randomContinue = int(random.randrange(0, 10))
    k = int(10)
    while k > 0:
        print(f"Current iteration: {k} :: Current value: {k}")
        if k == randomContinue:
            print(f"Continuing at random number k({k}) = randomContinue({randomContinue})")
            # continue: Adding this statement here results in an infinite loop :: Explained above by future darkfather 
        k -= 1

    
    # ESLE : We can run an else statement once loop is no longer true
    l = int(0)
    print("\nUsing else statement after while to do something once loope has completed")
    while l < 10:
        print(f"Current iteration: {l + 1} :: Current value: {l}")
        l += 1
    else:
        print(f"Out of the loop at itereation {l + 1}, value {l}")
       
    # Honestly speaking (*^_^*)... Whats the point, you could have an if or continue statement... but if works in this case




    # FOR LOOPS
    # for loops are used to iterate over something whilst while loop are used to iterate over a given value range 
    # Python for loopies... like everything else in python is different. It works more like an iterator found in other programming
    # languages rather than a an actual for loop
    print("## A LOOK INTO FOR LOOPS")
    print("\nIteration over a truthful list")
    truthfulList = list(["dadarkfather", "is", "the", "best", "don't", "you", "agree"])
    for x in truthfulList:
        print(x)

    # Looping through a string
    theNameOfTheChosenOne = truthfulList[0] # Gives 'dadarkfather'
    print(f"\nIteration over string {theNameOfTheChosenOne}")
    for x in theNameOfTheChosenOne:
        print(x)

    # Break & continue statements works for for loops in the same way as in while loops

    # RANGE: Using range() you can specify numbe of iterations you wanna have
    print("\nA LOOK AT USING RANGE()", f"Printing x in range {range(9)}")
    for x in range(9):
        print(f"x = {x}")

    print(f"printing x in {range(4, 8)}")
    for x in range(4, 8):
        print(f"x = {x}")

    print(f"printing x in {range(0, 18)} in steps of 2")
    for x in range(0, 18, 2):
        print(f"x = {x}")