############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    COVID-19 AI Classification
# Project:       COVID-19 Pneumonia Detection/Early Detection
#
# Author:        Aniruddh Sharma
# Title:         Renaming Image and Filetype Conversion
# Description:   Indexes Images and Converts all of them to PNG Format
# License:       MIT License
# Last Modified: 2020-06-09
#
############################################################################################


import os 
  
os.chdir(' ') #paste location of your ct-scan images folder 
print(os.getcwd()) 
COUNT = 0
  
# Function to increment count  
# to make the files sorted. 
def increment(): 
    global COUNT 
    COUNT = COUNT + 1
  
  
for f in os.listdir(): 
    f_name, f_ext = os.path.splitext(f) 
    f_name = str(COUNT) 
    increment() 
  
    new_name = '{}{}'.format(f_name, ".png") #makes all images in .png extension if there/any
    os.rename(f, new_name)