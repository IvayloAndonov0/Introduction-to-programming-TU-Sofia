import random
def exercise_1():
    number = int(input("Enter an integer: "))
    digits = tuple(int(digit) for digit in str(number))
    reverse_digits = digits[::-1]

    print(f"Digits in  order: {digits}")
    print(f"Digits in reverse order: {reverse_digits}")


#exercise_1()

def exercise_2():
    numbers = [random.randint(1, 100) for _ in range(10)]
    numbers_with_sums = []

    for index, number in enumerate(numbers):
        numbers_with_sums.append(number)
        if index < len(numbers) - 1:
            numbers_with_sums.append(number + numbers[index + 1])

    print(numbers)
    print(numbers_with_sums)

#exercise_2()

def exercise_3():
    text = input("Enter text: ")
    character_counts = {}

    for character in text:
        character_counts[character] = character_counts.get(character, 0) + 1

    print(character_counts)

#exercise_3()

def exercise_4():
    number = int(input("Enter an integer: "))
    numbers = list(range(1, number + 1))
    reversed_numbers = numbers[::-1]
    number_mapping = dict(zip(numbers, reversed_numbers))

    print(numbers)
    print(number_mapping)

#exercise_4()
