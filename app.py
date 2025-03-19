# Exercise
count = 0
for number in range(1, 10):
    if (number % 2 == 0):
        count = count + 1
        print("number: ", number, " count:", count)
print(f"we have {count} even numbers")
