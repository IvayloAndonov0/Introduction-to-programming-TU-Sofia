import random
 
 
#  Helper functions 
 
def read_numbers(prompt):
    return [int(x) for x in input(prompt).split()]
 
 
def read_dict(prompt):
    result = {}
    for pair in input(prompt).split(","):
        pair = pair.strip()
        if pair:
            name, quantity = pair.split(":")
            result[name.strip()] = int(quantity)
    return result
 
 
#  Tasks 
 
def task_1():
    number = int(input("Enter an integer: "))
    forward = tuple(int(c) for c in str(abs(number)))  
    backward = forward[::-1]                           
    print("Forward order: ", forward)
    print("Reverse order: ", backward)
 
 
def task_2():
    numbers = [random.randint(1, 20) for _ in range(6)]
    print("Original list:", numbers)
 
    result = []
    for i in range(len(numbers) - 1):
        result.append(numbers[i])
        result.append(numbers[i] + numbers[i + 1]) 
    result.append(numbers[-1])                      
    print("After inserting sums:", result)
 
 
def task_3():
    text = input("Enter text: ")
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1  
    print(counts)
 
 
def task_4():
    n = int(input("Enter a positive integer n: "))
    numbers = list(range(1, n + 1))
    reversed_map = dict(zip(numbers, numbers[::-1]))  
    print("List:      ", numbers)
    print("Dictionary:", reversed_map)
 
 
def task_5():
    numbers = read_numbers("Enter integers (separated by spaces): ")
    smallest, largest = min(numbers), max(numbers)
    print(f"Smallest: {smallest}, occurs {numbers.count(smallest)} time(s)")
    print(f"Largest:  {largest}, occurs {numbers.count(largest)} time(s)")
 
 
def task_6():
    numbers = [random.randint(1, 5) for _ in range(10)]
    print("Original list:", numbers)
 
    unique = []
    for number in numbers:
        if number not in unique:  
            unique.append(number)
    print("Without duplicates:", unique)
 
 
def task_7():
    numbers = read_numbers("Enter a list of numbers (separated by spaces): ")
    x = int(input("Enter the number x: "))
    indices = [i for i, number in enumerate(numbers) if number == x]
    if indices:
        print(f"{x} is found at indices:", indices)
    else:
        print(f"The number {x} is not in the list.")
 
 
def task_8():
    a = [random.randint(1, 10) for _ in range(8)]
    b = [random.randint(1, 10) for _ in range(8)]
    print("First list: ", a)
    print("Second list:", b)
 
    set_b = set(b)  
    common = []
    for number in a:
        if number in set_b and number not in common:
            common.append(number)
    print("Common elements:", common)
 
 
def task_9():
    numbers = tuple(read_numbers("Enter integers (separated by spaces): "))
    total = sum(numbers)
    average = total / len(numbers)
    evens = tuple(x for x in numbers if x % 2 == 0)
    print("Sum:", total)
    print("Average:", average)
    print("Tuple of even numbers:", evens)
 
 
def task_10():
    sentence = input("Enter a sentence: ")
    counts = {}
    for word in sentence.lower().split():   
        word = word.strip(".,!?;:\"'()")   
        if word:
            counts[word] = counts.get(word, 0) + 1
    print(counts)
 
 
def task_11():
    n = int(input("How many students will you enter? "))
    grades = {}
    for _ in range(n):
        name = input("Name: ")
        grades[name] = float(input(f"Grade of {name}: "))
 
    print("Students with a grade above 4.50:")
    for name, grade in grades.items():
        if grade > 4.50:
            print(" -", name, grade)
 
    average = sum(grades.values()) / len(grades)
    print(f"Average grade: {average:.2f}")
 
 
def task_12():
    print("Format: product:quantity, product:quantity ...")
    d1 = read_dict("First dictionary: ")
    d2 = read_dict("Second dictionary: ")
 
    merged = dict(d1)                   # copy of the first one
    for product, quantity in d2.items():
        merged[product] = merged.get(product, 0) + quantity
    print("Merged dictionary:", merged)
 
 
def task_13():
    a = set(read_numbers("First set (separated by spaces): "))
    b = set(read_numbers("Second set (separated by spaces): "))
    print("Union:                ", a | b)
    print("Intersection:         ", a & b)
    print("Difference (A - B):   ", a - b)
    print("Symmetric difference: ", a ^ b)
 
 
def task_14():
    numbers = read_numbers("Enter a list of numbers (separated by spaces): ")
    unique = set(numbers)
    print("Number of distinct numbers:", len(unique))
    repeated = sorted(x for x in unique if numbers.count(x) > 1)
    print("Numbers that occur more than once:", repeated)
 
 
def task_15():
    n = int(input("Enter n: "))
    result = {k: (k ** 2, k ** 3) for k in range(1, n + 1)}
    print(result)
 
 
# ---------- Menu ----------
 
TASKS = {
    1: task_1, 2: task_2, 3: task_3, 4: task_4, 5: task_5,
    6: task_6, 7: task_7, 8: task_8, 9: task_9, 10: task_10,
    11: task_11, 12: task_12, 13: task_13, 14: task_14,
    15: task_15,
}
 
if __name__ == "__main__":
    while True:
        choice = input("\nChoose a task (1-15) or 0 to exit: ")
        if choice == "0":
            break
        if choice.isdigit() and int(choice) in TASKS:
            TASKS[int(choice)]()
        else:
            print("Invalid choice.")
 