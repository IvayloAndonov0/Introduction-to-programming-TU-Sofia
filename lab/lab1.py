def max_number():
    n = int(input("Enter the number of integers "))
    max_number = int(input("Enter starting max number "))
    for number in range(n-1):
        new_number = int(input("Enter a number "))
        if new_number > number:
            max_number = new_number
    print(f"Your biggest number is {max_number}")

#max_number()



def sum_numbers():
    count = int(input("Enter the number of integers "))
    sum = 0
    for number in range(count):
        new_n = int(input("Enter a number to add "))
        sum += new_n
    print(f"The sum is {sum}")

#sum_numbers()

def print_stars():
    n = int(input("Enter the number of rows "))

    for i in range(n+1):
        print("*" * i)

print_stars()