# İstifadəçi rəqəm daxil edir ( 1dən-9 rəqəmliyə kimi ola bilər).Onun neçə rəqəmdən ibarət
# olduğunu tapın. Maximum 3 dəyişən istifadə edə bilərsiniz.
# Распечатать сумму цифр числа
# Распечатать произведение цифр числа
# Посчитать сумму четных цифр числа
# Распечатать произведение цифр числа, делящихся на 3 без остатка

# number = int(input('enter the number:'))
# count = 0
# digits_sum = 0
# even_digits_sum = 0
# digits_product = 1
# while number != 0:
#     digits_sum = digits_sum + number % 10
#     digits_product = digits_product * (number % 10)
#     count += 1
#     number = number // 10
#
# print('count of digits = ', count)
# print('sum of digits = ', digits_sum)

# 104 // 10 = 10
# 10 % 10 = 0
#
# 10 // 10 = 1
# 1 % 10 = 1
#
# 1 // 10 = 0
#
# 3654 % 10 = 4
# 3654 // 10 = 365
#
# 365 % 10 = 5
# 365 // 10 = 36
#
# 36 % 10 = 6
# 36 // 10 = 3
#
# 3 % 10 = 3
# 3 // 10 = 0

# number = int(input('enter the number:'))
# count = 0
# even_digits_sum = 0
# while number != 0:
#     digit = number % 10
#     if digit % 2 == 0:
#         even_digits_sum = even_digits_sum + digit
#     number = number // 10


number = int(input('enter the number:'))
count = 0
even_digits_product = 1
while number != 0:
    digit = number % 10
    if digit % 3 == 0:
        even_digits_product = even_digits_product * digit
    number = number // 10
print(even_digits_product)


