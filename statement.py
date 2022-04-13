# if else and else if abbreation is elif
mark = 33
if mark >= 33:
    print('You are pass')

mark = 99
if mark > 80:
    print('mark is  good')
else:
    print('you are fail')


# age = int(input('if your age is :'))
_age = 33
if _age < 18:
    print('You are not teenager')
elif _age > 20:
    print('you are young')
else:
    print('You are matured')
# odd and even number check
num = 35
if num%2 == 0:
    print('its even num')
else:
    print('its a odd number')

# Inner if statement
age = 10
age1 = 15
age2 = 18
age3 = 20
if age < age1:
    if age1 < age2:
        if age2 > age3:
            print('You are voter')
        else:
            print('You are not voter')
# Ternary operator
number = 33
Pass = number if number >= 33 else 'she is not pass'
print('she is got', Pass)

# Logical operator

voter = 1
voter1 = 2
voter2 = 3
if voter<voter1 and voter2 > voter1:
    print('You have got 3 vote')

mango = 1
banana = 3

if mango<banana or mango > banana:
    print('You have got 4 fruit')

character = 'a'
if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
    print('Its vowel')
if character != 'b':
    print('Its again also said that its vowel')

# letter grade find
marks = int(40)
if marks >= 80 and marks <= 100:
    print('A+')
elif marks == 70 and marks < 80:
    print('A')
elif marks >= 60 and marks  < 70:
    print('A-')
elif marks >= 50 and marks < 60:
    print('B')
elif marks >= 40 and marks <50:
    print('C')
elif marks >= 33 and marks <40:
    print('D')
else:
    print('You are fail')

