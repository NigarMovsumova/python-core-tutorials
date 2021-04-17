def check_pension_age():
    if age <= 65:
        print('You are too young.')
    else:
        print('You can get a pension.')

# def check_pension_age_with_args(age):
#     if age <= 65:
#         print('You are too young.')
#     else:
#         print('You can get a pension.')


age = int(input('Enter your age: '))
check_pension_age()

# age = int(input('Enter your age: '))
# check_pension_age_with_args(age)

