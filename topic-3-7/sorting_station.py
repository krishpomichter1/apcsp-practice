label = input()
shape = label[0:4]
color = label[4:7]
size = int(label[7:10])
mass = int(label[10:14])
condition = label[14]

#Two equal signs
destination = "unknown"

if condition == "D" or size > 50 or mass > 2000:
    destination = "INSPECT"

print(destination)
print("shape: " + shape)
print("size: " + str(size))
print("mass: " + str(mass))


#Use " " for ball if its a string