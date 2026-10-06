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

# ADVANCED: 3n - 1 variation

start = 5
value = start
steps = 0

print("Advanced test:")
print(value)

while steps < 1000 and value <= 1000000:
    if value % 2 == 0:
        value = value // 2
    else:
        value = 3 * value - 1

    steps = steps + 1
    print(value)

    if value == start:
        break

if value == start:
    print("CYCLE FOUND")
else:
    print("LIMIT REACHED")

# Test: 5 -> 14 -> 7 -> 20 -> 10 -> 5

# ADVANCED: cycle detector limit

start = 3
value = start
steps = 0

print("Advanced limit test:")
print(value)

while steps < 1000 and value <= 1000000:
    if value % 2 == 0:
        value = value // 2
    else:
        value = 3 * value - 1

    steps = steps + 1
    print(value)

    if value == start:
        break

if value == start:
    print("CYCLE FOUND")
else:
    print("LIMIT REACHED")

# Test: 3 enters the cycle 2 -> 1 -> 2 without returning to 3,
# so the detector reaches its limit.