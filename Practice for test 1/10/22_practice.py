label = input()

genre = label[0:3]
cover = label[3:5]
page_count = int(label[5:8])
year_published = int(label[8:12])
status = label[12]

# print(genre)
# print(cover)
# print(page_count)
# print(year_published)
# print(status)

if status == "L" or year_published < 1900:
    destination = "DESK"
else:
    if genre == "SCI":
        if cover == "PB" and (year_published >=2000 or page_count < 100):
                destination = "SHELF 3"
        else:
            destination = "SHELF 4"
    else:
         if genre == "FIC":
              if cover == "HB" and page_count > 400:
                   destination = "SHELF 1"
              else:
                   destination = "SHELF 2"
         else:
            destination = "SHELF 5"

print(destination)







