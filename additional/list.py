# 4. Даны три числа. Вывести на экран «yes«,
# если можно взять какие-то два из них и в сумме получить третье


list1 = [1, 2, 3]

for i in range(0, len(list1)):
    for j in range(i + 1, len(list1)):
        if i != j and list1[i] + list1[j] == list1[len(list1) - i - j]:
            print(i, '  ',  j, '   ', list1[i], ' + ', list1[j], ' = ', list1[len(list1) - i - j])
