# in python we know that we can't combine the text and the number.
# But we can combine string and the number with the help of f-string() method

# F-strings
# example
a = 36
b = f"This is my age,{a}"
print(b)


# modifer is inclded by adding the colon : followed by the legal  formatting type like .2f which means the decimal points are also included.

price = 59
c = f"the price of the burger is {price:.2f} ruppes"
print(c)

# the value is 59 only it will carry out the output as 59.00 and if the decimal points is there like 50.90 the out will be 59.90 only the number will be
# added in the .2f

txt = f"The price is {20 * 30}"
print(txt)
# we cam multiply, add and so on.