value = 999999
steps = 0
peak = value

while value != 1 and steps < 1000 and value <= 1000000:
    if value % 2 == 0:
        value = value // 2
    else:
        value = 3 * value + 1

    steps = steps + 1

    if value > peak:
        peak = value

print(value)
print(steps)
print(peak)

if value == 1:
    print("REACHED 1")
else:
    print("LIMIT REACHED")