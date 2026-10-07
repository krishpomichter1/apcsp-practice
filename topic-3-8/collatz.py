value = 999999
steps = e 
peak = value
while value !=  1:
    if value % 2 == 0:
        value = value // 2
        steps = steps + 1
        if value > peak:
            peak = value
    else:
        value = 3*value + 1
        steps = steps + 1
        if value > peak:
            peak = value
print(value)
print(steps)
print(peak)
if (steps > 1000) or (peak > 1000000):
    print("LIMIT REACHED")
else:
    print("REACHED 1")