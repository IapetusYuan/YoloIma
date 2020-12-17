# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 15:55:35 2020

@author: Small
"""

import os
import shutil
path = 'C:\\Users\\Small\\Desktop\\myyolov4\\Oimages'
namelist1=os.listdir(path+"\\Pending")
for i in namelist1:
    if not os.listdir(path+"\\Pending\\"+i):  #判斷資料夾是否為空
          continue     
    namelist2=os.listdir(path+"\\Pending\\"+i)
    for j in namelist2:
        if os.path.isdir(path+"\\Original sample\\"+i):
            shutil.move(path+"\\Pending\\"+i+"\\"+j, path+"\\Original sample\\"+i)
        else:
            os.makedirs(path+"\\Original sample\\"+i)
            shutil.move(path+"\\Pending\\"+i+"\\"+j, path+"\\Original sample\\"+i)
            
        
        