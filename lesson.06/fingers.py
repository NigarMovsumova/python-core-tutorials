# 1.  Пользователь вводит порядковый номер пальца руки.
# Необходимо показать его название на экран - мизинец, указательный, безымянный и тд
# Нужно учесть все 10 пальцев руки, нельзя использовать or/ and или
# темы, которые мы не прошли

finger_index = int(input("Please enter finger's index number: "))

# 1, 6 - bolshoy palec % 5
# 2, 7 - ukazatelniy palec 2
# 3, 8 - sredniy palec 3
# 4, 9 - bezimanniy palec 4
# 5, 10 - mizinec 0

remainder = finger_index % 5
if finger_index > 10:
    print('Invalid input')
elif remainder == 1:
    print('Thumb')
elif remainder == 2:
    print('Forefinger')
elif remainder == 3:
    print('Middle Finger')
elif remainder == 4:
    print('Ring Finger')
elif remainder == 0:
    print('Little Finger')
