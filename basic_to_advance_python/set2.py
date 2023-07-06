### Problem **1: Print the following pattern**

# Write a program to print the following number pattern using a loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

print("------------------solution-1--------------------")

n = 5

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


### Problem **2: Display numbers from a list using loop**

# Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions

# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop

# **Given**:

# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```

# **Expected output:**
# 75
# 150
# 145


print("------------------solution-2--------------------")


numbers =  [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num % 5 == 0:
        if num > 500:
            break
        elif num > 150:
            continue
        else:
            print(num)



### Problem **3: Append new string in the middle of a given string**

# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.

# **Given**:

# ```
# s1 = "Ault"
# s2 = "Kelly"
# ```

# **Expected Output**:AuKellylt

print("------------------solution-3--------------------")

def append_in_middle(s1, s2):
    middle_index = len(s1) // 2
    s3 = ""

    for i in range(len(s1)):
        if i == middle_index:
            s3 += s2
        s3 += s1[i]

    return s3

# Example usage
s1 = "Ault"
s2 = "Kelly"
s3 = append_in_middle(s1, s2)
print(s3)



### Problem **4: Arrange string characters such that lowercase letters should come first**

# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

# **Given**:

# ```
# str1 = PyNaTive
# ```

# **Expected Output**:yaivePNT


print("------------------solution-4--------------------")

def arrange_characters(string):
    lower_chars = ""
    upper_chars = ""

    for char in string:
        if char.islower():
            lower_chars += char
        else:
            upper_chars += char

    arranged_string = lower_chars + upper_chars
    return arranged_string

# Example usage
input_string = "PyNaTive"
arranged_string = arrange_characters(input_string)
print(arranged_string)



### Problem **5: Concatenate two lists index-wise**

# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# **Given**:

# ```
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# ```

# **Expected output:**

# ```
# ['My', 'name', 'is', 'Kelly']
# ```
print("------------------solution-5--------------------")


def concatenate_lists(list1, list2):
    result = []
    min_length = min(len(list1), len(list2))

    for i in range(min_length):
        concatenated_value = str(list1[i]) + str(list2[i])
        result.append(concatenated_value)

    return result

# Example usage
list1 = ["M", "na", "i", "Ke"]
list2 =["y", "me", "s", "lly"]
concatenated_list = concatenate_lists(list1, list2)
print(concatenated_list)

# 6- Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"] 
# output:-['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']


print("------------------solution-6--------------------")

def concatenate_lists(list1, list2):
    result = []

    for word1 in list1:
        for word2 in list2:
            concatenated_value = word1 + word2
            result.append(concatenated_value)

    return result

# Example usage
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
concatenated_list = concatenate_lists(list1, list2)
print(concatenated_list)


### Problem **7: Iterate both lists simultaneously**

# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

# **Given**

# ```
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# ```

# **Expected output:**
# 10 400
# 20 300
# 30 200
# 40 100


print("------------------solution-7--------------------")

def iterate_lists(list1, list2):
    reversed_list2 = list2[::-1]  # Reverse the order of list2

    for item1, item2 in zip(list1, reversed_list2):
        print(item1, item2)

# Example usage
list1 =[10, 20, 30, 40]
list2 = [100, 200, 300, 400]
iterate_lists(list1, list2)


# 8-nitialize dictionary with default values**

# In Python, we can initialize the keys with the same values.


# ```
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# ```

# **Expected output:**{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}


print("------------------solution-8--------------------")

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

employee_dict = {employee: defaults for employee in employees}
print(employee_dict)


### Problem **9: Create a dictionary by extracting the keys from a given dictionary**

# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# **Given dictionary**:

# ```
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]
# ```

# **Expected output:**{'name': 'Kelly', 'salary': 8000}
print("------------------solution-9--------------------")

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys = ["name", "salary"]

new_dict = {key: sample_dict[key] for key in keys if key in sample_dict}
print(new_dict)


### Problem **10: Modify the tuple**

# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222

# **Given**:tuple1 = (11, [22, 33], 44, 55)
# output :-tuple1: (11, [222, 33], 44, 55)
print("------------------solution-10--------------------")
tuple1 = (11, [22, 33], 44, 55)

# Convert the tuple to a list
list1 = list(tuple1)

# Modify the first item of the list
list1[1][0] = 222

# Convert the modified list back to a tuple
tuple1 = tuple(list1)

print("tuple1:", tuple1)
