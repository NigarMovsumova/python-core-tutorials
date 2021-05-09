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
