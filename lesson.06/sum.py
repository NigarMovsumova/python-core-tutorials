# print((1 + 100)*50)

# index = 1
# numbers_sum = 0
# while index <= 100:
#     numbers_sum = numbers_sum + index
#     index += 1
# print(numbers_sum)

# index = 1
# numbers_sum = 0
# while index <= 100:
#     numbers_sum = numbers_sum + index
#     print(index)
#     index += 1

# От 1 до 100 - только четные прибавить

# index = 2
# numbers_sum = 0
# while index <= 100:
#     numbers_sum = numbers_sum + index
#     index += 2
# print(numbers_sum)

# Пользователь вводит число, нужно посчитать сколько в этом числе цифр
# number = int(input('Enter the number: '))
# digit_counter = 0
# while number != 0:
#     digit_counter = digit_counter + 1
#     number = number // 10
#
# print(digit_counter)

# 1den 100e kimi reqemler var. Onlarin 3-ə, 5-ə, 7-ə bölünüb bölünməməsini (qalıqsız) yoxlayın.
# (Ayrı-ayrı)

# index = 1
# while index <= 100:
#     if index % 3 == 0 or index % 5 == 0 or index % 7 == 0:
#         print(index)
#     index += 1

# Пользователь вводит число, нужно вывести звездочки в этом количестве
# number = int(input('Enter the number: '))
# # print('*' * number)
# index = 1
# while index <= number:
#     print('#')
#     index += 1

# Ədədin üstünü hesablayan proqram yazın
# (istifadəçi iki ədəd daxil edəcək əsas və üst məs. 2 və 3 cavab 8 alınmalıdır)
# num1 = int(input('Enter the first number : '))
# num2 = int(input('Enter the second number : '))
# result = 1
# index = 1
# while index <= num2:
#     result = result * num1
#     index += 1
# print(result)

# Пользователь вводит число, нужно его делить на 10 до тех пор, пока оно не станет = 0
# num = int(input('Enter the number: '))
#
# while num != 0:
#     num = num // 10
# print(num)

# Пользователь вводит количество страниц в книге
# начинает он читать по 1 странице в день и каждый день увеличивает количество страниц на 5
# сколько дней у него займет прочитать эту книгу
# page_count = int(input('Enter count of pages in a book'))
# index = 1
# while page_count <= :


# Пользователь вводит сколько он может класть в банк каждый месяц
# и сколько месяцев он это будет делать
# посчитать сколько у него будет денег в банке в конце срока
# monthly_payment = int(input('Enter the monthly payment: '))
# months_count = int(input('Enter count of months:'))
# index = 1
# monthly_payment * months_count


# Пользователю нужно вывести номера месяцев года

# index = 1
# while index <= 12:
#     print(index)
#     index += 1

# İstifadəçinin daxil etdiyi aralıqda (məs 10 və 30)
# cüt rəqəmləri ekrana çıxarın.
# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter the second number: '))
# while num1 <= num2:
#     if num1 % 2 == 0:
#         print(num1)
#     num1 += 1

# İstifadəçinin daxil etdiyi aralıqda (məs 10 və 30)
# tək rəqəmləri ekrana çıxarın.
# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter the second number: '))
# while num1 <= num2:
#     if num1 % 2 != 0:
#         print(num1)
#     num1 += 1

# Пользователь вводит верхнюю и нижнюю границы, нужно вывести все числа
# и рядом указать оно четное или нечетное

# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter the second number: '))
# while num1 <= num2:
#     if num1 % 2 == 0:
#         print(num1, ' is even')
#     else:
#         print(num1, 'is odd')
#     num1 += 1

# Пользователь вводит верхнюю и нижнюю границы, нужно вывести все четные числа
# и сумму нечетных чисел в конце
# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter the second number: '))
# odd_sum = 0
# while num1 <= num2:
#     if num1 % 2 == 0:
#         print(num1)
#     else:
#         odd_sum = odd_sum + num1
#     num1 += 1
# print(odd_sum)

# Пользователь вводит верхнюю и нижнюю границы, нужно вывести произведение четных чисел
# и сумму нечетных чисел в конце

# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter the second number: '))
# # num1 = 5
# # num2 = 10
# odd_sum = 0
# even_product = 1
# while num1 <= num2: # false
#     if num1 % 2 == 0: # true
#         even_product = even_product * num1 # even_product = 48 * 10 = 480
#     else:
#         odd_sum = odd_sum + num1 # odd_sum = 12 + 9 = 21
#     num1 = num1 + 1 # num1 = 11
#
# print(odd_sum)
# print(even_product)
