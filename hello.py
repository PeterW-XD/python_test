# This is a test file
x, y, z = 1, 2, 3
print(x,y,z)
print(x+y+z)
one=two=three=90
print(two)
# List
x = ['a ', 'b', 'c']
print(x)
x, y, z = x
print(x,y,z)
print(x+y+z)
x=range(5)
print(type(x))
x = b"Hello"
# List, Tuple, Set
x = 1j
print(x*x)
import random
print(random.randrange(1, 10))
print('He is called "Johnny"')
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a[0:4])
print(a[-1])
for x in "test":
    print(x)
age = 36
txt = f"my age is {age}"
print(txt)
#modifier :.2f  with 2 decimals
txt = f"my age is {age:.2f}"
print(f"my age is {age:.2f}")
x="hello"
y=10
#print(x+y)
print(2<<2)
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content