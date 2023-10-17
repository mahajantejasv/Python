# range operator
# from random import randint, shuffle


print(range(0,11))

print(list(range(0,11)))

print(list(range(0,11,2)))

print(list(range(0,101,10)))


index_count = 0

for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1

# enumerate operator
for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))

print(list(enumerate('abcde')))

# zip operator
mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']

print(list(zip(mylist1,mylist2)))

for item1, item2 in zip(mylist1,mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))

# membsership operator

print ('x' in ['x','y','z'])

print ('x' not in ['x','y','z'])

# min operator
print(min(mylist1))

# max operator
print(max(mylist1))

# random operator
# mylist = [10,20,30,40,100]

# print(shuffle(mylist))

# print(randint(0,100))

# type operator
print(type(1))
print(type([]))
print(type(()))
print(type({}))


# input opeartor
data = input('Enter Something into this box: ')
print(data)



