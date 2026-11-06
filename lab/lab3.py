def square_area(side):
    return side * side


def rectangle_area(width, height):
    return width * height


def right_triangle_area(leg_a, leg_b):
    return leg_a * leg_b / 2


def exercise_1():
    print("1 - square")
    print("2 - rectangle")
    print("3 - right triangle")
    shape = input("Choose a shape: ")

    if shape == "1":
        side = float(input("Side: "))
        area = square_area(side)
    elif shape == "2":
        width = float(input("Width: "))
        height = float(input("Height: "))
        area = rectangle_area(width, height)
    elif shape == "3":
        leg_a = float(input("Leg a: "))
        leg_b = float(input("Leg b: "))
        area = right_triangle_area(leg_a, leg_b)
    else:
        print("Invalid shape")
        return

    print(f"Area: {area}")


#exercise_1()


def is_palindrome(number):
    text = str(number)
    if text == text[::-1]:
        return 1
    return 0


def exercise_2():
    number = int(input("Enter an integer: "))
    if is_palindrome(number):
        print(f"{number} is a palindrome")
    else:
        print(f"{number} is not a palindrome")


#exercise_2()


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def exercise_3():
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

    operation = input("Operation (+, -, *, /): ")
    if operation not in operations:
        print("Invalid operation")
        return

    a = int(input("First number: "))
    b = int(input("Second number: "))

    result = operations[operation](a, b)
    if result is None:
        print("Division by zero is not allowed")
    else:
        print(f"{a} {operation} {b} = {result}")


#exercise_3()


def replace_greater_with_zero(numbers, limit):
    for index in range(len(numbers)):
        if numbers[index] > limit:
            numbers[index] = 0


def exercise_4():
    numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    limit = int(input("Enter a number: "))

    replace_greater_with_zero(numbers, limit)
    print(numbers)


#exercise_4()
