
                           # The program to get the Cube_root and Square_root.
                           # ________________________________________________
                           
  
# Exponential Method

num=int(input("Enter a Number:"))
sr=num**(1/3)
print("The Cube_root of the given Number!",sr)


# Math Module:
import math
num1=int(input("Enter a Number:")) #sqrt is a function to get the square_root of any function,but first we have to import the module(math),where, math---->is a module name.
sr1=math.sqrt(num1) 
print("The Square_root of the given Number!",sr1)