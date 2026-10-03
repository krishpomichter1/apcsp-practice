value = 6
steps = 0
peak = value

print(value)

while value != 1 and steps < 1000 and value <= 1000000:
    if value % 2 == 0:
        value = value // 2
    else:
        value = 3 * value + 1
    
    steps = steps + 1
    print(value)

    if value > peak:
        peak = value

if value == 1:

    print("REACHED 1")

else:

    print("LIMIT REACHED")

print("Transformations:", steps)

print("Peak:", peak)

print("Final value:", value)


# TESTS:

# 1, 6, 7, 27, 999999, and 6 with 5 step limit
# ALL WORKED