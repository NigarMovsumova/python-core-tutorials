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
print(txt.format(name='John', age=age))

sample_txt = '''
My name is Natalia.
My surname is Govorova.
I am 15.
I was born in 1982 in Chelyabinsk.
My address is Flat 116, 19, Pionerskaya Street. My phone number is 41-5-81.'''
