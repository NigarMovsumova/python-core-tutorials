print('I`m a teacher')
print('I receive a salary from students for 8 lessons')
privately_student = int(input('Count of privately student:'))
big_group = int(input('Count of group studens:'))
small_group = int(input('Count of small studens:'))
price_of_privately_student = 250
price_of_big_group = 1000
price_of_small_group = 350
score = (privately_student * price_of_privately_student +
big_group * price_of_big_group +
small_group * price_of_small_group)/\
        (privately_student + big_group + small_group)
print(f'You average is {score}')
