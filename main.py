text = 'hello world first'
print(text)
# Syntext
if 5 > 3:
    print('Five grater then three second')

# Integer variable declaration

x=4
y=5
sum=x+y
print(sum)

#  Variable casting like integer as a int,string as a str, and the float
age = int(22)
string_age = str(22)
float_age = float(33)
print(type(age), type(string_age), float_age) # If you want to chcek which type those are variable 'write' type(var)

# camel case
myNameIs = 'Sanvi Rahman'

# Pascal case
MyGirlFriendName = 'Aria mich'

# Snake case
my_ex_name = 'Juliet Rohms'

# Assign multiple value
# x assign=Cherry
# y assign = Mango
# z assign = jack-fruit
x, y , z = 'Cherry', 'Mango', 'Jack-fruit'
print(x, y , z)
#One Value to Multiple Variables
a = b = c = 'Diamond'
# Simple distructuring list

fruits =['banana', 'apple', 'Malta', 'waterMelon', 'pineapple']
k, l, m, n, o = fruits

#  Global variables can be used by everyone, both inside of functions and outside.
name = 'Mahbub'
def nameFun():
    print('My Name is ' + name)
nameFun()

# Like scope variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Set Globally
def firstFun():
    global ex
    ex = 'Tasnim'

firstFun()

print('She is  '+ ex)

# If you want to new line in your code use backslash n like \n
print("My name is \n Diptoh AL Mahbub")

# If you want to create tab in your code use backslash t like \t

print("Hello \t World in python test")

# If you want to create double qoute in your code use \" text here\"
print("\"Time and tide waite for none\"")

# if you add variable like integer or float do not need plus sign
age = 22
print('I am',age, 'old')

#  Basic Numerical Operations  plus (+) ,Minus (-), Multiple (*) , Division (/), Floor value (//), Modulus (%), Squer or Power (**)
_a = 55
_b = 4
plus = _a + _b
minus = _a - _b
multiple = _a * _b
division = _a / _b
floor_value = _a // _b
modulus = _a % _b
squre_or_power = _a ** _b
print(plus)
print(minus)
print(multiple)
print(division)
print(floor_value)
print(modulus)
print(squre_or_power)





# Get user input
name_ = input("Enter your name : ")
age = input("Enter your age : ")
gpa =float(input("Enter your gpa : "))

print("Name :" + name_)
print("Age :" + age)
print("Gpa :" , gpa)

# Type Casting or convert integer number
physics = int(input("Please enter physics value : "))
chemisty = int(input("Please enter chemisty value : "))
math = int(input("Pleas enter math value : "))
sum = physics + chemisty + math
print(sum)
if gpa> 4.5 and sum <=250:
    print("You are not eligible for admission")
else:"Congratulation you are eligible for admission"

