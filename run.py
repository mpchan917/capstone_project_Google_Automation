#!/usr/bin/env python3

import os
import requests
import os.path

txt_dir = os.path.join(os.getcwd()+ "/supplier-data/descriptions/")
photos_dir = os.path.join(os.getcwd()+ "/supplier-data/images/")
items = []
url = "http://[linux-instance-external-IP]/fruits"

def get_items(txt_dir):
    '''Get items list that need to upload to website'''
    for file in os.listdir(txt_dir):
        file_dict = {}
        filename = os.path.splitext(file)
        if filename[1] == ".txt":
            #process txt file
            with open (txt_dir+file, "rb") as f:
                file_dict["name"] = f.readline()
                file_dict["weight"] = int(f.readline().strip(' lbs'))
                file_dict["description"] = f.readlines()
                file_dict["image_name"] = filename[0]+'.jpeg'
            f.close()
            items.append(file_dict)
    return items

def upload(items):
     for file in items:
         response = requests.post(url, data=file)

items = get_items(txt_dir)
upload(items)


