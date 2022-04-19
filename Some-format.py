# String formate using f""
num1 = 33
num2 = 54
fromat =  f"{num1} + {num2} = {num1+num2}"
print(fromat)

# skip break line or new line
name = 'sanvi rahman age 22'
print(name)

# 19/4/22

# if you using while loop and wanna broke this loop firstle and also can use break method .
i = 1
while i<=100:
    if i==30:
        break
    print('i love python',i)
    i+=1


# second format
i = 1
while i<=100:
    print('i love my country',i)
    i+=1
    if i==50:
        break


# if you using while loop and wanna continue with conditionaly like i==20 then continue this loop firstly and also can use continue method .
i = 1
while i<=100:
    if i==30:
        continue
    print('i love python with continue',i)
    i+=1


# second format
i = 1
while i<=100:
    print('i love my country with continue',i)
    i+=1
    if i==50:
        continue