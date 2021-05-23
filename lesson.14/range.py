import datetime

# 2.Siyahi reqemlerden ibaretdir.Cut olan reqemlerin siyahida hansi indeksde yerlesdiyini cap edin.
example_list = []

for i in range(0, 100000):
    example_list.append(i)

print(datetime.datetime.now())
for i in range(0, 100000):
    if example_list[i] % 2 == 0:
        print(example_list[i], end=' ')
print('\n')
print(datetime.datetime.now())

print('\n')
# i = 0
# for element in example_list:
#     if element % 2 == 0:
#         print(i, end=' ')
#     i += 1
print(datetime.datetime.now())
for element in example_list:
    if element % 2 == 0:
        print(element, end=' ')
print('\n')
print(datetime.datetime.now())
