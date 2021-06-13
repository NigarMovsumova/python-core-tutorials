def salutation():
    print("\n\t\tWelcome to your contact book\n")


def specific_person_contact():
    contact_name = str(input("Enter contact info: "))
    print(contact_list[contact_name])


def delete_number():
    contact_name = str(input("Enter name of contact: "))

    choice = input("Are you sure?\n Y or N \n")

    if choice == 'Y':
        del contact_list[contact_name]
        print("\nContact deleted")

    # elif choice == 'N':


# 3. Можно добавить номер телефона (если размер книжки уже дошел до 10, то

# предложите ему удалить номер чей-то, если он согласится,

# спросите для начала имя удаляемого контакта и удалите его.

# Если не соглашается, то вовзращаемся в основное меню.

def add_number():
    if len(contact_list) < 10:

        contact_name = str(input("Enter name of contact: "))

        contact_number = str(input("Enter phone number: "))

        contact_list[contact_name] = contact_number

        print("Contact added")

    elif len(contact_list) == 10:

        print("You dont have any memory for this please delete old contact")

        delete_number()


def update_number():
    change_name = str(input("Enter name of contact: "))

    change_number = str(input("Enter new number: "))

    contact_list[change_name] = change_number

    print("Changes has been saved")


def how_many_numbers():
    print("You have ", len(contact_list), " contacts in your contact book")


def delete_all():
    choice_for_delete = str(input("Are you sure? \n Y or N \n"))

    if choice_for_delete == 'Yes':

        del contact_list

        print("All contacts deleted")

    elif choice_for_delete == 'No':

        return choice

    else:

        print("Wrong choise")

        return choice_for_delete


def all_list():
    print(contact_list)


contact_list = {

    "Tale Suleymanov": "0502312279",

    "Aslan Babakisiyev": "0502312097",

    "Mehman Esgerov": "0502312128",

    "Ejder Huseynzade": "0502312535",

    "Taleh Bayramov": "0502312480",

}

salutation()

choice = int(input('''Please make a choice:\n

1. Watch specific contact

2. Add contanct

3. Delete contanct

4. Update phone number

5. Whatch how many contacts you have

6. Delete all contacts

7. Whatch all contacts

\n'''))

if choice == 1:
    spesific_person_contact()
elif choice == 2:
    add_number()
elif choice == 3:
    delete_number()
elif choice == 4:
    update_number()
elif choice == 5:
    how_many_numbers()
elif choice == 6:
    delete_all()
elif choice == 7:
    all_list()
else:
    print("Wrong choice")
