# -----------------------------------
# Variables and Data Types in Python
# -----------------------------------

# Variables are containers that store values.

a = 5                  # Integer
b = "Hello World"      # String
c = 4.33               # Float
d = True               # Boolean
e = None               # NoneType

# -----------------------------------
# Data Types in Python
# -----------------------------------

# 1. Numeric / Text Data Types: int, float, str

name = "John"          # String data type
age = 24               # Integer data type
salary = 500.00        # Float data type

# 2. Boolean Data Type: True or False

school = False
college = True

# 3. Sequence Data Types: List, Tuple

# List:
# An ordered collection of items.
# Lists are mutable (can be modified).

fruits = ["Apple", "Orange", "Pineapple"]  
fruits_price = ["Apple", 100, "Orange", 85, "Pineapple", 90]
fruits_basket = [
    ["Apple", 100],
    ["Orange", 85],
    ["Pineapple", 90]
]

print(fruits)
print(fruits_price)
print(fruits_basket)


# Tuple:
# An ordered collection of items.
# Tuples are immutable (cannot be modified).

tuple1 = (("Parrot", "Sparrow"), ("Tiger", "Lion"))
print(tuple1)

# 4. Mapped Data Type: Dictionary

# Dictionary:
# An unordered collection of key-value pairs.

dict1 = {
    "name": "John",
    "surname": "Moon",
    "age": 24
}

print(dict1)