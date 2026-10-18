import math


def exercise_1():
    price = float(input("Price: "))
    first_discount = float(input("Discount: "))
    second_discount = float(input("Second discount: "))

    price -= price * first_discount / 100
    price -= price * second_discount / 100

    print(f"Final price: {price:.2f}")


def exercise_2():
    km_with_bus = float(input("Enter the distance in kilometers for bus: "))
    km_with_taxi = float(input("Enter the distance in kilometers for taxi: "))
    price_with_bus = float(input("Enter the price per km for bus: "))
    price_with_taxi = float(input("Enter the price per km for taxi: "))

    total_cost_bus = km_with_bus * price_with_bus
    total_cost_taxi = km_with_taxi * price_with_taxi
    total_km = km_with_bus + km_with_taxi
    total_cost = total_cost_bus + total_cost_taxi

    print(f"Total distance: {total_km:.2f}")
    print(f"Total cost: {total_cost:.2f}")


def exercise_3():
    hours = float(input("Отработени часове: "))
    hourly_pay = float(input("Заплащане на час: "))
    bonus_percent = float(input("Процент бонус: "))
    deduction_percent = float(input("Процент удръжка: "))

    salary = hours * hourly_pay
    salary += salary * bonus_percent / 100
    salary -= salary * deduction_percent / 100

    print(f"Крайно възнаграждение: {salary:.2f}")


def exercise_4():
    food_price = float(input("Enter the price of food: "))
    drink_price = float(input("Enter the price of drink: "))
    tax_percent = float(input("Enter the tax percentage: "))
    service_charge_percent = float(input("Enter the service charge percentage: "))
    people = int(input("Enter the number of people: "))

    price_with_tax = food_price + drink_price
    price_with_tax += price_with_tax * tax_percent / 100
    price_with_service_charge = price_with_tax * (
        1 + service_charge_percent / 100
    )
    price_per_person = price_with_service_charge / people

    print(f"Total price with tax and service charge: {price_with_service_charge:.2f}")
    print(f"Price per person: {price_per_person:.2f}")


def exercise_5():
    length = float(input("Enter the length of the parallelepiped: "))
    width = float(input("Enter the width of the parallelepiped: "))
    height = float(input("Enter the height of the parallelepiped: "))

    volume = length * width * height
    surface_area = 2 * (length * width + length * height + width * height)

    print(f"Volume of the parallelepiped: {volume:.2f}")
    print(f"Surface area of the parallelepiped: {surface_area:.2f}")


def exercise_6():
    liters1 = float(input("Enter the amount of the first liquid in liters: "))
    price1 = float(input("Enter the price of the first liquid per liter: "))
    liters2 = float(input("Enter the amount of the second liquid in liters: "))
    price2 = float(input("Enter the price of the second liquid per liter: "))

    total_liters = liters1 + liters2
    total_cost = liters1 * price1 + liters2 * price2
    average_price_per_liter = total_cost / total_liters

    print(f"Total liters: {total_liters:.2f}")
    print(f"Total cost: {total_cost:.2f}")
    print(f"Average price per liter: {average_price_per_liter:.2f}")


def exercise_7():
    distance = float(input("Enter the distance in kilometers: "))
    speed = float(input("Enter the speed in kilometers per hour: "))
    rest_minutes = int(input("Enter the rest time in minutes: "))

    travel_time_hours = distance / speed
    total_time_hours = travel_time_hours + rest_minutes / 60

    print(f"Total travel time: {total_time_hours:.2f} hours")


def exercise_8():
    length_room = float(input("Enter the length of the room in meters: "))
    width_room = float(input("Enter the width of the room in meters: "))
    height_room = float(input("Enter the height of the room in meters: "))
    doors_windows_area = float(
        input("Enter the total area of doors and windows in square meters: ")
    )
    paint_coverage_per_liter = float(
        input("Enter the paint coverage per liter in square meters: ")
    )
    price_per_liter = float(input("Enter the price of paint per liter: "))

    walls_area = 2 * (length_room + width_room) * height_room
    paintable_area = walls_area - doors_windows_area
    liters_needed = paintable_area / paint_coverage_per_liter
    total_cost = liters_needed * price_per_liter

    print(f"Liters of paint needed: {liters_needed:.2f} liters")
    print(f"Total cost of paint: {total_cost:.2f} euros")


def exercise_9():
    grade1 = float(input("Enter the first grade: "))
    weight1 = float(input("Enter the weight of the first grade (as a percentage): "))
    grade2 = float(input("Enter the second grade: "))
    weight2 = float(input("Enter the weight of the second grade (as a percentage): "))
    grade3 = float(input("Enter the third grade: "))
    weight3 = float(input("Enter the weight of the third grade (as a percentage): "))

    final_average_grade = (
        grade1 * weight1 / 100
        + grade2 * weight2 / 100
        + grade3 * weight3 / 100
    )

    print(f"Final average grade: {final_average_grade:.2f}")


def exercise_10():
    starting_sum = float(input("Enter the starting sum: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    years = int(input("Enter the number of years: "))

    simple_interest = starting_sum * (interest_rate / 100) * years
    final_amount = starting_sum + simple_interest

    print(f"Simple interest: {simple_interest:.2f}")
    print(f"Final amount after {years} years: {final_amount:.2f}")


def exercise_11():
    total_seconds = int(input("Enter the total number of seconds: "))
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    print(f"Time: {hours} hours, {minutes} minutes, {seconds} seconds")


def exercise_12():
    length = float(input("Enter the length of the floor in meters: "))
    width = float(input("Enter the width of the floor in meters: "))
    tile_area = float(input("Enter the area of one tile in square meters: "))
    reserve_percent = float(input("Enter the reserve percentage for broken tiles: "))
    price_per_tile = float(input("Enter the price of one tile: "))

    floor_area = length * width
    area_with_reserve = floor_area * (1 + reserve_percent / 100)
    tiles_needed = math.ceil(area_with_reserve / tile_area)
    total_cost = tiles_needed * price_per_tile

    print(f"Total tiles needed (including reserve): {tiles_needed}")
    print(f"Total cost: {total_cost:.2f} euros")


def exercise_13():
    power_watts = float(input("Enter the power of the device in watts: "))
    hours_per_day = float(input("Enter the number of hours the device is used per day: "))
    days = int(input("Enter the number of days: "))
    price_per_kwh = float(input("Enter the price of electricity per kWh: "))

    power_kw = power_watts / 1000
    total_energy_kwh = power_kw * hours_per_day * days
    total_cost = total_energy_kwh * price_per_kwh

    print(f"Total energy consumed: {total_energy_kwh:.2f} kWh")
    print(f"Total cost of electricity: {total_cost:.2f} euros")


def exercise_14():
    distance1 = float(input("Enter the distance of the first trip in kilometers: "))
    speed1 = float(input("Enter the speed of the first trip in kilometers per hour: "))
    distance2 = float(input("Enter the distance of the second trip in kilometers: "))
    speed2 = float(input("Enter the speed of the second trip in kilometers per hour: "))

    time1 = distance1 / speed1
    time2 = distance2 / speed2
    total_distance = distance1 + distance2
    total_time = time1 + time2
    average_speed = total_distance / total_time

    print(f"Total time: {total_time:.2f} hours")
    print(f"Average speed: {average_speed:.2f} km/h")


def exercise_15():
    products_sold = int(input("Enter the number of products sold: "))
    selling_price_per_product = float(input("Enter the selling price per product: "))
    cost_price_per_product = float(input("Enter the cost price per product: "))
    additional_expenses = float(input("Enter any additional expenses: "))

    revenue = products_sold * selling_price_per_product
    total_cost = products_sold * cost_price_per_product + additional_expenses
    profit = revenue - total_cost

    print(f"Total revenue: {revenue:.2f} euros")
    print(f"Total cost: {total_cost:.2f} euros")
    print(f"Profit: {profit:.2f} euros")


EXERCISES = {
    "1": exercise_1,
    "2": exercise_2,
    "3": exercise_3,
    "4": exercise_4,
    "5": exercise_5,
    "6": exercise_6,
    "7": exercise_7,
    "8": exercise_8,
    "9": exercise_9,
    "10": exercise_10,
    "11": exercise_11,
    "12": exercise_12,
    "13": exercise_13,
    "14": exercise_14,
    "15": exercise_15,
}


def main():
    print("Available exercises: 1-15")
    exercise_number = input("Choose an exercise: ")
    exercise = EXERCISES.get(exercise_number)

    if exercise is None:
        print("Invalid exercise number.")
        return

    exercise()


if __name__ == "__main__":
    main()
