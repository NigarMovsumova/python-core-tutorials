# numbers = [23, 43, 56, 76, 76, 12, -9]
# number = 76
# flag = False
# for i in numbers:
#     if i == number:
#         flag = True
#         break
# print(flag)

# print(76 in numbers)
# print(37 in numbers)
# print(True in numbers)
# print('tea' in numbers)

# numbers_sum = 0
# for number in numbers:
#     numbers_sum += number
# print(numbers_sum)
#
# print(sum(numbers))
# print(min(numbers))
# print(max(numbers))
# numbers = [23, 43, 56, 76, 76, 12, -9]
#
# max_number = numbers[0]
# max_number_index = 0
# for i in range(1, len(numbers)):
#     if numbers[i] > max_number:
#         max_number_index = i
#         max_number = numbers[i]
#
# print(max_number)
# print(max_number_index)

# for i in numbers:
#     print(i)
#
# for number in numbers:
#     print(number)

# print(87)
# print([87, 87, 78])

# Найти минимум массива
# numbers = [-90, 23, 43, 56, -90, 76, 76, 12, -9]
# max_number = numbers[0]
# max_number_index = 0
# min_number = numbers[0]
# for i in range(1, len(numbers)):
#     if numbers[i] > max_number:
#         max_number_index = i
#         max_number = numbers[i]
#     elif numbers[i] < min_number:
#         min_number = numbers[i]
#
# print(max_number)
# print(min_number)

# Найти текущую сумму списка.
# https://leetcode.com/problems/running-sum-of-1d-array/

# numbers = [-90, 23, 43, 56, -90, 76, 76, 12, -9]
#
# sum_list = [-90]
# for i in range(1, len(numbers)):
#     sum_list.append(numbers[i] + numbers[i-1])
# print(sum_list)

# numbers = [-90, 23, 43, 56, -90, 76, 76, 12, -9]
# for i in range(1, len(numbers)):
#     numbers[i] = numbers[i] + numbers[i - 1]
# print(numbers)

# Найти второй максимум списка
# Найти третий максимум списка

# numbers = [-90, 23, 43, 56, -90, 76, 76, 12, -9]
# max_num = numbers[0]
# second_max = numbers[0]
# third_max = numbers[0]
# for i in range(1, len(numbers)):
#     if max_num < numbers[i]:
#         third_max = second_max
#         second_max = max_num
#         max_num = numbers[i]
# print(max_num)
# print(second_max)
# print(third_max)

first = 4
second = 5
# tmp = second
# second = first
# first = tmp
#
# print(first)
# print(second)

# print(first, second, sep=' ')
# first = first + second  # = 9
# second = first - second  # = 9 - 5 = 4
# first = first - second  # = 9 - 4 = 5
# print(first, second, sep=' ')
