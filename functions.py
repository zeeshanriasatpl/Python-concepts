def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome aboard")


greet("Zeeshan", "Riasat")
greet("Mosh", "Hamdani")


# Types of functions
#   1. perform a task
#   2. return a value

def performfun(name):
    print(f"Hi {name}")


def returnfun(name):
    return f"Hi {name}"


performfun("Zeeshan")
message = returnfun("Mosh")
print(message)


# Keyword arguments

def keywordArguments(number, by):
    return number + by


print(keywordArguments(3, by=2))
