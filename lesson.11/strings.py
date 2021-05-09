hello = 'hello'
print('hello')
print(hello)

print('''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
''')

print("""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
""")

for character in hello:
    print(character)

print(len(hello))

print('h' in hello)
print('r' in hello)
print('he' in hello)

lorem = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit .
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(lorem[20])
print(lorem[0:5])
print(lorem[:5])
print(lorem[5:])
print(lorem[-1])
print(lorem[-2])
print(lorem[-3])
print(lorem[-10: -1])
print(lorem[::-1])
print(lorem.upper())
print(lorem.lower())

hello = " Hello, World! "
print(hello)
print(hello.strip())
print(hello)
print(lorem.replace('.', '!'))
print(lorem.replace(' ', '*'))

left = 'left'
right = 'right'
print(left + right)

# 1. Длинный текст в переменной
# 2. нужно заменить , на .
# 3. нужно распечатать все lowercase
# 4. проверить длина строки больше 200 или нет. true/false

text = '''Нас было много на челне;
Иные парус напрягали,
Другие дружно упирали
В глубь мощны веслы. В тишине
На руль склонясь, наш кормщик умный
В молчанье правил грузный челн;
А я — беспечной веры полн, —
Пловцам я пел… Вдруг лоно волн
Измял с налету вихорь шумный…
Погиб и кормщик и пловец! —
Лишь я, таинственный певец,
На берег выброшен грозою,
Я гимны прежние пою
И ризу влажную мою
Сушу на солнце под скалою.'''

text = text.replace(',', '.').lower()
print(text)
flag = True if len(text) > 200 else False
print(flag)
print(True if len(text) > 200 else False)

if len(text) > 200:
    print(True)
else:
    print(False)

age = 36
txt = "My name is John, {} and I am {}"
print(txt.format(13, age))
txt = "My name is John, {1} and I am {1}"
print(txt.format(13, age))
txt = 'My name is {name}, and I am {age}'
print(txt.format(age=age, name='John'))

name = input('Enter your name: ')
surname = input('Enter your surname: ')
age = input('Enter your age: ')
birth_year = input('Enter your birth year: ')
birth_place = input('Enter your birth place: ')
address = input('Enter your address: ')
phone_number = input('Enter your phone number: ')

sample_txt = '''
My name is {name}.
My surname is {surname}.
I am {age}.
I was born in {birth_year} in {birth_place}.
My address is {address}. My phone number is {phone_number}.'''

print(sample_txt.format(phone_number=phone_number, age=age, name=name, surname=surname,
                        birth_year=birth_year, birth_place=birth_place, address=address))

