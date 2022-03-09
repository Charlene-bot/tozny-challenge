#Authored by Charlene Crystal Namuyige 
#Code Assessment challenge Tozny 

import json
import re 


#driver code 
def main():

    database = inputFile()
    menu(database)

def menu(database):

    print("====== Welcome to Inventory Management System ====")

    while(1):
        print("1) What are the 5 most expensive items from each category?")
        print("2) Which cds have a total running time longer than 60 minutes?")
        print("3) Which authors have also released cds?")
        print("4) Which items have a title, track, or chapter that contains a year?")
        print("Enter your choice:- ")

        n = int(input())

        if n ==1:
            top5 = mostExpensive(database)
            print(top5)
        elif n == 2:
            greaterthan60 = totalRunningTime(database)
            print(greaterthan60)
        elif n == 3:
            doubleAuthor = authorWithCd(database)
            print(doubleAuthor)
        elif n == 4:
            itemContainsYear = itemWithYear(database)
            print(itemContainsYear)
        else: 
            break

def inputFile():

    with open(('inventory-manager\database.json'), 'r') as f:
        json_array = json.load(f)
    return json_array


#finds 5 most expensive by sorting and slicing the array 
def mostExpensive(database):
    book_list = []
    cd_list = []
    dvd_list = []
    top5 = []

    for item in database:
        if item["type"] == "book":
            book_list.append(item)
        elif item["type"] == "cd":
            cd_list.append(item)
        elif item["type"] == "dvd":
            dvd_list.append(item)

    book_list.sort(key = lambda x:x["price"], reverse=True)
    cd_list.sort(key = lambda x:x["price"], reverse=True)
    dvd_list.sort(key =lambda x:x["price"], reverse=True)

    top5.append(book_list[:5])
    top5.append(cd_list[:5])
    top5.append(dvd_list[:5])

    return top5

def totalRunningTime(database):
    greaterthan60 = []
    sum = 0
    maxTime = 3600
    for item in database:
        if item["type"] == "cd":
            for track in item["tracks"]:
                sum = sum + track["seconds"]
            if sum > maxTime:
                greaterthan60.append(item)
    
    return greaterthan60

def authorWithCd(database):

    authors_Withcd = []
    author_list = []

    for item in database:
        if item["type"] == "book":
            author_list.append(item["author"])

    for item in database:
        if item["type"] == "cd":
            if item["author"] in author_list:
                authors_Withcd.append(item["author"])
    return authors_Withcd

def itemWithYear(database):

    #regex expression for valid date 1900-2099
    year = r"\b(19|20)\d\d"

    matched = []
    for item in database:
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
            for chapter in item["chapters"]:
                if re.search(year, chapter):
                    matched.append(item)

    return matched 

if __name__ == "__main__":
    main()