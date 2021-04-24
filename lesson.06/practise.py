# 1. 1-100 diapazonunda 3-ə bölünüən bütün ədədləri ekrana çıxaran proqram yazın.
# 2. Пользователь вводит слово, нужно вывести из этого слова только гласные - aeiou
# 3. İstifadəçi 1-20 arası ədəd daxil edir. 1den o edede kimi bütün ədədləri çap etmək gərəkir
# və yanında qeyd etmək lazımdır bu ədəd 10dan aşağıdır ya yox

# 1 is less than 10
# 2 is less than 10
# 10 is equal to 10
# 11 is more than

# user_input = input('Enter any word: ')
# index = 0
#
# while index < len(user_input):
#     print('index = ', index)
#     if user_input[index] == 'a':
#         print('index = ', index, 'I found a')
#     index += 1

number = int(input('Enter the number between 1 and 20: '))
index = 1
while index < number:
    if index < 10:
        print(index, 'is less than 10')
    elif index == 10:
        print(index, 'is equal to 10')
    else:
        print(index, 'is more than 10')
    index += 1


