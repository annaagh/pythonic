# string.py - Practice Python String Operations

# 1. Basic String Operations
def basic_operations():
    my_string = "Hello, Python!"
    print("Original String:", my_string)

    # Length of the string
    print("Length of the string:", len(my_string))

    # Accessing characters and slicing
    print("First character:", my_string[0])
    print("Last character:", my_string[-1])
    print("Slicing (0:5):", my_string[0:5])

    # String concatenation
    print("Concatenation:", my_string + " Let's learn strings.")

    # String repetition
    print("Repetition:", my_string * 3)


# 2. String Methods
def string_methods():
    my_string = " Hello, Python! "

    # Stripping whitespace
    print("Stripped string:", my_string.strip())

    # Converting to uppercase and lowercase
    print("Uppercase:", my_string.upper())
    print("Lowercase:", my_string.lower())

    # Checking start and end of the string
    print("Starts with 'Hello':", my_string.startswith("Hello"))
    print("Ends with '!':", my_string.endswith("!"))

    # Finding and counting substrings
    print("Find 'Python':", my_string.find("Python"))
    print("Count 'o':", my_string.count("o"))

    # Replace substring
    print("Replace 'Python' with 'World':", my_string.replace("Python", "World"))


# 3. String Formatting
def string_formatting():
    name = "Alice"
    age = 30

    # Using f-strings (Python 3.6+)
    print(f"My name is {name} and I am {age} years old.")

    # Using str.format()
    print("My name is {} and I am {} years old.".format(name, age))

    # Padding and aligning strings
    print(f"|{name:<10}|{name:>10}|{name:^10}|")


# 4. String Splitting and Joining
def string_split_join():
    my_string = "apple,banana,cherry"

    # Splitting
    fruits = my_string.split(",")
    print("Split:", fruits)

    # Joining
    joined_string = "-".join(fruits)
    print("Joined:", joined_string)


# 5. String Validation
def string_validation():
    my_string = "Python123"

    # Checking if the string is alphanumeric
    print("Is alphanumeric:", my_string.isalnum())

    # Checking if the string is alphabetic
    print("Is alphabetic:", my_string.isalpha())

    # Checking if the string is a digit
    print("Is digit:", my_string.isdigit())

    # Checking if the string is lowercase or uppercase
    print("Is lowercase:", my_string.islower())
    print("Is uppercase:", my_string.isupper())


if __name__ == "__main__":
    basic_operations()
    string_methods()
    string_formatting()
    string_split_join()
    string_validation()