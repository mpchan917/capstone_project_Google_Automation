#!/usr/bin/env python3

import os
import requests
import os.path

txt_dir = os.path.join(os.getcwd()+ "/supplier-data/descriptions/")
photos_dir = os.path.join(os.getcwd()+ "/supplier-data/images/")
items = []
url = "http://34.135.167.13/fruits/"

def get_items(txt_dir):
    '''Get items list that need to upload to website'''
    for file in os.listdir(txt_dir):
        file_dict = {}
        filename = os.path.splitext(file)
        if filename[1] == ".txt":
            #process txt file
            with open (txt_dir+file, "r") as f:
                file_dict["name"] = f.readline().strip()
                file_dict["weight"] = int(f.readline().strip(' lbs\n'))
                file_dict["description"] = f.readline().strip()
                file_dict["image_name"] = filename[0]+'.jpeg'
            f.close()
            items.append(file_dict)
    return items

def upload(items,url):
     for file in items:
         response = requests.post(url, data=file)

items = get_items(txt_dir)
upload (items,url)



