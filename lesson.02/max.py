# Пользователь вводит 2 цифры
# Программа выводит максимум из них

# 1. cifra1, cifra2  - inte cevirmek lazimdir 2, 5
# 2. esli cifra1 bolshe cifra2 - > cifra1 2 > 5 ?
# 3. esli cifra1 menshe cifra2 - > cifra2 2 < 5 ? 5
# 4. esli cifra1 ravno cifra2 - > cifri ravni 2 == 5 ?

first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))
if first_number > second_number:
    print(first_number)
elif first_number < second_number:
    print(second_number)
else:
    print('Numbers are equal')

