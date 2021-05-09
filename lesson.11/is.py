# 0. Count all lower case, upper case, digits from a given string
#
# lower - 10
# upper - 3
# digits - 10


country = 'Azerbaijan 1994'

print(country[0].isupper())
print(country[0].islower())
print(country[0].isdigit())
print(country[-1].isdigit())
print(country[10].isalnum())

print(country[0].isalnum())
print(country[-1].isalnum())
print(country[0].isalpha())

print(country[-1].isalpha())
print(country[10].isspace())
print(country.istitle())
test = 'test'
print(test.istitle())
test = 'TEST'
print(test.istitle())
print('\n')
decimal = '12345,6'
print(decimal.isdigit())
print(decimal.isdecimal())
print(ord('a'))
print(ord('A'))
print(ord('!'))
print(ord('\t'))
print('\t'.isprintable())
print(' '.isprintable())
