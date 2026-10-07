value = 1999
passes = 0

while value >= 10:
    total = 0

    while value > 0:
        total = total + value % 10
        value = value // 10

    value = total
    passes = passes + 1

print(value)
print(passes)

#Advanced test:
# 1999 ----> 28 -> 10 -> 1 
#1999 is actually smaller thatn 9875 and needs 3 passes

#Explanation: each digit has a place value, so adding just the digits makes the number smaller. 