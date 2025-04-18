'''
File:           Operators
Author:         dadarkfather
Date:           18 April 2025
Dependencies:   none

Just a dive into learning python operators and stuff, been a breeze so far, lets hope it continues this way
'''

def pythonOperators():
    print("### A LOOK INTO OPERATORS W/ PYTHON ###\n")
    # Python operators are divided into the following
    # Arithmetic operators
    # Assignment operators
    # Comparison operators
    # Logical operators
    # Identity operators
    # Membership operators
    # Bitwise operators



    # Arithmetic operators are the same, except for 2
    # Exponetial operator
    x , y = 2, 4
    print(f"{x} to the power of {y} = {x ** y}") # Answer 4^2 = 16

    # Floor division: what the heck is floor division anyway???
    print(f"The floor division of {x} by {y} is: {x // y}") # Answer: I don't know /(ㄒoㄒ)/~~



    # ASSIGNMENT OPERATORS: There's a whole bunch of new ones this time around
    # includes **= & //= as seen above
    print(f"THE FOLLOWING OPERATE ON x = {x} & y={y}\n")
    # Interesting, the following are listed as some of the assignment operators but I am having errors with them
    # A deeper look is necessary here
    # &=, |=, ^=, >>=, <<=
    print("What even is this: ", x := 3) # Answer: 3!? Like how????



    # Comparison operators are the same as everywhere else I suppose



    # Logical operators are not, and & or as seen in previous stuff yk



    # Identity operators include is & is not
    # Membership operators... As in the name would include in & not in
    


    # Bitwise operators: Are used to compare binary numbers they are as follows
    # & = AND, | = OR, ^ = XOR, ~ = NOT, << = zero fill shift left and >> zero fill shift right
    # These are the same as the ones I was getting errors for in the above assignment operators section
    # It is because these only work with binary numbers whereas I was trying to work them in int


    # Operator Presedence: Referres to the order in which operators are executed, there is a whole table for this btw
    # A look of order of presedence, top = highest presedence, below = lower presedence
    print("\nOPERATOR PRESEDENCE:")
    '''
    ()	Parentheses	
    **	Exponentiation	
    +x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
    *  /  //  %	Multiplication, division, floor division, and modulus	
    +  -	Addition and subtraction	
    <<  >>	Bitwise left and right shifts	
    &	Bitwise AND	
    ^	Bitwise XOR	
    |	Bitwise OR	
    ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
    not	Logical NOT	
    and	AND	
    or	OR
     '''
    # If there is operators of the same presedence, expression is executed left to right
    print("Same presedence: ", 4 + 8 - 2) # + & - have the same presedence, so answer = 10

    