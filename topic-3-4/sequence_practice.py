scores = [72, 85,91, 68, 88]
title = "weekly score report"

scores[1] = 86

#I changed the 85 to 86 by changing the variables value

print(scores[0])
print(scores[1])
print(scores[4])

scores.append(93)


weekly = title[0:6]
report = title[13:]

print(weekly)
print(report)

#I think it will print report and list out the scores for the weekly report

label = title[0:6] + " : " + str(scores[0])
print(label)
print("report:", label, scores)
