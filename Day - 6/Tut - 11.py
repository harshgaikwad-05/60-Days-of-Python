# Strings Slicing and Operations on strings

names = "John, Moon, Albert"
print(len(names))

fruit = "Kiwi"
len1 = (len(fruit))
print("Kiwi is a ",len1,"letter word.")

# Len() function is used for the length of the string.
# We use the (parentheses) for funtions and we use the [Square Brackets] for String Slicing.

slice = "Hello World"
print(len(slice))
print(slice[0:5])  # The [starting point : ending pointing -1 : skip]
print(slice[:5])   # If we dosen't use the string point python will by default use the starting point as 0.
print(slice[6:11]) # Here we are printing the word "World" using the index 6 for the W and ends on d thats 10 so we will write 11.
print(slice[0:-8]) # A Slimple way to learn the -Indexing is to subtract the "-" from the positive indexing. OP - Hel 

# print(slice[0:-8]) = Length of Slice - 10 ((0) and (10 - 8 = 2) that becomes 0:2) Output : Hel

# Quick Quiz:
name = "Albert"
print(name[-4:-2])  # Tell me the Out Put.

# Hint : Get the length of name and subtract the minus value from the length.