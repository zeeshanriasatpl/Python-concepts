course = "python programming"
print(len(course))
print(course[3:])
print(course[:3])

# escape sequesnces
# /" => "
# \\ => \
# \n => next line
course = "python \nprogramming"
print(course)


first_name = "Zeeshan"
last_name = "Riasat"
full_name = first_name + " " + last_name  # string concatination

print(full_name)

# formated stirngs
first_name = "Zeeshan"
last_name = "Riasat"
full_name = f"{first_name} {last_name}"

print(full_name)

# String methods

print(course.upper())
print(course.lower())
print(course.title())
# trim any white space form start and end of string we also have lstrip() and rstrip()
print(course.strip())
print(course.find("pro"))  # return index of charctor
print("pro" in course)  # return true false
print("pro" not in course)  # return true false

print(course.replace('p', 'j'))
