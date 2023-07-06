# (1):-Hello, World!: Write a Python program that prints "Hello, World!" to the console.
print("------------------------answer-1---------------------------")
print("Hello World!")


# (2):-2. **Data Type Play**: Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.
    # - *Input*: None
    # - *Output*: "Type of variable1: <class 'int'>, value: 10..."
print("------------------------answer-2---------------------------")

# Integer
my_integer = 10
print("Integer - Value:", my_integer, "Type:", type(my_integer))

# Float
my_float = 3.14
print("Float - Value:", my_float, "Type:", type(my_float))

# String
my_string = "Hello, World!"
print("String - Value:", my_string, "Type:", type(my_string))

# Boolean
my_boolean = True
print("Boolean - Value:", my_boolean, "Type:", type(my_boolean))

# List
my_list = [1, 2, 3, 4, 5]
print("List - Value:", my_list, "Type:", type(my_list))

# Tuple
my_tuple = (6, 7, 8, 9, 10)
print("Tuple - Value:", my_tuple, "Type:", type(my_tuple))

# Dictionary
my_dictionary = {"name": "John", "age": 25, "city": "New York"}
print("Dictionary - Value:", my_dictionary, "Type:", type(my_dictionary))

# Set
my_set = {1, 2, 3, 4, 5}
print("Set - Value:", my_set, "Type:", type(my_set))



# 3. **List Operations**: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
#     - *Input*: None
#     - *Output*: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]..."
print("------------------------answer-3---------------------------")

# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))
print("Original List:", numbers)

# Add a number to the list
numbers.append(11)
print("List after adding a number:", numbers)

# Remove a number from the list
numbers.remove(3)
print("List after removing a number:", numbers)

# Sort the list in ascending order
numbers.sort()
print("List after sorting in ascending order:", numbers)


# 4. **Sum and Average**: Write a Python program that calculates and prints the sum and average of a list of numbers.
#     - *Input*: [10, 20, 30, 40]
#     - *Output*: "Sum: 100, Average: 25.0"

print("------------------------answer-4---------------------------")

def calculate_sum(numbers):
    total = sum(numbers)
    return total

def calculate_average(numbers):
    total = calculate_sum(numbers)
    average = total / len(numbers)
    return average

# Example list of numbers
my_numbers = [10, 20, 30, 40, 50]

# Calculate and print the sum
sum_result = calculate_sum(my_numbers)
print("Sum:", sum_result)

# Calculate and print the average
average_result = calculate_average(my_numbers)
print("Average:", average_result)


# 5. **String Reversal**: Write a Python function that takes a string and returns the string in reverse order.
#     - *Input*: "Python"
#     - *Output*: "nohtyP"

print("------------------------answer-5---------------------------")
def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

# Example usage
my_string = "Ashish"
reversed_string = reverse_string(my_string)
print(reversed_string)


# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"

print("------------------------answer-6---------------------------")

def count_vowels(input_string):
    vowel_count = 0
    vowels = "aeiouAEIOU"

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

# Example usage
my_string = "Hello"
vowel_count = count_vowels(my_string)
print("Number of vowels:", vowel_count)

# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."

print("------------------------answer-7---------------------------")

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

# Example usage
my_number = 12
if is_prime(my_number):
    print(my_number, "is a prime number")
else:
    print(my_number, "is not a prime number")


# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."

print("------------------------answer-8---------------------------")

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

# Example usage
my_number = 5
result = factorial(my_number)
print("Factorial of", my_number, "is", result)


# 9. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.
#     - *Input*: 5
#     - *Output*: "[0, 1, 1, 2, 3]"

print("------------------------answer-9---------------------------")

def fibonacci_numbers(n):
    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence

# Example usage
n = 5
fib_numbers = fibonacci_numbers(n)
print(fib_numbers)


# 10. **List Comprehension**: Use list comprehension to create a list of the squares of the numbers from 1 to 10.
#     - *Input*: None
#     - *Output*: "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"

print("------------------------answer-10---------------------------")


squares = []
for num in range(1, 11):
    squares.append(num ** 2)

print(squares)
