def calculate(user_input_1, user_inut_2, operation):
    if operation == '+':
        print(user_input_1 + user_input_2)
    elif operation == "-":
        print(user_input_1 - user_inut_2)
    elif operation == "*":
        print(user_input_1 * user_inut_2)
    elif operation == "/":
        if user_input_2 == 0:
         print("Error")
        else:
            print(user_input_1 / user_inut_2)


user_input_1 = int(input('Enter first digit: '))
user_input_2 = int(input('Enter second digit: '))
operation = input("Enter operation: ")

print(calculate(user_input_1, user_input_2, operation))
