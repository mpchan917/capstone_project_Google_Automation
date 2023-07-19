#!/usr/bin/env python3

import requests
import os
import os.path

url = "http://localhost/upload/"
files = []
source_dir = os.path.join(os.getcwd()+"/supplier-data/images/")

def get_jpeg(source_dir):
    f=[]
    for file in os.listdir(source_dir):
        if file.endswith("jpeg"):
            f.append(os.path.join(source_dir+file))
    return f

files = get_jpeg(source_dir)
print (files)
for file in files:
    with open(file, 'rb') as images:
        r = requests.post(url, files={'file': images})

