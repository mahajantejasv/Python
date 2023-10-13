# Inside of the class we currently just have pass. But we can define class attributes and methods.

# An attribute is a characteristic of an object. A method is an operation we can perform with the object.
class Sample:
    # constructor 1st param is always self (like 'this' keyword)
    # we can write only one constructor at a time
    # def __init__(self):
    #     print('Hellow World')

    def __init__(self, value):
        self.value = value
    
# Sample()
instannce = Sample(value = 'This is a value field')
print(instannce.value)





class Dog:
    def __init__(self,breed):
        self.breed = breed
        
sam = Dog(breed='Lab')
print(sam.breed)
frank = Dog(breed='Huskie')
print(frank.breed)



class Animal:
    def __init__(self):
        print('Animal no arg constructor')

    def __init__(self, type, name):
        self.type = type
        self.name = name
    
    def details(self):
        print('my name is {} and I am of type {}'.format(self.name, self.type))


dog = Animal('dog', 'guddi')
dog.details()


