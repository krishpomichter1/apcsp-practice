a = 17
b = 13
temp = 0
count = 0

while b != 0:
    temp = a % b
    a = b
    b = temp
    count = count + 1

print(a)
print(count)

# TESTS:

# 48, 18 -> GCD 6, 3 repetitions
# 270, 192 -> GCD 6, 4 repetitions
# 17, 13 -> GCD 1, 3 repetitions
# 7, 0 -> GCD 7, 0 repetitions