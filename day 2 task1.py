def process_numbers(numbers):
    ascending = sorted(numbers)
    descending = sorted(numbers, reverse=True)
    print("Original:", numbers)
    print("Ascending:", ascending)
    print("Descending:", descending)
my_numbers = [12, 5, 7, 20, 1]
process_numbers(my_numbers)
