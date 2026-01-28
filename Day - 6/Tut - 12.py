# string_methods.py
# This file demonstrates common Python string methods

text = "  Hello World  "

print("Original string:")
print(repr(text))
print("-" * 40)

print("1. upper()        :", text.upper())
print("2. lower()        :", text.lower())
print("3. title()        :", text.title())
print("4. capitalize()   :", text.capitalize())
print("5. swapcase()     :", text.swapcase())

print("-" * 40)

print("6. strip()        :", text.strip())
print("7. lstrip()       :", text.lstrip())
print("8. rstrip()       :", text.rstrip())

print("-" * 40)

print("9. replace()      :", text.replace("World", "Python"))
print("10. split()       :", text.split())
print("11. join()        :", "-".join(["Hello", "World"]))

print("-" * 40)

print("12. find()        :", text.find("World"))
print("13. index()       :", text.index("World"))
print("14. count()       :", text.count("l"))

print("-" * 40)

print("15. startswith()  :", text.startswith("  He"))
print("16. endswith()    :", text.endswith("  "))

print("-" * 40)

print("17. isupper()     :", text.isupper())
print("18. islower()     :", text.islower())
print("19. isalpha()     :", "Hello".isalpha())
print("20. isdigit()     :", "123".isdigit())
print("21. isalnum()     :", "Hello123".isalnum())
print("22. isspace()     :", "   ".isspace())

print("-" * 40)

print("23. center()      :", "Hello".center(20, "-"))
print("24. ljust()       :", "Hello".ljust(10, "."))
print("25. rjust()       :", "Hello".rjust(10, "."))

print("-" * 40)

print("26. format()      :", "My name is {}".format("Python"))
print("27. zfill()       :", "42".zfill(5))

print("-" * 40)