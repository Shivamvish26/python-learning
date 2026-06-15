x = 1
# int
y = 1.3
# float
z = 1j
# complex

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

# convert the above number
a = float(x)
print(a)
# 1.0

b = int(1.3)
# Jab float ko int() me convert karte hain, to Python decimal part ko hata deta hai (round nahi karta).
print(b)

c = complex(x)
print(c)