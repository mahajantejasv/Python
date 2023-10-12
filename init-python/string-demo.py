# Python Program for  
# Creation of String  
     
# String with single quotes   
print('Welcome to the Geeks World')
     
# String with double quotes  
print("I'm a Geek")

print("'I'm a Geek'")
     
# String with triple quotes
print('''I'm a Geek and I live in a world of "Geeks"''')

# Python Program to Access  
# characters of String  
     
String1 = "GeeksForGeeks"
     
# Printing First character 
print(String1[0])  
     
# Printing Last character 
print(String1[-1])  

# Python Program to Update / delete  
# character of a String  
     
# String2 = "Hello, I'm a Geek"
     
# # Updating a character
# String2[2] = 'p'
   
# # Deleting a character   
# del String2[2]



# Python program to demonstrate
# string slicing
 
# String slicing
String = 'ASTRING'
 
# Using slice constructor
s1 = slice(3)
s2 = slice(1, 5, 2)
s3 = slice(-1, -12, -2)
 
print("String slicing")
print(String[s1])
print(String[s2])
print(String[s3])

# arr[start:stop]         # items start through stop-1
# arr[start:]             # items start through the rest of the array
# arr[:stop]              # items from the beginning through stop-1
# arr[:]                  # a copy of the whole array
# arr[start:stop:step]    # start through not past stop, by step


# Python program to demonstrate
# string slicing
 
# String slicing
String = 'GEEKSFORGEEKS'
 
# Using indexing sequence
print(String[:3])

# Python program to demonstrate
# string slicing
 
# Using indexing sequence
print(String[1:5:2])

# Prints string in reverse
print(String[::-1])

# String Interpolation
# String Interpolation is the process of substituting values of variables into placeholders in a string

n1 = 'Hello'
n2 = 'GeeksforGeeks'
 
# for single substitution
print("Welcome to % s" % n2)
 
# for single and multiple substitutions()
# mandatory
print("% s ! This is % s." % (n1, n2))

n1 = 'Hello'
n2 = 'GeeksforGeeks'
 
# for single substitution
print('{}, {}'.format(n1, n2))


n1 = "Hello"
n2 = "GeeksForGeeks"
 
# for single or multiple substitutions
# let's say b1 and b2 are formal parameters
# and n1 and n2 are actual parameters
print("{b1}! This is {b2}.".format(b1=n1, b2=n2))
 
# we can also change the order of the
# variables in the string without changing
# the parameters of format function
print("{b2}! This is {b1}.".format(b1=n1, b2=n2))

n1 = 'Hello'
n2 = 'GeeksforGeeks'
 
# f tells Python to restore the value of two
# string variable name and program inside braces {}
print(f"{n1}! This is {n2}")


a = 2
b = 3
c = 10
 
print(f"({a} * {b})-{c} = {(2 * 3)-10}")

