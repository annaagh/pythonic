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
        index = indices[i]
        length = lengths[i]
        substring_list.append(string[index:index+length])

    # short way --> substrings = [string[i:i + l] for i, l in zip(indices, lengths)]
    return substring_list


string = "abcdefghij"
indices = [1, 4, 6]
lengths = [3, 2, 4]
print(extract_substrings(string, indices, lengths))  # Output: ['bcd', 'ef', 'ghij']


