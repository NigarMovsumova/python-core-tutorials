students = ['Tale', 'Aslan', 'Namiq', 'Anar', 'Zarina', 'Mehman']
ages = [23, 27, 28, 29, 30]
# for student in students:
#     print(student)
#
# print(students[0])
# print(students[1])
# print(students[4])
# print(students[-1])

# print(students)
# students.append('Nigar')
# print(students)
#
# students[0] = 'Namiq'
# students[2] = 'Tale'
# print(students)

# students.pop()
# students.pop()

# students.append('Aslan')
# print(students)
# students.remove('Aslan')
# print(students)

# students.insert(0, 'Anna')
# students.insert(6, 'Anar')
# students.insert(100, 'Test user')
# students.insert(15, 'Michael')
# students.insert(75, 'Test')
# print(len(students))
# print(students)


# students.sort(reverse=True)
# ages.sort()
# print(students)
# print(ages)

# students.clear()
# print(students)

# *
# students_copy = students.copy()
# students_wrong_copy = students
# students.append('Test')
#
# print(students)
# print(students_copy)
# print(students_wrong_copy)

# 1. Есть список чисел, нужно напечатать только те, что больше 0.
# 2. Есть список чисел, нужно записать в новый список только те, что больше 0.
# 3. Нужно записать в новый список только негативные числа]
# 4. Нужно записать в новый список только 0.
# numbers = [3, 4, 5, 6, -9, 0, -76, 4]
# positive_numbers = []
# negative_numbers = []
# zeros = []
# for number in numbers:
#     if number > 0:
#         # print(number)
#         positive_numbers.append(number)
#     elif number < 0:
#         negative_numbers.append(number)
#     else:
#         zeros.append(number)
#
# print(numbers)
# print(positive_numbers)
# print(negative_numbers)
# print(zeros)


# 3. Siyahida n qeder element var, 100 element olmagina neche element
# chatmir ?

# elements = [1, 2, 3, 4, 6, -10]
# print(100 - len(elements))

# 4.

# cars = ['Lamborghini', 'Toyota', 'Bentley', 'BMW', 'Mersedes', 'Lada Kalina']
# scores = [4.5, 3.7, 4.7, 3, 2.5, -5]
#
# # 1. Если оценка больше 4, то она считается безопасной
# # 2. Если оценка меньше 4, но больше 0, то она не рекомендуется
# # 3. Если оценка меньше 0, то она считается опасной для вождения
# # Название машины + она опасная? безопасная? не рекомендуется ?
#
# for i in range(0, 6):
#     print('index =',  i, ' ', cars[i], ' ',  scores[i])
#     if scores[i] > 4:
#         print('{} is secure'.format(cars[i]))
#     elif scores[i] < 0:
#         print('{} is dangerous'.format(cars[i]))
#     else:
#         print('{} is not recommended'.format(cars[i]))

# На 1 кг веса 1 человек должен в день пить 30 миллилитров воды.
# Есть список весов людей, нужно создать новый список и добавить в него
# сколько воды должен пить из них каждый
# Зимой человек пьет на 20 процентов меньше воды
# 100 - 80 - 0.8
# В час сколько воды нужно выпить человеку летом и зимой в час?
# weights = [50, 30, 100, 120, 15]
# water_consumptions_summer = []
# water_consumptions_winter = []
# for i in range(0, len(weights)):
#     water_consumptions_summer.append(weights[i] * 30 / 1000)
#     water_consumptions_winter.append(weights[i] * 30 * 0.8 / 1000)
#     print(weights[i] * 30 / 1000 / 16)
#     print(weights[i] * 30 * 0.8 / 1000 / 16)
# print(water_consumptions_summer)
# print(water_consumptions_winter)

# Из списка поменять значение x на y
letters = ['a', 'c', 'm', 'x', 'l', 'r', 'x']

for i in range(0, len(letters)):
    if letters[i] == 'x':
        letters[i] = 'y'
        # break

print(letters)
