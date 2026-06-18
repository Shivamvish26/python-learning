# Boolean values represent the value for the two that is True and False.

print(10 > 9)
# True

print (10 == 9)
# False

print(10 < 9)
# false


# Conditional testing the boolean value
a = 200
b = 100

if b > a:
    print("b is greater than a")
else:
    print("b is not grater then a")
# b is not greater than a


# Evaluate the value and variables
print(bool("Hello")) 
# True
print(bool(15))
# True

#  Some values are false
print(bool(""))
print(bool(0))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(None))
# sab ka value false hoga

x = "Hello"
y = 12

print(bool(x))
print(bool(y))
# True

# Note
'''
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

'''

class myClass():
    def __len__(self):
        return 0
myObject = myClass()
print(bool(myObject))
# False


# Function can return a Boolean
def myFunction():
    return True
print(myFunction())
# True

# isinstance() method
x = 200
print(isinstance(x, int))
# True

y = 200
print(isinstance(y, str))
# False