'''
File:           Conditionals
Date:           18 April 2025
Project:        Python
Author:         dadarkfather
Dependencies:   none

/(ㄒoㄒ)/~~ I skipped a bunch of stuff to get to here, but now worries ( •̀ ω •́ )✧ I will get to it ASAP....
So, this file, as the name implies, is focused on taking a look at conditions in python because, again... why not
ԅ(¯﹃¯ԅ) Let's go
'''

def conditionals():
    # Here (Python) we use the generic conditional logic operators foung almost every (>, <, <=, >=, !=)
    print("### CONDITIONALS ###")
    x, y = 34, 32
    print(f"Heads up! The following statements use x = {x} & y = {y}example: if x > y print duuhhhhh")
    if x > y:
        print("duuhhhhh")


    # elif is just adding another if condition if others don't meet the requirements so, else if
    # it is adding another if condition before closing the condition off with an else statement
    print("\nelif")
    if x == y:
        print("condition 1(X = Y)")
    elif x > y: print("my goodness (⊙o⊙)... this is what an else if is capable of!") # This is a "short hand" if (just remove indentation)



    # A short hand if statement is referred to as a ternary operation
    print("\nTERNARY OPERATION:\n")
    print(f"the highest is {x}") if x > y else print(f"{y} is the bigger number")
    # the above can be chained by adding a few more else statements

    # We can chain conditions using and, not & or logical operators
    # Apperently, although a rumor... nested if statements exist in these parts
    
    # Naturally, if statements cannot be empty, but if for some reason your idiot self wishes to have one, 
    # use pass keyword to avoid getting an error, example:
    if y < x: pass
    # Short hand (pass if y < x) will result in an error, not allowed

