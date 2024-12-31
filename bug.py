def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = []
result = calculate_average(my_list)
print(f"Average: {result}") # This will print 0 as expected

my_list = [1, 2, 3, 0]
result = calculate_average(my_list)
print(f"Average: {result}") # This will throw ZeroDivisionError if 0 is present in the list and not handled

my_list = [1,2,3,4,5]
result = calculate_average(my_list)
print(f"Average: {result}")