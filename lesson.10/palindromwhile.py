# 1) Istifadəçi tek rəqəmli (7) ədəd daxil edir. Ədədin polindrom olub olmamasını təyin edin.
# (Polindrom - əksinə və düzünə eyni cür oxunur 12321 polindromdur, 12345 polindrom deyil)

number = int(input('Enter the number: '))
# if number % 10 == number // 10000 and (number % 100) // 10 == (number // 1000) % 10:
#     print('palindrom? ', True)
# else:
#     print('palindrom?', False)

# 1. Сравнить последнюю и первую цифру
# 2. Сравнить вторую и четвертую цифру

# 1234321
# 1234321
#
# 1. % 10 // 1
# 2. % 100 // 10
# 3. % 1000 // 100


# digits_count = 7

# 1. // (10 ^ digits_count -1) % 1
# 2. // (10 ^ digits_count -2) % 10
# 3. // (10 ^ digits_count - 3) % 10

# digits_count = 7
# power_counter = 2
# last_digit = number % 10
# first_digit = number // (10 ** (digits_count - 1))
#
# for i in range(0, 2):
#     right_digit = number % (10 ** )



