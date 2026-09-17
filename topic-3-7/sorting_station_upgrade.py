label = input()
shape = label[0:4]  # Ball, cube, cone
color = label[4:7]  # Blue, green, red
size = int(label[7:10])  # length
mass = int(label[10:14])  # Mass (G)
condition = label[14]  # Normal or damaged

# One equal sign because destination is being defined as unknown
destination = "unknown"
eliminate = "FALSE"

if(shape == "CUBE") and (size <= 60) and (mass <= 2500) and (condition =="N"):
    exclude = "TRUE"

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
                destination = "D"
        else: 
            destination = "E"

print(destination)

packaging = "temp"

if destination == "INSPECT":
    packaging = "HOLD"
else:
    if shape == "CONE" or mass > 1000:
        packaging = "CRATE"
    else:
        if shape == "BALL":
            packaging = "PADDED"
        else:
            packaging = "BOX"
print(packaging)
            



# Use " " for ball if its a string


