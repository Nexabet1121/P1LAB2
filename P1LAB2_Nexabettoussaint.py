# In-class examples of math equations

# Import library for the programm
import random


"""
side1 = float(input("Enter value for side 1; "))
side2 = float(input("Enter value for side 2; "))
"""



# Generate random values for side1 and side2
side1 = random.randint(1,100)
side2 = random.randint(1,10)

# calculate hypotenuse
hypotenuse = (side1 ** 2) + (side2 ** 2)

# Displlay results to the user
print(f"the hypotenuse of a triangle with the sides {side1} and {side2} is {hypotenuse} ")
