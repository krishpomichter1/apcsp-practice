label = input()
shape = label[0:4]  # Ball, cube, cone
color = label[4:7]  #
size = int(label[7:10])  # legnth
mass = int(label[10:14])  # Mass (G)
condition = label[14]  # Normal or damaged

# One equal sign because destination is being defined as unknown
destination = "unknown"

if condition == "D" or size > 50 or mass > 2000:
    destination = "INSPECT"

else:
    if shape == "BALL":
        if color == "RED" and size > 10:
            destination = "B"

        else:
            destination = "A"
    else:
        if shape == "CUBE":
            if color == ("BLU" or "GRN") and size <= 10:
                destination = "C"
    else: 


print(destination)


# Use " " for ball if its a string
