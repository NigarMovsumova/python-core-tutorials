# 2. Есть числа от 1 до 100, нужно находить их сумму до тех пор, пока сумма меньше 100.
# В итоге нужно вывести конечную сумму и на каком числе программа остановила подсчёт
index = 1
numbers_sum = 0
while numbers_sum < 100:
    numbers_sum += index
    index += 1
print(numbers_sum)
print(index - 1)
