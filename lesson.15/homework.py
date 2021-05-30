# 5. Ölçüsü 9 olan massiv yaradın.
#  Massivdəki rəqəmlərin yerlərini tərsinə çevirən program
# yazın. (0-cı indeksi 9-la, 1-i 8-lə və s.)
# [0, 12, 32, -45, 65, 7, 23, 1, 6]
# [6, 1, 23, 7, 65, -45, 32, 12, 0]

# 0 - 8
# 1 - 7
# 2 - 6
# 3 - 5
# 4 - 4 (9 // 2) нужно остановиться на 4ом индексе
# индекс элемента слева будет расти, а справа уменьшаться

# numbers = [0, 12, 32, -45, 65, 7, 23, 1, 6, 7]
#
# for i in range(0, len(numbers) // 2):
#     # print(numbers[i])
#     # print(numbers[len(numbers) - 1 - i])
#     tmp = numbers[i]
#     numbers[i] = numbers[len(numbers) - 1 - i]
#     numbers[len(numbers) - 1 - i] = tmp
#     # print('\n')
#
# print(numbers)

# 2. reqemi istifadechi daxil edir. siyahida neche defe rast gelinirse onu tapmaq gerekir
# [1, 2, 1, 1, 3, 4]
# 1. - 3
# 2 - 1
# 23 - 0

# number = int(input('Enter the searched number: '))
# numbers = [1, 2, 1, 1, 3, 4]

# counter - 0
# esli number == 1: to counter uvelicivaem na 1
# esli number == 2: to counter uvelicivaem na 1 ...
#

# counter = 0
#
# for num in numbers:
#     if number == num:
#         counter += 1
#
# print(counter)
# print('Number of occurences of {} in {} = {}'.format(number, numbers, counter))


# 3. Проверить элементы списка расположены в порядке убывания или нет.
# [87, 85, 3, -10] - True
# [78, 56, 67] - False

# esli predidushiy element >= sleduyuweqo, to idem sleduyuwie proveraem
# v inom sluchae - break, False
# numbers[i], numbers[i + 1]

# 0. flag = True
# 1. proytis po massivu - for (0, len(numbers) - 1)
# 2. esli numbers[i] < numbers[i+1] - flag = False, break
# [87, 87, 85, 3, -10]
# 87 < 87 ? -
# 87 < 85 ? -
# ...
# 3 < -10 ? -

# [78, 56, 67]
# 78 < 56 ? -
# 56 < 67 ? + flag = False, break

# numbers = [78, 56, 89]
# flag = True
#
# for i in range(0, len(numbers) - 1):
#     if numbers[i] < numbers[i+1]:
#         flag = False
#         break
#
# print(flag)






