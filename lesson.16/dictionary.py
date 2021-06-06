# Rayon mashin indeksi
# Pocht indeksine gore unvan
# Olkede pul vahidi
# Telefon kitabchasi
# - Mekteb direktorlari
# - Restoran menyusu
# - Imtahanlar fennleri qruplara gore

# Olkede pul vahidi
# Azerbaycan - AZN
# Almaniya - Avro
# Chin - Yuan
# Russiya - Rubl
# Turkiye - YTL
# Izrail - INS
# Georgia - LARI


currencies = {
    "AZN": "Azerbaijan",
    "YTL": "Turkey",
    "RUBL": "Russia",
    "YUAN": "China",
    "INS": "Israel",
    "LARI": "Georgia",
    "EURO": ["Germany", 'France', 'Italy', 'Holland']
}


# car = {
#     "color": "red",
#     "brand": "Ford",
#     "year": 1985,
# }

# print(currencies['AZN'])
# print(currencies['INS'])

# currency = input('Enter a currency: ')
# print(currencies[currency])
# print(currencies['EURO'])
# print(len(currencies))
# print(type(currencies))
# print(type(print))
#
# currencies['RUBL'] = 'Tunisia'
# print(currencies)

# clear()
# print(currencies)
# currencies.clear()
# print(currencies)

# currencies.popitem()
# currencies.popitem()
# currencies.popitem()
# currencies.popitem()
# currencies.popitem()
# currencies.popitem()
# currencies.popitem()
# currencies.popitem()
# print(currencies)

# del
# print(currencies)
# del currencies['RUBL']
# print(currencies)

# pop(4)

# print(currencies)
# currencies.pop('AZN')
# print(currencies)

# currencies_copy = currencies.copy()
# print(currencies_copy)

# currencies_copy_new = currencies
# print(currencies_copy_new)

# currencies['AZN'] = 'Manat'
#
# print(currencies)
# print(currencies_copy)
# print(currencies_copy_new)

currencies['test'] = 'test'
print(currencies)



# currencies dictionarysinde eger istifadechi daxil etdiyi
# key varsa, onu silmek gerekir value ile birlikde.


# 1. Istifadechi key daxil edir. Eger o dictionaryde yoxdursa,
# hemin key elave edilir dictionaryye, value kimi ise her
# hansisa random ededi elave edirsiniz.

# 2. Telebelerin ballari yazildigi dictionary yaratmaq gerekir,
# key - Telebenin adi/soyadi/ata adi, value ise yigdigi xal
# Istifadechiye menu verin, ve hemin menuda bu sechimler olsun:
# 1. Telebe elave etmek (hem ad/soyad/ata adi, hem xali) +
# 2. Telebeni silmek +
# 3. Telebelerin siyahisina baxmaq +
# 4. Telebenin xalini deyishmek +

# Proqram istifadechi s herfini daxil edene
# kimi sonsuz olaraq ishlemelidir.


# 1. Вывести в красивой форме студентов и их баллы (каждый студент и его бал на отдельной строке + тире + id)
# 1. Movsumova Nigar Akif - 80 points
# 2. Aslan Babakishiyev Alim - 90 points

# 2. Выделить код в функции
# 3. Программа должна работать бесконечно, пока пользователь не ввел букву s.
# 4. Добавить в меню выборов, сколько студентов есть в словаре.


# Написать похожую программу для телефонного справочника.
# 1. Посмотреть номер телефона конкретного человека
# 2. Можно удалить номер телефона
# 3. Можно добавить номер телефона (если размер книжки уже дошел до 10, то
# предложите ему удалить номер чей-то, если он согласится,
# спросите для начала имя удаляемого контакта и удалите его.
# Если не соглашается, то вовзращаемся в основное меню.
# 4. Можно обновить номер телефона
# 5. Посмотреть сколько мобильных номеров есть
# 6. Очистить всю телефонную книжку (перед тем как очистить, еще раз спрашиваете подтверждения,
# если пользователь отказался, возвращайтесь в основное меню)

# test = input('Enter the input:')
# while test != 's':
#     print('If you want to end the program, enter s. ')
#     test = input('Enter the input:')
# print('Good bye!')
