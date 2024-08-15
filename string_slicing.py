# Solving python tasks using slicing

def reverse_words(string):
    """
    Reverse Words in a String Using Slicing
    :param string:
    :return:
    """

    str_list = string.split()
    str_list = str_list[::-1]

    return ' '.join(str_list)


# Example Usage
s = "Hello World"
print(reverse_words(s))  # Output: "World Hello"


def extract_substrings(string, indices, lengths):
    """
    Extract Substrings with Variable Lengths
    :param string:
    :param indices:
    :param lengths:
    :return:
    """
    substring_list = []
    for i, l in zip(indices, lengths):
        substring_list.append(string[i:i + l])

    # short way --> substrings = [string[i:i + l] for i, l in zip(indices, lengths)]
    return substring_list


string = "abcdefghij"
indices = [1, 4, 6]
lengths = [3, 2, 4]
print(extract_substrings(string, indices, lengths))  # Output: ['bcd', 'ef', 'ghij']


def is_palindrome(s):
    """
        Palindrome Check Using Slicing
    :param s:
    :return:
    """
    s = s.replace(" ", "").lower()
    return s == s[::-1]


# Example Usage
s = "A man a plan a canal Panama"
print(is_palindrome(s))  # Output: True


def custom_step_slice(s, index, step):
    """
        Function takes a string and returns every nth character starting from a given index.

    :param s:
    :return:
    """
    return s[index::step]


# Example Usage
string = "abcdefghij"
start_index = 1
step = 3
print(custom_step_slice(string, start_index, step))  # Output: "beh"


def circular_rotations(s):
    """
        All possible rotations of the string using slicing.
    :param s:
    :return:
    """
    return [s[i:] + s[:i] for i in range(len(s))]


s = "abcd"
print(circular_rotations(s))  # Output: ['abcd', 'bcda', 'cdab', 'dabc']


def manual_slice(s, start, end, step):
    """
        String Slicing Without Using Slicing
    :param s:
    :param start:
    :param end:
    :param step:
    :return:
    """
    output_list = []
    i = start
    while i < end:
        output_list.append(s[i])
        i += step
    return ''.join(output_list)


# Example Usage
string = "abcdefgh"
start = 2
end = 6
step = 2
print(manual_slice(string, start, end, step))  # Output: "ce"


def middle_characters(s):
    """
    Function that returns the middle character(s) of a string.
    If the string length is even, return the middle two characters; if odd, return the middle character.
    :param s:
    :return:
    """
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return s[mid - 1:mid + 1]
    else:
        return s[mid]


# Example Usage
s1 = "abcde"
s2 = "abcdef"
print(middle_characters(s1))  # Output: "c"
print(middle_characters(s2))  # Output: "cd"


def remove_nth_occurrence(s, subs, n):
    """
    Given a string, a substring, and an integer n,
    write a function to remove the n-th occurrence of the substring using slicing.
    :param s:
    :param subs:
    :param n:
    :return:
    """
    index = -1
    for _ in range(n):
        index = s.find(subs, index + 1)
        if index == -1:
            return None
    return s[:index] + s[index + len(subs) + 1:]


# Example Usage
string = "the cat in the hat"
substring = "the"
n = 2
print(remove_nth_occurrence(string, substring, n))  # Output: "the cat in hat"


def all_substrings(s):
    """
    Returns all possible substrings of a string using slicing.
    :param s:
    :return:
    """
    subs_list = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            subs_list.append(s[i:j])
    return subs_list


# Example Usage
s = "abc"
print(all_substrings(s))  # Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']
