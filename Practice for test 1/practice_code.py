label = input()

shape = label[0:4]
color = label[4:7]
weight = int(label[7:10])
fragility = int(label[10:13])
flag = label[13]

if flag == "Y":
    destination = INSPECT
