# 1.Create a variable named name and store your name in it. Print the variable.
name = "Shivam"
print(name)
# Shivam

# 2.Create three variables: city, age, salary Store appropriate values and print them.
city = "Pune"
age = 23
salary = 10000
print("I Live in", city)
print("My age is :", age)
print("I earn :", salary)

# 3.Swap the values of two variables:
a = 10
b = 20

a, b = b, a
print("a :", a)
print("b :", b)
# a : 20
# b : 10

# 4.Create variables with the following values: 25 25.5 "Python" True Print the type of each variable.
c = 25
d = 25.5
e = "Python"
f = True

print(type(c))
# <class 'int'>
print(type(d))
# <class 'float'>
print(type(e))
# <class 'str>
print(type(f))
# <class 'bool>

# 5.Predict the output
x = "100"
y = 100

print(type(x))
# <class 'str'>
print(type(y))
# <class 'int'>

#  6.what will be the output
a = 1j
print(type(a))
# <class 'complex'>

# 7.Write a program to add two numbers.
a = 10
b = 20
c = a + b
print(c)
# 30

# 8. Write a program to find: Addition, Subtraction, Multiplication, Division for two numbers.
# take the above example
d = a - b
print(d)
# -10
e = a * b
print(e)
# 200
f = a / b
print(f)
# 0.5

# 9. Predict the output
print(10/2)
# 5.0
print(10//2)
# 5

# 10. predict the output
print(5 % 2)
# 1

# 11. convert the following string into integer
h = "50"
j = int(h)
print(type(j))

# 12. Convert it into string
k = 30
l = str(k)
print(type(l))

# 13. Predict the output
print(int(5.99))
# 5

# 14. Predict the ouput
print(float(10))
# 10.0

# 15. What will happen
# print(int('abc'))
# it will give an error

# 16. Create a string using a indexing
name = "Shivam"
print(name[0])
print(name[-1])

# 17. Using Negative indexing print
print(name[-1:-7:-1]) 
# 

# 18. Predict the output
print(name[1:4])
# hiv

# 19. Predic the output
print(name[::-1])  #[start:stop:step] this is the negative indexing for slicing reversing the string
# mavihs

# 20. Check whether "VAM" is present in name or not
if "vam" in name:
    print("Vam is present in Shivam")
else:
    print("Vam is not present in Shivam")    

# vam is present in Shivam

# 21. Convert the string in upper case
txt = "Python"
print(txt.upper())
# PYTHON

# 22. count how many times apple appears
txt1 = " apple apple mango apple"
print(txt1.count("apple"))
# 3

# 23. Predict the output
txt2 = "Hello World"
print(txt2[-5:-2])
# Wor

# 24. Predict the output
print(bool("Hello"))
# True

# 25. Predict the output
print(bool(""))
# False

# 26. Predict the the output
print(bool(100))
# True

# 27. Predict the output
print(bool(0))
# False

# 28. write an if-else statment
name2 = ""

if name2 == "":
    print("Name is empty")
else:
    print("Name is Present") 
# Name is empty

# 29. predict the output
x = "25"
y = "5"
print (x + y)
# 255

# 30. Predict the output
x = "25"
y = 5
print(int(x)+y)
# 30

# 31. predict the output
name3 = "Python"
print(len(name3))
# 6

# 32. without using len() print the last char of
print(name3[-1])

# String and number can operate together wuth the *
A,B=2,3
Txt_2="@"
print(2*Txt_2*3)
# @@@@@@

# String and stringcan operate with the help of +
C,D="2",3
Text_3="@"
print((C+Text_3)*3)
# 2@2@2@