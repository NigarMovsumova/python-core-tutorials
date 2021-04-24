# number = int(input('Enter the number between 1 and 20: '))
# index = 1
# while index < number:
#     if index < 10:
#         print(index, 'is less than 10')
#     elif index == 10:
#         print(index, 'is equal to 10')
#     else:
#         print(index, 'is more than 10')
#     index += 1

# 1-20 aralığında hər bir ədəd yoxlanılır, 2-yə, 3-ə, 5-ə tam bölünürmü

# index = 1
#
# while index <= 20:
#     is_divisible = False
#     result = 'index = ' + str(index) + ' is exactly divisible by '
#     if index % 2 == 0:
#         is_divisible = True
#         result += '2 '
#     if index % 3 == 0:
#         is_divisible = True
#         result += '3 '
#     if index % 5 == 0:
#         is_divisible = True
#         result += '5 '
#     if not is_divisible:
#         result += 'None'
#     # if is_divisible == False:
#     #     result += 'None'
#     print(result)
#     index += 1

# Найти сумму чисел, которые делятся на 2, 3, 5 от 1 до 100
# index = 1
# divisible_by_2_sum = 0
# divisible_by_3_sum = 0
# divisible_by_5_sum = 0
# while index <= 10:
#     if index % 2 == 0:
#         # divisible_by_2_sum = divisible_by_2_sum + index
#         divisible_by_2_sum += index
#     if index % 3 == 0:
#         divisible_by_3_sum += index
#     if index % 5 == 0:
#         divisible_by_5_sum += index
#     index += 1
#
# print('sum of numbers, divisible by 2 = ', divisible_by_2_sum)
# print('sum of numbers, divisible by 3 = ', divisible_by_3_sum)
# print('sum of numbers, divisible by 5 = ', divisible_by_5_sum)

# Найти произведение чисел, которые делятся на 2, 3, 5 от 1 до 100
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# 2, 3, 4, 5, 6, 8, 9, 10 = 120
# 2, 4, 6, 8, 10

# 2, 3, 4, 5, 6, 8, 9, 10 = 518400
# product = 1
# index = 1
# while index <= 10:
#     if index % 2 == 0 or index % 3 == 0 or index % 5 == 0:
#         product = product * index
#     index += 1
# print(product)

# while <условие> :
#        <список операций>

# index = ?
# while index <=> ? :
#        <список операций>
#        index += ?


# index = 0
# while index < 10:
#     if index == 5:
#         break
#     print('hi')
#     index += 1

# Пользователь вводит минимум и максимум. В этой границе найти числа, которые делятся на 3.
# minimum = int(input('enter minimum:'))
# maximum = int(input('enter maximum:'))
# index = minimum
# while index <= maximum:
#     if index % 3 == 0:
#         print(index)
#     index += 1

# Пользователь вводит минимум и максимум. В этой границе найти числа, квадрат которых меньше 25
# minimum = int(input('enter minimum:'))
# maximum = int(input('enter maximum:'))
# index = minimum
# while index <= maximum:
#     if index * index <= 25:
#         print(index)
#     index += 1

# Пользователь вводит
# 1. максимум - 3
# 2. число - 34
# В границе от 1 до максимума нужно делить число на все числа.
# maximum = int(input('enter maximum:'))
# number = int(input('enter the divided number:'))
# index = 1
# while index <= maximum:
#     number = number / index
#     index += 1
# print(number)
