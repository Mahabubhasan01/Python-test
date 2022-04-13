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