# Пользователь через консоль вводит сколько звонков у него было сегодня
# Далее он вводит сколько человек дало какую оценку за звонок - 1, 2, 3, 4, 5
# по каждой оценке он вводит сколько человек так проголосовали
# Нужно посчитать и вывести какой средний результат у пользователя по оценённым звонкам
#
# Если среднее более 4.5 - результат отличный
# Если результат меньше 4 - результат ужасный
# Если результат между 4 и 4.5 - результат хороший

print('Enter the count of people with marks: ')
call_score_1 = int(input('1 :'))
# 10
call_score_2 = int(input('2 :'))
# 20
call_score_3 = int(input('3 :'))
# 30
call_score_4 = int(input('4 :'))
# 40
call_score_5 = int(input('5 :'))
# 50
# 250 + 300 = 550 / 150 = 3.6
score = (call_score_1 * 1 + call_score_2 * 2 + call_score_3 * 3 + call_score_4 * 4 +
         call_score_5 * 5) / \
        (call_score_1 + call_score_2 + call_score_3 + call_score_4 + call_score_5)
print(f'You average for today is {score}')
if score >= 4.5:
    print('Excellent result')
elif score <= 4:
    print('Awful result')
else:
    print('Not bad result')
# Пример на среднее арифметическое
# Сегодня у вас было 6 уроков
# Из них вы по одному получили 2, по одному 4, по двум - 5.
# Какая у вас средняя оценка за день
# 1.  /4
# 2. 2 * 1 + 4 * 1 + 5 * 2 = 2 + 4 + 10 = 16  - общая сумма оценок
# 3. 16 / 4 = 4

# Яблоки и груши
# Сколько-то килограммов яблок и груш по разным ценам
# Какая будет общая цена за эти покупки
# 1 kq яблок - 40 копеек, 1 кг груш - 60 копеек
# я купила 2 кг яблок и 3 кг груш - 2 * 0.40 + 3 * 0.60 = 0.8 + 1.8 = 2.6
# 2.6 / 5 = 0.52 копеек

# У тебя квартира, 50 кв метров
# на кухне у тебя были затраты на ремонт - 3000 манат на 1 кв метр
# всего у тебя на кухне 10 кв метров
# в столовой у тебя были затраты на ремонт - 2000 манат на 1 кв метр
# всего я тебя в столовой 15 кв матров
# какая средняя затрата на отремонтированную часть квартиры на 1 кв м
# (3000 * 10 + 2000 * 15)/25

# Я - преподаватель
# Я получаю зп с учеников за 8 уроков
# 1 ученик - частно - 250 азн за 8 уроков
# 1 группа, в которой 30 человек - 1000 за 8 уроков
# 1 группа, в которой 7 человек - 350 манат за 8 уроков
# Сколько я получаю в среднем с одного своего студента за 8 уроков
# (250 + 1000 + 350) / 38 = 1600 / 38

# В компании 10 работников
# Из них 1 менеджер, 1 исполнительный директор, 7 офисных работников, 1 уборщица
# Менеджер получает 4500, директор получает 8000, офисные работники - 350,
# уборщица получает 800 манат
# Сколько в среднем на 1 человека получается зп
# (4500 + 8000 + 350 * 7 + 800 ) / 10

# У меня 10 кошек
# 3 кошкам 19 лет, 2 кошкам - 1 год, 5 кошкам - 4 годика
# Какой средний возраст одной кошки
# (3 * 19 + 2 * 1 + 5 * 4 ) / 10

# 10 детей
# 1 ребенок - больше 18 лет - нет расходов
# 3 детей - меньше 5 лет - 150 манат
# 3 детей - больше 5 лет и меньше 15 лет - 120 манат
# 3 ребенка - больше 15 лет - 350 манат
# в среднем на 1 ребенка сколько расходов у тебя
# (3 * 150 + 3 * 120 + 3 * 350 + 1 * 0) / 10
