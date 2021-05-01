# Вывести все числа от 1 до 100
# number = 1
#
# while number <= 100:
#     print(number)
#     number += 1

# for number in range(100, 0, -1):
#     print(number)

# number = 100
# while number >= 1:
#     print(number)
#     number -= 1

# 1. Есть числа от 1 до 1000, нужно проверить какие числа делятся ли оно на 3, 5 и 7 одновременно.
# for number in range(1, 1001):
#     if number % 105 == 0:
#         print(number)
#
#
# for number in range(105, 1001, 105):
#     print(number)

# 2. Есть числа от 1 до 100, нужно находить их сумму до тех пор, пока сумма меньше 100.

# numbers_sum = 0
# for number in range(1, 100):
#     if numbers_sum + number <= 100:
#         numbers_sum = numbers_sum + number
#     else:
#         print('numbers_sum = ', numbers_sum, 'number = ', number)
#         break
#
# print(numbers_sum)

# Пользователь вводит минимум и максимум. В этой границе найти числа, которые делятся на 3.
# minimum = int(input('Enter the min: '))
# maximum = int(input('Enter the max: '))
# for number in range(minimum, maximum):
#     if number % 3 == 0:
#         print(number)


# İstifadəçi tam ədəd daxil edir, bu ədədin qalıqsız bölündüyü
# bütün rəqəmləri ekrana çıxaran proqram yazın.
# number = int(input('Enter the number:'))
# for digit in range(1, number+1):
#     if number % digit == 0:
#         print(digit)

# 4) İstifadəçi ədəd daxil edir,
# bu ədədin rəqəmlərinin artan ardıcıllıqla
# olub olmamasını yoxlayan proqram yazın. (12299 artan ardıcıllıq, 122044 artan ardıcıllıq deyil)

# number = int(input('enter the number: '))
# is_ascending = True
# previous_digit = 10
# while number != 0:
#     digit = number % 10
#     if digit > previous_digit:
#         is_ascending = False
#         break
#     previous_digit = number % 10
#     number = number // 10
#
# print('Ardicilliq artandi ? ', is_ascending)
