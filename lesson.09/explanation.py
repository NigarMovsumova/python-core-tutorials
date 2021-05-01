# İstifadəçi 5 rəqəmli ədəd daxil edir, ədədi əksinə çevirən proqram yazın.
# 12345
# 54321

number = int(input('Enter the number: '))

for index in range(1, 6):
    print(number % 10)
    number = number // 10

# 1. concatenation

example = 'abcd' + 'efgh'
example = example + str(5)
print(example)
