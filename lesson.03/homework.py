# 1. İstifadəçi rəqəm daxil edir. Əgər rəqəm 0dan yuxarıdırsa,
# konsola - "Number is positive",
# 0dan aşağıdırsa, "Number is negative", 0a bərabərdirsə,
# "Number is equal to zero" çıxarın.

# number = int(input('Enter the number:'))
# if number < 0:
#     print("Number is negative")
# elif number > 0:
#     print('Number is positive')
# else:
#     print('Number is equal to zero')

# 2. İstifadəçi klaviaturadan saati daxil edir.
# Əgər daxil edilən nömrə 0-6 arasında yerləşirsə, o zaman "Good Night" çıxarın,
# Eger 7- 12 arasinda yerleshirse, 'Good Morning' chixarin
# 13-17 arasındadırsa, "Good Day" çıxarın,
# 18-0 arası isə - "Good Evening".
# Məsələn, 6 rəqəmi 6-13 arasındadır.
#
# hour = int(input('Enter the hour:'))
# if hour >= 0 and hour<=6:
#     print('Good night')
# elif hour >= 7 and hour <= 12:
#     print('Good morning')
# elif hour >= 13 and hour <= 17:
#     print('Good day')
# elif hour >= 18 and hour <= 24:
#     print('Good evening')
# else:
#     print('Your input is invalid')

# hour = int(input('Enter the hour:'))
# if 0 <= hour <= 6:
#     print('Good night')
# elif 7 <= hour <= 12:
#     print('Good morning')
# elif 13 <= hour <= 17:
#     print('Good day')
# elif 18 <= hour <= 24:
#     print('Good evening')
# else:
#     print('Your input is invalid')


# 3.  İstifadəçi klaviaturadan 3 rəqəm daxil edir. Birincisi - aylıq maaşıdır.
# İkincisi - aylıq kredit
# ödənişidir, üçüncüsü - kommunal xidmətlərə görə borcudur.
# Bütün ödənişləri etdikdən sonra istifadəçidə hansı məbləğin qaldığını konsola çıxartmaq
# lazımdır.
#
# salary = float(input('Enter your salary: '))
# monthly_loan_payment = float(input('Enter your monthly loan payment: '))
# monthly_utility_payment = float(input('Enter your monthly utility payment: '))
# print(f'Your remaining balance: {salary -monthly_loan_payment - monthly_utility_payment} AZN')


# 4. Istifadəçi otağın enini, uzunluğunu və hündürlüyünü daxil edir, otağın divarları üçün neçə kv
# metr oboy lazım olduğunu hesablayan program yazın.

# width = float(input('Enter width of the room:'))
# length = float(input('Enter length of the room:'))
# height = float(input('Enter height of the room:'))
# print(f'You need {2* height* (length + width)} square meter wallpapers')
# 2 * length * height + 2 * width * height
# 2*height*(length + width)

# 5. Пользователь вводит цену машины и скидку на нее.
# Нужно показать пользователю, сколько она будет стоить после скидки
# и сколько составила скидка
# car_price = float(input('Enter car\'s price'))
# car_price = float(input("Enter car's price: "))
# discount_percentage = float(input('Enter the discount in percents:'))
# discount_amount = car_price * discount_percentage / 100
# print(f'Your car will cost {car_price - discount_amount} AZN after {discount_amount} AZN discount')

# Extras:
# 1. İstifadəçi klaviaturadan 3 rəqəm daxil edir.
# İstifadəçi seçimindən asılır olaraq proqram 3 rəqəmin cəmini ya
# hasilini konsola çıxarır.
# num1 = int(input('Enter the first number:'))
# num2 = int(input('Enter the second number:'))
# num3 = int(input('Enter the third number:'))
# choice = int(input('''
# Please make a choice:
# 1. Sum
# 2. Multiply\n'''))
# if choice == 1:
#     print(f'Result = {num1 + num2 + num3}')
# elif choice == 2:
#     print(f'Result = {num1 * num2 * num3}')
# else:
#     print('Your choice is invalid.')

# 2. İstifadəçi 2 rəqəm daxil edir.
# Seçimindən asılı olaraq, proqram ekrana 2 rəqəmin maksimumunu,
# minimumunu və ya hasilini əks etdirin.
# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter the second number: '))
# choice = int(input('''
# Please make a choice:
# 1. Max
# 2. Min
# 3. Multiply
# '''))
# if choice == 3:
#     print(f'Result = {num1 * num2}')
# elif choice == 1:
#     if num1 > num2:
#         print(f'Max = {num1}')
#     elif num1 < num2:
#         print(f'Max = {num2}')
#     else:
#         print(f'Numbers are equal to {num1}')
# elif choice == 2:
#     if num1 > num2:
#         print(f'Min = {num2}')
#     elif num1 < num2:
#         print(f'Min = {num1}')
#     else:
#         print(f'Numbers are equal to {num1}')
# else:
#     print('Your input is invalid.')

# 3. İstifadəçi klaviaturdan metr sayını daxil edir.
# Seçimdən asılı olaraq, proqram metrləri millərə, düymlara
# və ya yardlara çevirir.

meters = float(input('Enter the meters count: '))
choice = int(input('''
Please make a choice:
1. Miles
2. Inches
3. Yards
'''))
if choice == 1:
    print(f'{meters} meters = {meters * 0.000621371} miles')
elif choice == 2:
    print(f'{meters} meters = {meters * 39.3701} inches')
elif choice == 3:
    print(f'{meters} meters = {meters * 1.09361} yards')
else:
    print('Your input is invalid.')

