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
call_score_2 = int(input('2 :'))
call_score_3 = int(input('3 :'))
call_score_4 = int(input('4 :'))
call_score_5 = int(input('5 :'))
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
