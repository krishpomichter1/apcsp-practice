label = input()

type = label[0:4]
color = label[4:7]
size = int(label[7:10])
weight = int(label[10:14])
condition = label[14]

destination = "E"

if condition == "D" or size > 50 or weight > 2500:
    destination = "INSPECT"
else:
    if type == "BOX": 
        if color == "RED" and size > 15:
            destination = "A"
        else:
            destination = "B"

    if type == "BAG":
        if (color == "BLU" or color == "GRN") and size <= 20:
            destination = "C"
        else: 
            destination = "D"

    if type == "BALL":
        if color == "RED" and size > 10:
            destination = "B"
        else:
            destination = "A"

print(destination)