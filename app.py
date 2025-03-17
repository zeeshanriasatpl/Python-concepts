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
