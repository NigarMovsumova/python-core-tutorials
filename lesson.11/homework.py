# 1) İstifadəçi araligi daxil edir. O araliqda butun ededleri yoxlayib , sade olub
# olmadigini gostermek gerekir. Ədəd sadədirsə True, mürəkkəbdirsə False çap olunsun.
# (Sadə ədədlər yalnız özünə və 1-ə bölünən ədədlərdir)


# first_digit = int(input("Enter first digit: "))
# second_digit = int(input("Enter second digit: "))
# for i in range(first_digit, second_digit):
#     is_prime = True
#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#             break
#     print(i, "is prime? ", is_prime)

# 3) Istifadechi eded daxil edir. Ededin tek reqemlerinin cemini tapmaq gerekir

number = int(input('Enter any num: '))
numbers_sum = 0

while number != 0:
    print(number % 10)
    if (number % 10) % 2 != 0:
        numbers_sum += number % 10
    # number = number // 10
    number //= 10

print(numbers_sum)
