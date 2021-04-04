account_balance = 900

price = float(input('Please, enter the price: '))

# eger account_balance > price - pulu var
# eks halda pulu yeterli deyil

if account_balance > price:
    print('You have enough balance')
else:
    print('You do not have enough balance')


# eger yash 65den ashagidirsa - pensiya yoxdur
# 65den 85e kimi - $200
# 85den 100e kimi - $400
# 100den yuxari - $600

age = int(input('Enter your age: '))
if age < 65:
    print('You are not old enough.')
#else if
elif 65 <= age < 85:
    print('Your pension is $200')
elif 85 <= age < 100:
    print('Your pension is $400')
else:
    print('Your pension is $600')
