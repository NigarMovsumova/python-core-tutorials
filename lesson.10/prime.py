# number = int(input('Enter the number: '))
# flag = True
# for i in range(2, number):
#     if number % i == 0:
#         flag = False
#         break
# print(number, 'is Prime ? ', flag)

for j in range(2, 11):
    is_prime = True
    for i in range(2, j):
        if j % i == 0:
            is_prime = False
            break
    print(j, 'is Prime ? ', is_prime)

