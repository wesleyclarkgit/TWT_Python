### TWT_Python

# 1

# Variables and Data Types
int 0
str 'Wes', "Wes"
bool True, False (true is not, it is case sensitive)
float 0.32

Declaring a variable
name = 'Wes'
print(name)
variables are case sensitive.  Name =/ name

# Basic Operators and Inputs
name = 'Wes'
print(name)  in this instance, name is the argument
The terms parameter and argument can be used for similar things.  A parameter is the variable listed inside the parentheses in the function definition
An argument is the value that is sent to the function when it is called
def example_function(parameter)
  print(first_name + "last_name")
example_function(Wes, Clark)  <--Wes and Clark are arguments.  first_name and last_name are parameters.  Arguments are automatically separated by spaces

Operators, +, -, /, *
exponents = **
integer division = //
modulo, find the remainder = %

We can cast a type, str(3) = '3'

# Conditions
<, >, ==, !=
In Python the == operator compares the value or equality of two objects, wheras the Python is operator checks whether two variables point to the same object in memory.  Another way to htink about it would be that single equal mark is used to assign a value to a variable, wheras two consecutive equal marks is used to check whether 2 expressions give the same value

# Decisions - if/elif/else
if condition == True:
  do this
  
the 'do this' must be indented properly

else follows an if statement and follows the same syntax

age = input('Input your age: ')

if int(age) >= 16:
  print("hey you're older than 16")
else:
  print("you are younger than 16")
  
height = input()

if int(height) < 1:
  print("you cannot ride, under 4 feet")
elif int(height) >2:
//you can have as many elifs as you want, but only one else.  else is the final closing logical increment
  print('you cannot ride, over 6 feet')
else:
  print('you can ride')
  
# Chained conditionals and nested statements
x = 2
y = 3
if x == y and x + y ==5:
  print("it happened")

if you use and, both conditions must be true.  if you use or, at least 1 must be true
if x == y or x + y ==5:
  print('k it happened freal')
  
not reverses the value
if not(y == x or x + y ==5):
//this evaluates to false, because it would normally evaluate to true, but not changes the value
  print('ran')
else:
  print(':/')
  
Instead of using and/or you could use nested statements
if x ==2:
  if y ==3:
    print('x = 2, y = 3')
  else:
    print('x = 2, y != 3')
else:
  print('x != 2')




