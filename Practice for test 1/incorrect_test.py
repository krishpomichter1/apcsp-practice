#Version D

label = input()

temperature = int(label[0:3])
moisture = int(label[3:6])
sunlight = label[6]
tank = int(label[7:10])
sensor = label[10]


# flag = label[11] 
# humidity = int(label[12:14])
# vent = label[14] 
# else: 
#     humidity = int(label[12:15]) 
#         vent = label[15] 
#         action = IDLE



if sensor == "F" or temperature > 40:
    destination = "CHECK"
else:
    if moisture < 40: 
        if tank < 12:
            destination = "REFILL"

    if (sunlight == "B") and (temperature >= 24): 
        destination = "WATER_LONG"

    if moisture < 40:
        destination = "WATER_SHORT"

    if temperature >= 32:
        destination = "VENT"
        
    else:
        destination = "IDLE"

print(destination)





        
            