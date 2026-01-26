# Type Casting
# The conversion of one data type into the other data type is known ad type casting.

# There are two types of typecasting.
# 1. Explicit Typecasting (Done by programmer or developer)

string = "15"
number = 7
string_number = int(string) # changed the string to integer.
sum = number + string_number
print(sum)

# 2. Impilicit Typecasting (Done by Python)

a = 7     #int
b = 3.0   #float
# Python automatically converts c to float as it is a float addition.
c = a + b
print(c)