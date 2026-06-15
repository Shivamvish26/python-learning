# Strings
print ("Hello World")
# Hello World

# quote insude quote
print("Hello this is 'Shubham'")
# Hello this is 'shubham

# Assign a string as an variable
a = "Hello World"
print(a)
# Hello World

# Multileline string
b = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua
"""
print(b)

# String as an array
a = "Hello World"
print(a[1])
# e

# Looping through the strings
for x in "banana":
    print(x)

# String length 
a = "Hello, World"
print(len(a))

# check the string pharse or char is present in string or not

b = "The best thing of nature is air is free"
print("free" in b)
# Passes the boolean value for it i.e is true and false
# the output for it is True

c = "Shivam"
if "vam" in c:
    print("Text Found")
else:
    print("Text not Found")    

# Text Found ye output hoga kyu ki name ke andhar vam present hai

age = 22

if age > 18:
    print("Adult")
elif age == 18:
    print("Just Adult")
else:
    print("Minor")     
# Adult   