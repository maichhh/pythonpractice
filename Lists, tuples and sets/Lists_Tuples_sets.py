import itertools

# -------
# multiplies all the items in a list by the value of the variable factor.
# The program should also allow multiplying the variable factor by a string in case the list contains strings.
# Option 1
# -------
import math


def multiply_list_elements(my_list):
    factor = 2

    for i in range(len(my_list)):
        my_list[i] *= factor

    print(my_list)


# -------
# multiplies all the items in a list by the value of the variable factor.
# # Enumerate returns the index and value of each list item. [(0,3),(1,5),(2,7),(3,9)]
# Option 2
# -------


def multiply_list_elements_2(my_list):
    factor = 2

    for i, elem in enumerate(my_list):
        my_list[i] = elem * factor

    print(my_list)


# -------
# Print Elements on the Same Line Without Commas
# Option 1
# -------


def print_on_same_line(my_list):
    for elem in my_list:
        print(elem, end=" ")


# -------
# Print Elements on the Same Line Without Commas
# Use * to unpack
# Option 2
# -------


def print_on_same_line_2(my_list):
    print(*my_list, sep=" ")


# -------
# Get Max and Min Values
# Option 1
# -------


def get_max_min_value(my_list):
    if my_list:
        print(max(my_list), min(my_list))

    else:
        print(None)


# -------
# Check if List is Empty or Not
# Option 1
# -------


def list_is_empty(my_list):
    if len(my_list) == 0:
        print("Empty")

    else:
        print("Not empty")


# -------
# Check if List is Empty or Not
# Option 2
# -------


def list_is_empty_2(my_list):
    if not my_list:
        print("Empty")

    else:
        print("Not empty")


# -------
# Print the Elements and Their Indices
# Option 1
# -------


def print_elem_and_index(my_list):
    if not my_list:
        print("Empty")

    else:
        for i in range(len(my_list)):
            print(my_list[i], i)


# -------
# Print the Elements and Their Indices
# Option 2
# -------


def print_elem_and_index_2(my_list):
    if not my_list:
        print("Empty")

    else:
        for i, elem in enumerate(my_list):  # index and its element
            print(elem, i)


# -------
# Remove Matching Element
# Option 1
# Count() method for no. of occurences of an element
# my_list.remove only removes the 1st iteration of the element
# -------


def remove_element(my_list):
    elem_to_remove = 3

    if not my_list:
        print("Empty list")
    elif my_list.count(elem_to_remove) == 0:
        print("Not found")
    else:
        for i in range(my_list.count(elem_to_remove)):
            my_list.remove(
                elem_to_remove)  # removes only the first occurrence of the element so we have to invoke it severally

    print(my_list)


# -------
# Remove Duplicates from a List
# Sets are commonly used to remove duplicates from lists and tuples in Python.
# Sets do not preserve the order of the elements
# Option 1
# -------


def remove_duplicates(my_list):
    no_duplicates = list(set(my_list))  # create a set then form a list
    print(no_duplicates)


# -------
# Remove Duplicates from a List
# Sets are commonly used to remove duplicates from lists and tuples in Python.
# Sets do not preserve the order of the elements
# Option 2
# -------


def remove_duplicates_2(my_list):
    no_duplicates = list(dict.fromkeys(my_list))  # this will ensure the order of elems is preserved
    # a dictionary is created {1: None, 2: None, 3: None, ...}
    # Then cast the dictionary into a list
    print(no_duplicates)


# -------
# Count Elements Greater than 3
# Option 1
# -------
my_list = [3, 5, 7, 9, 8, 0]


def count_elems_greater_than_three(my_list):
    count = 0

    for elem in my_list:
        if elem > 3:
            count += 1
    print(count)


# -------
# Count Elements Greater than 3
# Option 2
# Generator expression
# -------


def count_elems_greater_than_three_2(my_list):
    count = sum(1 for elem in my_list if elem > 3)  # add 1 for every elm > 3

    print(count)


# -------
# Find the Intersection of Two Sets
# Another set with elements that are common to the 2 sets
# Option 1
# -------


def set_intersection(my_list):
    set1 = {1, 2, 3, 4, 6}
    set2 = {1, 2, 5, 6}
    intersection = set()  # to create empty set

    for elem in set1:
        if elem in set2:
            intersection.add(elem)

    print(intersection)


# -------
# Find the Intersection of Two Sets
# Another set with elements that are common to the 2 sets
# Option 2
# -------


def set_intersection_2(my_list):
    set1 = {1, 2, 3, 4, 6}
    set2 = {1, 2, 5, 6}
    set3 = {3, 4, 5, 1}

    print(set1.intersection(set2, set3))


# -------
# Difference Between Two Lists
# Print (as a list) the elements of listA that are not in listB
# Option 1
# -------


def list_difference(my_list):
    listA = [1, 2, 3, 4]
    listB = [3, 4]
    difference = []

    for elem in listA:
        if elem not in listB:
            difference.append(elem)

    print(difference)


# -------
# Distance Between Two 3D Points
# The points are represented by two lists with three elements. The first element is the x-coordinate.
# The second element is the y-coordinate. The third element is the z-coordinate.
# sqrt(square(x2-x1) + square(y2-y1) + square(z2-z1)
# Option 1
# -------


def dist_between_2_3D_points(my_list):
    pointA = [3, 4, 5]
    pointB = [2, 2, 4]

    distance = ((pointA[0] - pointB[0]) ** 2
                + (pointA[1] - pointB[1]) ** 2
                + (pointA[2] - pointB[2]) ** 2) ** (1 / 2)

    print(distance)


# -------
# Distance Between Two 3D Points
# The points are represented by two lists with three elements. The first element is the x-coordinate.
# The second element is the y-coordinate. The third element is the z-coordinate.
# sqrt(square(x2-x1) + square(y2-y1) + square(z2-z1)
# Option 2
# -------


def dist_between_2_3D_points_2(my_list):
    pointA = [3, 4, 5]
    pointB = [3, 3, 4]

    addition = ((pointA[0] - pointB[0]) ** 2
                + (pointA[1] - pointB[1]) ** 2
                + (pointA[2] - pointB[2]) ** 2) ** (1 / 2)
    distance = math.sqrt(addition)

    print(distance)


# -------
# Print Common Elements in Two Lists
# Option 1
# -------


def common_elems(my_list):
    listA = [3, 4, 5]
    listB = [3, 3, 4]
    common = []

    for elem in listA:
        if elem in listB:
            common.append(elem)
    print(common)


# -------
# Find the Second Largest Value in a List
# Option 1
# -------


def second_largest_elem(my_list):
    listA = [3, 4, 5, 1]

    if len(listA) > 1:
        sorted_list = sorted(listA)
        print(sorted_list[-2])
    else:
        print(None)


# -------
# Find the Second Largest Value in a List
# Option 2
# -------


def second_largest_elem_2(my_list):
    listA = [3, 4, 5, 1]

    if len(listA) > 1:
        no_duplicates = set(listA)  # Convert it to a set
        no_duplicates.remove(max(no_duplicates))  # remove the largest element
        print(max(no_duplicates))  # print the max. Second largest
    else:
        print(None)


# -------
# Find the Second Smallest Value in a List
# Option 1
# -------


def second_smallest_elem(my_list):
    listA = [3, 4, 5, 1]

    if len(listA) > 1:
        no_duplicates = set(listA)  # Convert it to a set
        no_duplicates.remove(min(no_duplicates))  # remove the smallest element
        print(min(no_duplicates))  # print the min. Second smallest
    else:
        print(None)


# -------
# Find the Second-Smallest Value in a List
# Option 2
# -------


def second_smallest_elem_2(my_list):
    listA = [3, 4, 5, 1]

    if len(listA) > 1:
        sorted_list = sorted(listA)  # Returns a new copy of the list
        print(sorted_list[1])
    else:
        print(None)


# -------
# Make a Frequency Dictionary from the Elements of a List
# The test should be case-sensitive. Therefore, "A" should not be considered the same element as "a"

# Option 1
# -------


def frequency_dictionary(my_list):
    listA = ["a", "b", "a", "a", "c", "b", "A"]
    freq_dict = {}  # This creates an empty dictionary

    for elem in listA:
        if elem not in freq_dict:
            freq_dict[elem] = 1  # Add the element to the dictionary and initialize its occurrence to 1. Key and value
        else:
            freq_dict[elem] += 1  # Increment the occurrence (value) of the element

    print(freq_dict)


# -------
# Flatten a List that Contains Lists
# "Flattened" means that all the elements in the nested lists should be added to a main list such that it doesn't
# contain any nested lists, just the individual.
# The list could contain other elements that are not lists or other sequences, so you must check the type of each
# element and act appropriately.

# Option 1
# -------


def flattened_list(my_list):
    listA = [7, [5, 6, 0, 7], [1, 2, 3], [7, 8, 9], "a"]  # [7, 5, 6, 0, 7, 1, 2, 3, 7, 8, 9, 'a']
    flat_list = []

    for elem in listA:
        if isinstance(elem, list):  # if the elem is a 'list'
            for nested_elem in elem:
                flat_list.append(nested_elem)
        else:
            flat_list.append(elem)  # you append the elem directly to the flattened version.

    print(flat_list)


# -------
# Generate all Permutations of a List
# Permutation is a possible arrangement of the list elements. For example, [2, 1, 3] is a permutation of [1, 2, 3].
# Include the list itself as a permutation.
# The permutations function of the itertools module can be very helpful to solve this exercise.
# You can import this module with import itertools
# Option 1
# -------


def permutation_list(my_list):
    listA = [7, 8, 9, 1]
    # iterable is a variable than you can use in a loop. A list is an iterable.

    permutations = list(itertools.permutations(listA))  # returns a sequence with all the different permutations of list
    # casts it into a list
    for permutation in permutations:  # To print each permutation in a new line
        print(permutation)


# -------
# Generate all Permutations of a List
# Refactored version without the intermediate variable
# Permutation is a possible arrangement of the list elements. For example, [2, 1, 3] is a permutation of [1, 2, 3].
# Include the list itself as a permutation.
# The permutations function of the itertools module can be very helpful to solve this exercise.
# You can import this module with import itertools
# Option 2
# -------


def permutation_list_2(my_list):
    listA = [7, 8, 9, 1]
    # iterable is a variable than you can use in a loop. A list is an iterable.

    for permutation in list(itertools.permutations(listA)):  # To print each permutation in a new line
        print(list(
            permutation))  # will print them as list not tuples. TUPLES ARE IMMUTABLE. Can be used when we don't need to modify the list.


permutation_list_2(my_list)
