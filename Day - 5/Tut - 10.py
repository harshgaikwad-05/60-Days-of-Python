# Strings in python

name = "lovish"
Friend_1 = "Moon"
Friend_2 = "John"

# Strings can be enclosed in single or double quotes and it dosent matter even. The String output remains the same.

apple = "He said \"He wants to eat an apple\"."   # For adding the extra "Quotes or any notation" we must use the Backslash \.  OR
alternative_apple = 'He said "He wants to eat an apple."'  # We can use the single quotes to add the double quotes inside the sentence without using the backslash.

# To print the multiple line 

string = '''We can use 
the triple quotes
to add the spaces wherever 
we want to.'''

# Using the triple quotes we can add up spaces and line breaks without using the \n and escape sequences.

store_it = "ABCDEFG"
print(store_it[0])
print(store_it[1])
print(store_it[2])
print(store_it[3])
print(store_it[4])
print(store_it[5])
print(store_it[6])

# We can access the string by their index - Starting from 0.

for i in store_it:
    print(i)

# We can use the for loop as well for printing the character by character.
# Don't worry about the loops we will study further about the loops.