def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    if all(num == 0 for num in numbers):
        return 0 # Handle list with all zeros
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = []
result = calculate_average(my_list)
print(f"Average: {result}")

my_list = [1, 2, 3, 0]
result = calculate_average(my_list)
print(f"Average: {result}")

my_list = [0,0,0]
result = calculate_average(my_list)
print(f"Average: {result}")

my_list = [1,2,3,4,5]
result = calculate_average(my_list)
print(f"Average: {result}") 