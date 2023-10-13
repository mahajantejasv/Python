list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    print(num)

for index in list1:
    if index > 5:
        print(index)
        
print([index for index in list1 if index < 5])