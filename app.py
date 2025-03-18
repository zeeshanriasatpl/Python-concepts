x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")


# type conversions
# int(x)
# float(x)
# bool(x)
# str(x)


# Falsy values => "", 0, None
print(bool(""))

# conditional statements
temperature = 35
if temperature > 30:
    print("Its warm")
elif temperature > 30:
    print("its nice")
else:
    print("its cold")
print("Done")

# Ternary operator
age = 22
message = "eligible" if age >= 18 else "not eligible"
print(message)
