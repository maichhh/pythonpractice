import string


def print_string_length(s):
    # prints the length of the string
    # returns number of items of an object
    print(len(s))


# print_string_length(s)


def print_character_at_index(i):
    if len(s) == 0:
        print("Empty string")
    elif i < len(s):  # Since we start index at zero
        print(s[i])
    else:
        print("i out of range")


# print_character_at_index(3)

def print_character_at_index_option2(i):
    if not s:  # Truthy value. returns TRUE when s is EMPTY
        print("Empty string")
    elif i < len(s):
        print(s[i])
    else:
        print("i out of range")


# print_character_at_index_option2(0)

def reverse_string_1(s):
    # string slicing
    # string[start:stop:step]
    print(s[::-1])


# reverse_string_1(s)

def reverse_string_2(s):
    # use reversed() to reverse string
    # and join them with an empty string
    # anything else added to join will be used to join the characters
    reversed_word = "".join(reversed(s))
    print(reversed_word)


# reverse_string_2(s)


# -------
# Print first and last x characters
# Option 1
# -------


def first_and_last_3(s):
    if len(s) < 6:
        print("")
    else:
        # s[0:3] same as s[:3] --> from index 0 to 3 without including 3.
        # s[len(s) - 3:]---> default value is continuing until end of the string. Char at index 'len(s) - 3' is included
        new_string = s[:3] + s[len(s) - 3:]
        print(new_string)


# first_and_last_3(s)

# -------
# Print first and last x characters
# Option 2
# -------

def first_and_last_characters_2(s):
    # This approach makes modification and maintenance easier and faster. We update the value only once
    num_chars = 4
    if len(s) < num_chars * 2:
        print("")
    else:
        # s[0:3] same as s[:3] --> from index 0 to 3 without including 3.
        new_string = s[:num_chars] + s[len(s) - num_chars:]
        print(new_string)


# -------
# Print the string without the characters located at even indices.
# Option 1
# -------


def omit_chars_at_even_indices(s):
    # Strings are immutable, so we have to create a new string
    # range by default starts the sequence from 0 to len(s) -1
    new_string = ""
    for i in range(len(s)):
        if i % 2 != 0:
            new_string += s[i]

    print(new_string)


# -------
# Print the string without the characters located at even indices.
# Option 2
# -------


def omit_chars_at_even_indices_2(s):
    # use range to generate only the odd indices
    new_string = ""
    # from 1 to len(s) - 1, while incrementing by 2
    for i in range(1, len(s), 2):
        # 1,3,5,.., len(s)-1
        new_string += s[i]

    print(new_string)


# -------
# Check string contains numbers only
#
# -------


def check_string_contains_only_nums(s):
    # The .isdecimal() method returns True if all the characters in the string are digits.
    # an empty string returns false
    # 7.897 returns false
    print(s.isdecimal())


# -------
# Remove nth Character from a String
# Option 1
# -------


def remove_char_nth_index(s):
    n = 7
    # empty string and out of range
    if len(s) == 0 or n >= len(s):
        print(s)
    else:
        # add the char to new string if it is not n
        new_s = ""
        for i in range(len(s)):
            if i != n:
                new_s += s[i]
        print(new_s)


# -------
# Remove nth Character from a String
# Option 2
# -------


def remove_char_nth_index_2(s):
    n = 7
    # we use (not s) to return true when string is empty
    if not s or n >= len(s):
        print(s)
    else:
        # add the char to new string if it is not n
        new_s = ""
        for i in range(len(s)):
            if i != n:
                new_s += s[i]
        print(new_s)


# -------
# Replace a Character in a String. Replace curr_char with new_char
# Option 1
# -------


def replace_current_char(s):
    new_string = ""
    curr_char = "Z"
    new_char = "ry"

    # for every character in string s
    for char in s:
        if char == curr_char:
            new_string += new_char
        else:
            new_string += char

    print(new_string)


# -------
# Replace a Character in a String. Replace curr_char with new_char
# Option 2
# Use in built method
# -------

s = "Z46uy8"


def replace_current_char_2(s):
    curr_char = "Z"
    new_char = "!ry"

    print(s.replace(curr_char, new_char))


# -------
# Replace comma with dot
# Option 1
# -------


def replace_comma_with_dot(s):
    new_s = ""
    comma = ","
    dot = "."

    for char in s:
        if char == comma:
            new_s += dot
        else:
            new_s += char
    print(new_s)


# -------
# Check if string contains all letters of the alphabet (PANGRAM)
# Option 1
# -------


def string_contains_all_alphabets(s):
    set_s = set(s.lower())
    SPACE = " "

    # Check space is available in the set before removing it
    if SPACE in set_s:
        set_s.remove(" ")  # Remove spaces from the set. Will fail if s has no spaces.

    # Convert string into a set to remove duplicate characters and
    # order. Compare this set with the set of letters in the constant.(string.ascii_lowercase)

    print(set_s == set(string.ascii_lowercase))


# -------
# Check if string contains all letters of the alphabet (PANGRAM)
# Option 2
# -------


def string_contains_all_alphabets_2(s):
    is_pangram = True

    for char in string.ascii_lowercase:
        if char not in s.lower():
            is_pangram = False

    print(is_pangram)


# -------
# Check if string contains all letters of the alphabet (PANGRAM)
# Option 3. use break to improve its performance
# -------

s = "QWTFH KO Veyuiopsdfghjklmnbvcxz"


def string_contains_all_alphabets_3(s):
    is_pangram = True

    for char in string.ascii_lowercase:
        if char not in s.lower():
            is_pangram = False
            break  # Stop loop immediately

    print(is_pangram)


# -------
# Remove Spaces from a String
# Option 1
# -------


def string_copy_without_spaces(s):
    new_s = ""
    for char in s:
        if char != " ":
            new_s += char

    print(new_s)


# -------
# Remove Spaces from a String
# Option 2
# Use replace
# -------


def string_copy_without_spaces_2(s):
    print(s.replace(" ", ""))


# -------
# Check if a String Starts with a Prefix
# Option 1
# -------


def string_starts_with_prefix(s):
    prefix = "He"
    # Python slicing returns the whole string if the end is greater than the length of the string being sliced
    print(s[:len(prefix)] == prefix)


# -------
# Check if a String Starts with a Prefix
# Option 2
# use startswith() method
# Recommended by python developers
# -------


def string_starts_with_prefix_2(s):
    prefix = "Het"
    print(s.startswith(prefix))


# -------
# Check if a String Ends with a Suffix
# Option 1
# -------

s = "HeTFH KO Vertyuiopasdfghjklmnbvcxz"


def string_ends_with_suffix(s):
    suffix = "Het"
    print(s.startswith(suffix))


# -------
# Check if a String ends with suffix
# Option 2
# -------


def string_ends_with_suffix_2(s):
    suffix = "ello"
    # Python slicing returns the whole string if the end is greater than the length of the string being sliced
    # the last character of a string is at index -1, and we can decrement as we move leftwards -2, -3, -4 ....
    print(s[-len(suffix):] == suffix)


# -------
# Reverse Words in a String and changes their case
# Option 1
# -------


def reverse_and_change_case(s):
    word = "heLLo world"
    new_word = ""
    word_list = word.split(" ")  # ["Hello","world"]

    for word in word_list:
        reversed_word = "".join(reversed(word))
        swapped_case = reversed_word.swapcase()
        new_word += swapped_case + " "

    new_word = new_word.rstrip()  # remove the spaces at the end of the string
    print(new_word)


# -------
# Count Repeated Characters
# Option 1
# -------


def count_repeated_chars(s):
    s = "heLLhhwwo world"
    repeated_count = 0
    repeated_chars = []

    for char in s:
        if (s.count(char) > 1) and (char not in repeated_chars):
            repeated_count += 1
            repeated_chars.append((char))

    print(repeated_count)

    if len(repeated_chars) > 0:
        for char in sorted(repeated_chars):  # Sorted in alphabetical order
            print(char, end=" ")

    else:
        print(None)


# -------
# Count Repeated Characters
# Option 2
# -------


def count_repeated_chars_2(s):
    s = "heLLhhwwo world"
    repeated_count = 0
    repeated_chars = []

    for char in s:
        if (s.count(char) > 1) and (char not in repeated_chars):
            repeated_count += 1
            repeated_chars.append((char))

    print(repeated_count)

    if repeated_chars:
        # unpacking (*) : Print the items in the list one by one, avoid loop separated by space " "
        print(*sorted(repeated_chars), sep=" ")

    else:
        print(None)


# -------
# Count Repeated Characters
# Option 3
# without using the counter
# use the length of the string
# -------


def count_repeated_chars_3(s):
    s = "heLLhhwwo world"

    repeated_chars = []

    for char in s:
        if (s.count(char) > 1) and (char not in repeated_chars):
            repeated_chars.append((char))

    print(len(repeated_chars))

    if repeated_chars:
        # unpacking (*) : Print the items in the list one by one, avoid loop separated by space " "
        print(*sorted(repeated_chars), sep=" ")

    else:
        print(None)


# -------
# Sort Words in Alphabetical Order (*)
# Option 1
# sort the characters of each word in alphabetical order
# use the length of the string
# -------


def sort_alphabetical_order(s):
    s = "heLLhhwwo world"
    new_s = ""
    word_list = s.split(" ")  # split the words to a new list

    for word in word_list:
        lowercase_word = word.lower()
        sorted_word = "".join(sorted(lowercase_word))  # Sorts in alphabetical order
        new_s += sorted_word + " "  # also adds a space after the last word

    new_s.rstrip()  # to remove space at end

    print(new_s)


# -------
# Sort Words in Alphabetical Order (*)
# Option 1
# sort the characters of each word in alphabetical order
# use the length of the string
# -------
""" Fails --> prints only the last word """


def sort_alphabetical_order_2(s):
    s = "hello world"
    new_s = ""
    word_list = s.split(" ")  # split the words to a new list

    for word in word_list:
        new_s = "".join(sorted(word.lower())) + " "  # More comapct and avoids creating too many variables

    new_s.rstrip()  # to remove space at end

    print(new_s)


sort_alphabetical_order(s)
