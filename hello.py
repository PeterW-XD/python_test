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
# returns False because x is not the same object as y, 
# even if they have the same content
thistuple = ("apple",)
print(type(thistuple))
# Receive a tuple
def my_function(*kids):
  print(kids)
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
#receive a dictionary
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")
# None-local
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

# When importing using from keyword, do not use the module name when referring to the module

with open('text.txt', 'r') as file:
  lower_bits_lines = file.readlines() # return a list
for i in lower_bits_lines:
  print(i.strip()) # Remove any whitespace


name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
# using zip() to map values
mapped = zip(name, roll_no) # zip type
print(type(mapped))

# iterate
l1 = ["eat", "sleep", "repeat"]
# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)
for count, ele in enumerate(l1):
    print(count)
    print(ele)

squares = [x**2 for x in range(10)]
print(squares)