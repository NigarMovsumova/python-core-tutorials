# Пользователь вводит ежемесячный взнос и на сколько месяцев он
# хочет оставить деньги в банке
# Сколько денег у него будет в конце ?

month_count = int(input('Ежемесячный вклад: '))
monthly_amount = int(input('Срок вклада: '))
total_fee = month_count * monthly_amount
print('Общая сумма сбережений: ', total_fee)
