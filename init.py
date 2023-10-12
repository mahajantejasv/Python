print("Hello World!!")


# Python program showing 
# indentation 
   
site = 'gfg'
   
if site == 'gfg': 
    print('Logging on to geeksforgeeks...') 
else: 
    print('retype the URL.') 
print('All set !') 

# This is a comment 

""" 
This would be a multiline comment in Python that 
spans several lines and describes geeksforgeeks. 
A Computer Science portal for geeks. It contains  
well written, well thought  
and well-explained computer science  
and programming articles,  
quizzes and more.  
… 
"""
print("GeeksForGeeks") 


#!/usr/bin/python 
   
# An integer assignment 
age = 45                     
   
# A floating point 
salary = 1456.8            
   
# A string   
name = "John"             
   
print(age) 
print(salary) 
print(name)


# Examples of Arithmetic Operator 
a = 9
b = 4
   
# Addition of numbers 
add = a + b 
# Subtraction of numbers  
sub = a - b 
# Multiplication of number  
mul = a * b 
# Division(float) of number  
div1 = a / b 
# Division(floor) of number  
div2 = a // b 
# Modulo of both number 
mod = a % b 
   
# print results 
print(add) 
print(sub) 
print(mul) 
print(div1) 
print(div2) 
print(mod)
# Examples of Relational Operators 
a = 13
b = 33
   
# a > b is False 
print(a > b) 
   
# a < b is True 
print(a < b) 
   
# a == b is False 
print(a == b) 
   
# a != b is True 
print(a != b) 
   
# a >= b is False 
print(a >= b) 
   
# a <= b is True 
print(a <= b)

# Examples of Logical Operator 
a = True
b = False
   
# Print a and b is False 
print(a and b) 
   
# Print a or b is True 
print(a or b) 
   
# Print not a is False 
print(not a) 


# Examples of Bitwise operators 
a = 10
b = 4
   
# Print bitwise AND operation   
print(a & b) 
   
# Print bitwise OR operation 
print(a | b) 
   
# Print bitwise NOT operation  
print(~a) 
   
# print bitwise XOR operation  
print(a ^ b) 
   
# print bitwise right shift operation  
print(a >> 2) 
   
# print bitwise left shift operation  
print(a << 2)


# Examples of Identity and 
# Membership operator
 
 
a1 = 'GeeksforGeeks'
b1 = 'GeeksforGeeks'
 
# Identity operator
print(a1 is not b1)
print(a1 is b1)
 
 
# Identity operator
print( {a : 2} is not {a : 3})
print( {a : 2} is {a : 3})
print( {a : 2} is {a : 2})
 
# Membership operator
print("G" in a1)
print("N" not in b1)

# Python 3.x program showing 
# how to print data on 
# a screen 
   
# One object is passed 
print("GeeksForGeeks") 
   
x = 5
# Two objects are passed 
print("x =", x) 
   
# code for disabling the softspace feature  
print('G', 'F', 'G', sep ='')
print('G', 'F', 'G') 
   
# using end argument 
print("Python", end = '@')   
print("GeeksforGeeks")  


# Python program to  
# demonstrate numeric value 
   
print("Type of a: ", type(5)) 
   
print("\nType of b: ", type(5.0)) 
   
c = 2 + 4j
print("\nType of c: ", type(c))
