# 1. Sətirdəki bütün saitləri sayan program yazın. ( A E İ O U).

user_input = input('Enter any word: ')
index = 0
count = 0
while index < len(user_input):
    if user_input[index] == 'a' or user_input[index] == 'e' \
        or user_input[index] == 'o' or user_input[index] == 'i' or user_input[index] == 'u':
        count += 1
    index += 1

print(count)
