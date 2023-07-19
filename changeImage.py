#!/usr/bin/env python3

from PIL import Image
import os
import os.path

def get_files(source_dir):
    '''list all images that need to alter'''
    for file in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir+file)):
            files_list.append(file)
    return files_list

def alter_images(source_dir, files_list):
    '''alter images to thumbnail'''
    for file in files_list:
        filename = os.path.splitext(file)
        #get the base name and file type for further processes
        if filename[1]== '.tiff':
            im = Image.open(source_dir+file)
            if im.mode != "RGB":
                im = im.convert("RGB")
            im.resize((600,400)).save(source_dir+filename[0]+".jpeg","Jpeg")


files_list = []
source_dir = os.getcwd()+"/supplier-data/images/"
files_list = get_files(source_dir)
alter_images(source_dir,files_list)








