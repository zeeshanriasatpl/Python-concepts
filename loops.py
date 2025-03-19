for number in range(3):
    print("Attempt: ", number)

print("in range form 1 to 4, => include 1 disclude 4")
for number in range(1, 4):
    print("Attempt: ", number)


print("range 1 to 10 with step of 2 means 1, 3, 5 etc")
for number in range(1, 10, 2):
    print("Attempt: ", number)

successfull = False
for number in range(3):
    if successfull:
        print("successfull")
        break
    else:
        print("failed")

# nested loops
for x in range(3):
    for y in range(2):
        print(f"({x}, {y})")
