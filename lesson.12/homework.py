# 2 Given an input string. Count occurences of all characters within a string [a,b,c,d,e]

# string = input('Enter string: ')
# index = 0
# count_a = 0
# count_b = 0
# count_c = 0
# count_d = 0
# count_e = 0
#
# while index <= len(string) - 1:
#     if string[index] == 'a':
#         count_a += 1
#     elif string[index] == 'b':
#         count_b += 1
#     elif string[index] == 'c':
#         count_c += 1
#     elif string[index] == 'd':
#         count_d += 1
#     elif string[index] == 'e':
#         count_e += 1
#     index += 1
#
# print(count_a, count_b, count_c, count_d, count_e)

# 2. Removal all the characters other than integers from a string
# User enters a string.

# result = ''
# user_input = input('Enter the string:')
# for i in user_input:
#     if i.isdigit():
#         result += i
#
# print(result)

user_input = input('Enter the string:')
print(user_input[1])
result = ""
i = 0
while i < len(user_input):
    if user_input[i].isdigit():
        result += user_input[i]
    i += 1
print(result)

# user_input = input('Enter the string:')
# for i in user_input:
#     if not i.isdigit():
#         user_input = user_input.replace(i, '')
#
# print(user_input)

# user_input = input('Enter the string:')
# for i in user_input:
#     if i.isalpha() or i.isspace() or i == '.':
#         user_input = user_input.replace(i, '')
#
# print(user_input)

# 3. By using first, second and last characters of the string, create a new string.

# user_input = input('Enter the string: ')
# print(user_input[0:2] + user_input[-1])

# 4. Does the string start with an A?

# user_input = input('Enter the string: ')
# if user_input[0] == 'A':
#     print('String starts with an A')
# else:
#     print('String does not start with an A')

# if user_input[0] == 'A' or user_input[0] == 'a':
#     print('String starts with an A/a')
# else:
#     print('String does not start with an A/a')

# print(user_input[0].upper())
#
# if user_input[0].upper() == 'A':
#     print('String starts with an A/a')
# else:
#     print('String does not start with an A/a')

# print(user_input[0].lower())
#
# if user_input[0].lower() == 'a':
#     print('String starts with an A/a')
# else:
#     print('String does not start with an A/a')

# text = input('Enter the string: ')
# result = ''
# for i in text:
#     if i == 'a' or i == 'e' or i == 'u' or i == 'o' or i == 'i':
#         result += i
# print(result, end='')

# text = input('Enter the string: ')
# text = text.replace(' ', '')
# print(text)


# • Методы строк.
# • Срез строки
# • Экранированные последовательности
# • «Сырые строки»
# • Форматированный вывод

# Escape последовательности

# \n
# print('test\ntest')
# # \'
# # print('test\')
# print("test'")
# # print('test'')
# print('test\'')
# print('It\'s an apple.')
# print("It\'s an apple.")
#
# # print("test"")
# print('test"')
# print("test\"")
# print('test\"')
#
# print("\"Don\'t judge each day by the harvest you reap but by the seeds that you plant.\" \n-Robert Louis Stevenson")
#
# print("\"Don\'t judge each day by the harvest you reap but by the seeds that you plant.\"\n Robert Louis Stevenson")
#
# print('\\\\\\')
# # C:\\Users\\Pat\\Desktop
# print('Apple        is\tthe best company in the company')
# apple = '\\\\\"Apple'
#
# # print(len(apple))
# print('Apple\tTest')
# print('t\tTest')
# print('\tApple')
# print('\t\tApple')
# print('Paralleloqra\t')
#
#
# print('Apple\tGoogle\tAmazon\tFacebook\tPalantir\tMicrosoft\tNetflix')
# print('1.55\tt')
# print('Azercell20\t\tt')
# print('\t\t"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et \n'
#       'dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea \n'
#       'commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat \n'
#       'nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim\n'
#       'id est laborum."')
