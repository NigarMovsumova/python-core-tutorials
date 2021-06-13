# args , kwargs
import math

# def test(*args, **kwargs):
#     print(kwargs)
#     print(kwargs['students'])
#     print(args)
#     print(args[0])
#     print(args[1])
#
#
# test([27, 32], [1600, 1400], students=['Nigar', 'Tale'], scholarships=[10000, 10000])


# def sum_numbers(*args, choice='n'):
#     print(choice)
#     numbers_sum = 0
#     for arg in args:
#         numbers_sum += arg
#     return numbers_sum
#
#
# choice = input('Enter y or n: ')
# print(sum_numbers(1, 2, choice=choice))
# print(sum_numbers(1, 2, 3, 4))
# print(sum_numbers(4))

# Функция принимает args - модели машин,
# если в kwargs есть ключевое слово "год", то нужно к каждому названию машины
# добавить год и вернуть.


def get_car_models(*args, **kwargs):
    # year = ' ' + kwargs['year'] if 'year' in kwargs.keys() else ''
    if 'year' in kwargs.keys():
        year = ' ' + kwargs['year']
    else:
        year = ''
    for arg in args:
        print(arg + year)


# get_car_models('Ford Focus', 'Hyundai Accent', year='2016')
# get_car_models('Ford Focus', 'Hyundai Accent')

def print_contacts():
    counter = 1
    for contact in contact_list.values():
        print('{}. {}'.format(counter, contact))
        counter += 1


def view_contact_by_index(user_choices):
    print(user_choices)
    counter = 1
    for i in user_choices:
        for number, contact in contact_list.items():
            if int(i) == counter:
                print('contact: {}, number: {}'.format(contact, number))
                break
            counter += 1


def view_contact_by_full_name(user_choices):
    for user_choice in user_choices:
        for number, contact in contact_list.items():
            if contact == user_choice:
                print("Contact: {} Number: {}".format(contact,  number))


def view_contact_by_first_letter(user_choices):
    contact_set = set()
    for user_choice in user_choices:
        for number, contact in contact_list.items():
            if contact[0: len(user_choice)] == user_choice:
                # print("Contact: {} Number: {}".format(contact,  number))
                contact_set.add("Contact: {} Number: {}".format(contact,  number))
    for contact in contact_set:
        print(contact)


contact_list = {
        "0502312279": "Tale Suleymanov",
        "0502312097": "Aslan Babakishiyev",
        "0502312128": "Mehman Askerov",
        "0502312535": "Ejder Huseynzade",
        "0502312480": "Taleh Bayramov",
        "0507777777": "Tukezban Melhemova",
        "0554321242": "Nigar Movsumova"
}

print_contacts()

user_input = ''
user_choices = []
while user_input != 's':
    user_choice = input('Enter contact name: ')
    user_choices.append(user_choice)
    print('If you want to exit, enter \'s\' as an input')
    user_input = input('Do you want to continue? ')

print('Contacts List: ')
# view_contacts(user_choices)
# view_contact_by_index(user_choices)
view_contact_by_first_letter(user_choices)

# По индексу передает контакт, по имени ? - regex
