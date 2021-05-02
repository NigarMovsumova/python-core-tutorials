# 1) Istifadəçi 5 rəqəmli ədəd daxil edir. Ədədin polindrom olub olmamasını təyin edin. (Polindrom
# - əksinə və düzünə eyni cür oxunur 12321 polindromdur, 12345 polindrom deyil)

number = int(input('Enter the number: '))
if number % 10 == number // 10000 and (number % 100) // 10 == (number // 1000) % 10:
    print('palindrom? ', True)
else:
    print('palindrom?', False)

# 1. Сравнить последнюю и первую цифру
# 2. Сравнить вторую и четвертую цифру

# 1.
# number % 10 - последняя цифра
# number // 10000 - первая цифра
# сравниваем - если последняя цифра == первой цифре. то тру

# 2.
# number % 100 // 10 - предпоследняя цифра
# number // 1000 % 10 - - вторая цифра
# сравниваем - если предпоследняя цифра == второй цифре. то тру

