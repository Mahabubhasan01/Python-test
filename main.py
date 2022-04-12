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

