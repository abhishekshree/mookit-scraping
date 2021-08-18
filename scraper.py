#!/usr/bin/env python3

import re
import sys
import os
from bs4 import BeautifulSoup

def prepare_data():
    """
    Returns a list of all the data as chunk of strings in the format:  
    Week, Title, URL
    """
    f = open('index.html', encoding="utf8")
    html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    f.close()

    li = soup.find_all('ul', class_='weekList')
    info = [x.findChildren("div", class_='lectureInfoBoxText') for x in li]
    
    # LectureNames is a 2D list hence it preserves week information.
    LectureNames = []

    for x in info:
        x = [str(y.text).strip() for y in x]
        LectureNames.append(x)

    urls = []
    for i in li:
        for j in i:
            url = re.findall(r'https:\/\/hello\.iitk\.ac\.in\/.+\/#\/lecture\/.+(?=">)', str(j))
            if url != []:
                urls.append(url)

    # Convert all the urls obtained to a 1D list of strings
    urls_final = [item for sublist in urls for item in sublist]

    all_list = []
    for i in range(len(LectureNames)):
        for j in range(len(LectureNames[i])):
            all_list.append(str("Week " + str(i) + ", " + LectureNames[i][j].replace(',',"") + ", " + urls_final.pop(0) + ","))

    all_list.reverse()
    return all_list


def write_data(n):
    """
    Writes the required number of data elements to the csv file
    """
    res = open("data.csv", "w")
    res.write("Week, Title, URL,\n")

    tmp = []
    allItems = prepare_data()

    if n > len(allItems):
        n = len(allItems)

    for x in range(n):
        tmp.append(allItems.pop(0))
    tmp.reverse()

    for x in tmp:
        res.write(x + "\n")
    res.close()

    print("Done")


if __name__ == "__main__":
    n = int(sys.argv[1])
    write_data(n)