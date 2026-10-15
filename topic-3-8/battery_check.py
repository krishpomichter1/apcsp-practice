charges = [62, 28, 85, 14, 47 ]
lowest = charges[0]
count = 0

for charge in charges:
    if charge < lowest:
        lowest = charge
    if charge < any80:
        any80 = True
    if charge < 30
    count = count + 1
    


for i in range(0, len(charges), 1):
    if lowest > charges[i]:
        lowest = charges[i]
    if charges[i] >= 80:
        any80 = True
    if charges[i] < 30:
        count = count + 1

print("Lowest charge", lowest)
print(count)
print(any80)



