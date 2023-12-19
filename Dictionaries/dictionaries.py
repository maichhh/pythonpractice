# -------
# Check if a Key Exists in a Dictionary
# The in operator can be very helpful to solve this challenge.
# -------


def key_exists_in_dictionary(my_dict):
    key = "c"

    print(key in my_dict)


# -------
# Add a Key-Value Pair Only if the Key is Not in the Dictionary
# You can use the not in operator to check if a key is not in a dictionary.
# Do not update the dict if the key already exists
# -------

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}


def add_pair_if_key_absent(my_dict):
    new_key = "z"
    new_value = 26

    if new_key not in my_dict:
        my_dict[new_key] = new_value

    print(my_dict)


# -------
# Merge Two Dictionaries
# "Merging" the dictionaries involves making a new dictionary with the key-value pairs in both dictionaries.
# Notice that the key-value pairs that share the same key on both dictionaries are not repeated.
# Dictionaries should not allow repeated keys.
# They are updated with the value of the second dictionary.
# -------


def merge_dictionaries(my_dict):
    merged_dict = my_dict_1 | my_dict_2  # my_dict_2 updates already existing keys in mydict_1

    print(merged_dict)


# -------
# Check if All Values are Equal
# The .values() method returns the values in a dictionary.
# You could also make a set from the dictionary to keep only one copy per value.
# Option 1
# -------

# my_dict_1 = {"a": 1, "b": 2, "c": 3, "d": 4}
my_dict_2 = {"h": 9, "i": 9, "j": 9, "a": 9}


def check_if_values_are_equal(my_dict):
    num_unique_values = len(set(my_dict_2.values()))  # sets don't have duplicates

    if num_unique_values == 0:
        print("Empty")
    elif num_unique_values == 1:
        print(True)
    else:
        print(False)  # Since not all values are equal


# -------
# Find the Maximum Value in a Dictionary
# The .values() method returns the values in a dictionary.
#
# -------


def dict_maximum_value(my_dict):
    num_unique_values = len(set(my_dict_2.values()))  # sets don't have duplicates

    if my_dict_1:
        max_value = max(set(my_dict_1.values()))  # to remove duplicates
        print(max_value)

    else:
        print(None)  # Since not all values are equal


# -------
# Find the Minimum Value in a Dictionary
# The .values() method returns the values in a dictionary.
#
# -------


def dict_minimum_value(my_dict):
    num_unique_values = len(set(my_dict_2.values()))  # sets don't have duplicates

    if my_dict_1:
        min_value = min(set(my_dict_1.values()))  # to remove duplicates
        print(min_value)

    else:
        print(None)  # Since not all values are equal


# -------
# Find Frequency of Values in a Dictionary
# Write a Python program that counts the frequency of each value in a dictionary.
# create a new dictionary to map each value in the original dictionary to its frequency.
# -------
my_dict_1 = {"a": 1, "b": 1, "c": 3, "d": 4}
freq_dict = {}


def find_value_frequency(my_dict):
    for value in my_dict_1.values():
        if value in freq_dict:
            freq_dict[value] += 1
        else:
            freq_dict[value] = 1
    print(freq_dict)


# -------
# Make a Dictionary from Nested Lists
# Each nested list has this format [value1, value2].
# value1 should be the key in the dictionary and value2 should be its corresponding value.
# -------
my_list = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]
new_dict = {}


def nested_list_dict(my_dict):
    for nested_list in my_list:
        key = nested_list[0]
        value = nested_list[1]
        new_dict[key] = value

    print(new_dict)


# -------
# Print the Max Sum of Values
# The sum() function returns the sum of the elements of a list or tuple.
# -------
my_dict = {
    "a": [1, 2, 3],
    "b": [4, 0, -4],
    "c": [3, 5, 9],
    "d": [45, 12, 190]
}


def max_value_sum_dict(my_dict):
    max_sum = None
    for list_value in my_dict.values():
        list_sum = sum(list_value)

        if max_sum is None:
            max_sum = list_sum
        elif max_sum < list_sum:
            max_sum = list_sum

    print(max_sum)


# -------
# Make a Frequency Dictionary for the Characters in a String
# Write a Python program that creates and displays a dictionary that maps each letter in a string to
# how many times the character occurs in the string (its frequency).
# The keys in the dictionary should be lowercase letters.
# Only add letters
# -------


def string_chars_frequency(my_dict):
    my_string = "Hhello, World"
    freq_dict = {}
    for char in my_string.lower():
        if char.isalpha():  # only alphabets
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1  # Initialize it to 1.

    print(freq_dict)

# -------
# Write a Python program that sorts (in ascending order) the lists contained as values in a dictionary.
# The .sort() method sorts a list (the list is mutated/changed#
# Using sorted()  only returns a sorted COPY of the list w/o modifying original one.
# -------


def sort_dict_ascending(my_dict):
    my_dict = {
        "a": [4, 3, 2, 8],
        "b": [5, 3, 7],
        "c": [1, 89, 10],
        "d": [3, 4, 1]
    }

    for list_value in my_dict.values():
        list_value.sort() # sort modifies it. We don't have to generate other dictionaries

    print(my_dict)

# -------
# Convert Dictionary into a List of Lists
# Write a Python program that takes the content of a dictionary and converts it into a list of lists.#
# Each nested list should contain a key as the first element and its corresponding value as the second element.
# The .items() dictionary method can be helpful to solve this exercise. It returns a sequence with the keys of the
# dictionary and their corresponding values.
# -------


def convert_dict_to_list_of_lists(my_dict):
    product_info = {
        "description": "shoe",
        "price": 4.56,
        "colors": ["green", "blue", "red"],
    }

    new_list= []

    for key, value in product_info.items():
        new_list.append([key, value])

    print(new_list)