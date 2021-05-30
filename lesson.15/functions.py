# print('')
# max([1, 3])
# [1, 3].sort()
# [1, 3].reverse()
# [1, 3].append(3)
# len('test')


# def count_number_occurrences(number, numbers):
#     counter = 0
#     for num in numbers:
#         if number == num:
#             counter += 1
#
#     print(counter)
#
#
# number = int(input('Enter the searched number: '))
# numbers = [1, 2, 1, 1, 3, 5]
# count_number_occurrences(number, numbers)
#
# new_numbers = [1, 2, 4, 6, 6]
# new_number = int(input('Enter the new number: '))
# count_number_occurrences(new_number, new_numbers)


# Calculator
# +/-/*//

# calculate - first_num, second_num, operation = +-*/
# print result

def calculate(numbers):
    for i in range(0, len(numbers) // 2):
        tmp = numbers[i]
        numbers[i] = numbers[len(numbers) - 1 - i]
        numbers[len(numbers) - 1 - i] = tmp
    print(numbers)


numbers = [0, 12, 32, -45, 65, 7, 23, 1, 6, 7]

calculate(numbers)
