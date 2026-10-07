n = 1000000
lower = 0
upper = 1001

while upper - lower > 1:
    middle = (lower + upper) // 2

    if middle * middle <= n:
        lower = middle
    else:
        upper = middle

print(lower)

 # TESTS:
# 0 -> 0
# 1 -> 1
# 15 --> 3
# 16 ---> 4
# 17 -> 4
# 1000000 -> 1000