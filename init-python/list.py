
# Python program to demonstrate   
# Creation of List   
     
# Creating a List  
List = []  
print(List)  
     
# Creating a list of strings
List = ['GeeksForGeeks', 'Geeks']
print(List)  
     
# Creating a Multi-Dimensional List  
List = [['Geeks', 'For'], ['Geeks']]  
print(List)


# Python program to demonstrate   
# Addition of elements in a List  
     
# Creating a List  
List = []
     
# Using append()
List.append(1)  
List.append(2)
print(List)  
   
# Using insert()
List.insert(3, 12)  
List.insert(0, 'Geeks')
List.insert(5, '5th Value')
print(List)  
   
# Using extend()  
List.extend([8, 'Geeks', 'Always'])  
print(List)


# Python program to demonstrate   
# Removal of elements in a List  
     
# Creating a List  
List = [1, 2, 3, 4, 5, 6,   
        7, 8, 9, 10, 11, 12]
 
# using Remove() method  
List.remove(5)  
List.remove(6)
print(List)  
   
# using pop()
List.pop()
print(List)  


# Python program to demonstrate   
# accessing of element from list  
     
 
List = [1, 2, 3, 4, 5, 6]  
     
# accessing a element
print(List[0])   
print(List[2])  
   
# Negative indexing
# print the last element of list  
print(List[-1])
# print the third last element of list   
print(List[-3])
# print reverse order list
print(List[::-1])

# Let us first create a list to demonstrate slicing
# lst contains all number from 1 to 10
lst =list(range(1, 11))
print (lst)
	
# below list has numbers from 2 to 5
lst1_5 = lst[1 : 5]
print (lst1_5)
	
# below list has numbers from 6 to 8
lst5_8 = lst[5 : 8]
print (lst5_8)
	
# below list has numbers from 2 to 10
lst1_ = lst[1 : ]
print (lst1_)
	
# below list has numbers from 1 to 5
lst_5 = lst[: 5]
print (lst_5)
	
# below list has numbers from 2 to 8 in step 2
lst1_8_2 = lst[1 : 8 : 2]
print (lst1_8_2)
	
# below list has numbers from 10 to 1
lst_rev = lst[ : : -1]
print (lst_rev)
	
# below list has numbers from 10 to 6 in step 2
lst_rev_9_5_2 = lst[9 : 4 : -2]
print (lst_rev_9_5_2)


# Python program to demonstrate list comprehension in Python

# below list contains square of all odd numbers from
# range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print (odd_square)

# for understanding, above generation is same as,
odd_square = []
for x in range(1, 11):
	if x % 2 == 1:
		odd_square.append(x**2)
print (odd_square)

# below list contains power of 2 from 1 to 8
power_of_2 = [2 ** x for x in range(1, 9)]
print (power_of_2)
#range 1 to 10
lst=[x**2 if x%2==1 else x*2 for x in range(1,11)]
print(lst)

#for understanding ,above "lst" is same as below "lst1"
lst1=[]
for x in range(1,11):
    if x%2 == 1:
        lst1.append(x**2)
    else:
        lst1.append(x*2)
print(lst1)
# below list contains prime and non-prime in range 1 to 50
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print (primes)

# list for lowering the characters
print ([x.lower() for x in ["A","B","C"]] )

# list which extracts number
string = "my phone number is : 11122 !!"

print("\nExtracted digits")
numbers = [x for x in string if x.isdigit()]
print (numbers)

# A list of list for multiplication table
a = 5
table = [[a, b, a * b] for b in range(1, 11)]

print("\nMultiplication Table")
for i in table:
	print (i)


import functools

# filtering odd numbers
lst = filter(lambda x : x % 2 == 1, range(1, 20))
print (list(lst))
	
# filtering odd square which are divisible by 5
lst = filter(lambda x : x % 5 == 0,
	[x ** 2 for x in range(1, 11) if x % 2 == 1])
print (list(lst))
	
# filtering negative numbers
lst = filter((lambda x: x < 0), range(-5,5))
print (list(lst))
	
# implementing max() function, using
print (functools.reduce(lambda a,b: a if (a > b) else b, [7, 12, 45, 100, 15]))

