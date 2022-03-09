import json
import re

#read file 
with open(('inventory-manager\database.json'), 'r') as f:
    json_array = json.load(f)



#print(type(json_array))

book_list = []

for item in json_array:
    if item["type"] == "book":
        book_list.append(item)
      #  print(item)

#print(book_list, end='\n')

#book_list.sort(key= lambda x:x["price"], reverse=True)

#print("SORTED\n")
#print(book_list)
#print(book_list[:5])
#dvd_list = []
#for item in json_array:
  #  if item["type"] == "dvd":
 #     #  print(item)
   #   dvd_list.append(item)

#print(dvd_list)

greaterthan60 = []
sum = 0 
for item in json_array:
    if item["type"] == "cd":
        for track in item["tracks"]:
            sum = sum + track["seconds"]
        if sum > 3600: 
            greaterthan60.append(item)

#print(greaterthan60)


author_list = []
for item in json_array:
    if item["type"] == "book":
        author_list.append(item["author"])

#print(author_list)

artiste_list = []
for item in json_array:
    if item["type"] == "cd":
        if item["author"] in author_list:
            artiste_list.append(item["author"])

#print(artiste_list)


#which item contains a year in either title, track or chapter 
year = r"^(19|20)\d\d"

matched = []
for item in json_array:
    if item["type"] == "dvd":
        if re.search(year, item["title"]):
            matched.append(item)
    if item["type"] == "cd":
        if re.search(year, item["title"]):
            matched.append(item)
        for track in item["tracks"]:
            if re.search(year, track["name"]):
                matched.append(item)
    if item["type"] =="book":
        if re.search(year, item["title"]):
            matched.append(item)



print(matched)