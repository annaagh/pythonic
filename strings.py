# string_operations.py - Practice Python String Operations with a Class

class StringOperations:
    def __init__(self, my_string):
        self.my_string = my_string

    # 1. Basic String Operations
    def basic_operations(self):
        print("Original String:", self.my_string)

        # Length of the string
        print("Length of the string:", len(self.my_string))

        # Accessing characters and slicing
        print("First character:", self.my_string[0])
        print("Last character:", self.my_string[-1])
        print("Slicing (0:5):", self.my_string[0:5])

        # String concatenation
        print("Concatenation:", self.my_string + " Let's learn strings.")

        # String repetition
        print("Repetition:", self.my_string * 3)

    # 2. String Methods
    def string_methods(self):
        print("Stripped string:", self.my_string.strip())

        # Converting to uppercase and lowercase
        print("Uppercase:", self.my_string.upper())
        print("Lowercase:", self.my_string.lower())

        # Checking start and end of the string
        print("Starts with 'Hello':", self.my_string.startswith("Hello"))
        print("Ends with '!':", self.my_string.endswith("!"))

        # Finding and counting substrings
        print("Find 'Python':", self.my_string.find("Python"))
        print("Count 'o':", self.my_string.count("o"))

        # Replace substring
        print("Replace 'Python' with 'World':", self.my_string.replace("Python", "World"))

    # 3. String Formatting
    @staticmethod
    def string_formatting(name, age):
        # Using f-strings (Python 3.6+)
        print(f"My name is {name} and I am {age} years old.")

        # Using str.format()
        print("My name is {} and I am {} years old.".format(name, age))

        # Padding and aligning strings
        print(f"|{name:<10}|{name:>10}|{name:^10}|")

    # 4. String Splitting and Joining
    def string_split_join(self, separator=","):
        # Splitting
        fruits = self.my_string.split(separator)
        print("Split:", fruits)

        # Joining
        joined_string = "-".join(fruits)
        print("Joined:", joined_string)

    # 5. String Validation
    def string_validation(self):
        # Checking if the string is alphanumeric
        print("Is alphanumeric:", self.my_string.isalnum())

        # Checking if the string is alphabetic
        print("Is alphabetic:", self.my_string.isalpha())

        # Checking if the string is a digit
        print("Is digit:", self.my_string.isdigit())

        # Checking if the string is lowercase or uppercase
        print("Is lowercase:", self.my_string.islower())
        print("Is uppercase:", self.my_string.isupper())


# Example usage
if __name__ == "__main__":
    # Create an instance of StringOperations
    my_string = " Hello, Python! "
    string_ops = StringOperations(my_string)

    # Perform basic operations
    string_ops.basic_operations()

    # Perform string methods
    string_ops.string_methods()

    # Perform string formatting (static method)
    StringOperations.string_formatting("Alice", 30)

    # Perform splitting and joining
    string_ops.string_split_join()

    # Perform string validation
    string_ops.string_validation()
