# Pyhton has an set of built-in method that you can use a strings.

# all string return the new string values. They do not change the original string

# capitalize()
# It retuen the fist char in upper case and all other on small case
# Letter hai → capitalize hoga.
# Number hai → same rahega.
# Symbol hai → same rahega.

# eg:-
a = "this is my name"
txt = (a.capitalize())
print(txt)
# This is my name

# the first char is number then
b = "36 is my age"
txt_2 = (b.capitalize())
print(txt_2)
# 36 is my age

# casefold method is used to return the string where all the string are in lower case
txt3 ="Hello, and Welcome to my World!"
print(txt3.casefold())
# hello, and welcome to my world

# center method will return align center the string, using the specifice char.
txt4="banana"
print(txt4.center(20))
#        banana       
print(txt4.center(20, "O"))
# OOOOOOObananaOOOOOOO

# count method return how many time string have been repeated
txt5 = "The Apple. An Apple a day keeps the doc away"
print(txt5.count("Apple"))
# 2

# position
txt6 = "I love apple, apple are my favorite fruit"
z = txt6.count("apple", 10, 24)
print(z)
# 1

# The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
# text ko bytes mai convert karta hai yane ki computer language mai
txt7 = "My Name is Shivam"
print(txt7.encode(encoding="ascii",errors="backslashreplace"))
print(txt7.encode(encoding="ascii",errors="backslashreplace"))
print(txt7.encode(encoding="ascii",errors="ignore"))
print(txt7.encode(encoding="ascii",errors="namereplace"))
print(txt7.encode(encoding="ascii",errors="replace"))
print(txt7.encode(encoding="ascii",errors="xmlcharrefreplace"))
# b'My Name is Shivam'

