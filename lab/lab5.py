import math


# Задача 2
def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read()


# Задача 3
def print_square_root():
    try:
        number = int(input("Enter a positive integer: "))
        if number < 0:
            raise ValueError("Negative number")
        print(math.sqrt(number))
    except ValueError:
        print("Invalid Number")
    finally:
        print("Good Bye")


if __name__ == "__main__":
    # Задача 2 - изключенията се обработват от извикващия код
    try:
        print(read_file("test.txt"))
    except OSError as e:
        print(f"Cannot read file: {e}")

    # Задача 3
    print_square_root()
