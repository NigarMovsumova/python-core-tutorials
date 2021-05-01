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
for number in range(1, 1001):
    if number % 105 == 0:
        print(number)


for number in range(105, 1001, 105):
    print(number)

# 2. Есть числа от 1 до 100, нужно находить их сумму до тех пор, пока сумма меньше 100.

