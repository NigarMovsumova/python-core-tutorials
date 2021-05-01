# Extra :
# Распечатать произведение цифр числа, делящихся на 3 без остатка

number = int(input('enter the number: '))
digits_product = 1
while number != 0:
    if (number % 10) % 3 == 0 and number % 10 != 0:
        digits_product = digits_product * (number % 10)
    number = number // 10

print('product of digits = ', digits_product)
