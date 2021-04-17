# 4.  İstifadəçi klaviaturadan 3 rəqəm daxil edir. Birincisi - aylıq maaşıdır. İkincisi - aylıq kredit
# ödənişidir, üçüncüsü - kommunal xidmətlərə görə borcudur.
# Bütün ödənişləri etdikdən sonra istifadəçidə hansı məbləğin qaldığını konsola çıxartmaq
# lazımdır.

# salary = float(input('Enter the salary:'))
# loan = float(input('Enter the monthly loan amount:'))
# utility = float(input('Enter the utility amount:'))
# print(f'{salary - loan - utility} amount is left after all payments')


def calculate_net_profit():
    salary = float(input('Enter the salary:'))
    loan = float(input('Enter the monthly loan amount:'))
    utility = float(input('Enter the utility amount:'))
    print(f'{salary - loan - utility} amount is left after all payments')


calculate_net_profit()
