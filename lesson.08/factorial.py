# Ədədin faktorialını tapan proqram yazın. (Məsələn (! - faktorial işarəsidir),  5! = 1*2*3*4*5)
# 3 = 1 * 2 * 3
# 5 = 1 * 2 * 3 * 4 * 5 = 120
# 0 ! = 1
# 1 ! = 1
number = int(input('enter the number:'))
factorial = 1
index = 1
while index <= number:
    factorial = factorial * index
    index += 1

print(factorial)
