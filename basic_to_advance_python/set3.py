# 1. **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
#     - *Input*: [("John", 25), ("Jane", 30)]
#     - *Output*: "John is 25 years old. Jane is 30 years old."

print("=====answer-1===========")

people = [("John", 25), ("Jane", 30)]

output = ""
for name, age in people:
    output += f"{name} is {age} years old. "

output = output.rstrip(". ")
print(output)

# 2. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"


print("=====answer-2===========")

def add_name_age(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, age):
    if name in dictionary:
        dictionary[name] = age

def delete_name(dictionary, name):
    if name in dictionary:
        del dictionary[name]

# Example dictionary
person_dict = {}

# Add a name-age pair
add_name_age(person_dict, "John", 25)
print(person_dict)  # {'John': 25}

# Update the age of a name
update_age(person_dict, "John", 26)
print(person_dict)  # {'John': 26}

# Delete a name from the dictionary
delete_name(person_dict, "John")
print(person_dict)  # {}

# 3. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"



print("=====answer-3===========")

def find_two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Example input
nums = [2, 7, 11, 15]
target = 9

# Find the two integers
result = find_two_sum(nums, target)

print(result)

# 4. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."



print("=====answer-4===========")

def check_palindrome(word):
    reversed_word = word[::-1]  # Reverse the word
    if word == reversed_word:
        return f"The word {word} is a palindrome."
    else:
        return f"The word {word} is not a palindrome."

# Example input
word = "madam"

# Check if the word is a palindrome
result = check_palindrome(word)

print(result)

# 5. **Selection Sort**: Implement the selection sort algorithm in Python.
#     - *Input*: [64, 25, 12, 22, 11]
#     - *Output*: "[11, 12, 22, 25, 64]"



print("=====answer-5===========")

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example input
arr = [64, 25, 12, 22, 11]

# Sort the array using selection sort
selection_sort(arr)

print(arr)


# 6. **Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"



print("=====answer-6===========")

from queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, value):
        self.q2.put(value)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1.empty():
            return self.q1.get()

# Test the Stack class
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 1



# 7. **FizzBuzz**: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".
#     - *Input*: None
#     - *Output*: "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16,..."




print("=====answer-7===========")

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# 8. **File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
#     - *Input*: A text file named "input.txt" with the content "Hello world"
#     - *Output*: A text file named "output.txt" with the content "Number of words: 2"



print("=====answer-8===========")

def count_words(input_file, output_file):
    # Read the input file
    with open(input_file, 'r') as file:
        content = file.read()

    # Count the number of words
    word_count = len(content.split())

    # Write the count to the output file
    with open(output_file, 'w') as file:
        file.write(f"Number of words: {word_count}")

# Example input and output file names
input_file = "input.txt"
output_file = "output.txt"

# Count words and write the count to the output file
count_words(input_file, output_file)

# *9. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."

print("=====answer-9===========")
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

# Example input
num1 = 5
num2 = 0

# Perform division and handle exceptions
result = divide_numbers(num1, num2)

print(result)
