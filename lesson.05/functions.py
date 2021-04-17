from calculation.rectangle import calculate_rectangle_area

# def - definition/ define


def calculate_square_area():
    side = int(input('Enter side of the square: '))
    print(f'The area of Square = {side ** 2}')


def calculate_triangle_area():
    triangle_side = int(input('Enter side of the triangle: '))
    triangle_height = int(input('Enter height of the triangle: '))
    print(f'The area of Triangle = {triangle_side * triangle_height * 0.5}')


def calculate_circle_area():
    radius = int(input('Enter the radius of a circle:'))
    print(f'The area of a Circle = {(radius ** 2) * 3.14}')


choice = int(input('''
Please make a choice:
1. Rectangle
2. Square
3. Triangle
4. A circle\n'''))
if choice == 1:
    calculate_rectangle_area()
elif choice == 2:
    calculate_square_area()
elif choice == 3:
    calculate_triangle_area()
elif choice == 4:
    calculate_circle_area()
else:
    print('Your choice is invalid')
