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

label = title[0:6] + " : " + str(len(scores))
print(label)
print("report:", label, scores)

print("Last item:", scores[len(scores) - 1])

lax_goals = [3, 5, 2]
lax_title = "lacrosse stats"
lax_goals.append(4)
lax_label = lax_title[0:8] + " : " + str(len(lax_goals))
print(lax_label, lax_goals)
