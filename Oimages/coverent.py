#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image
import os
path = 'C:\\Users\\Small\\Desktop\\myyolov4\\Oimages'
namelist1=os.listdir(path+"\\Pending")
namelist2=[]
angle = [0,30,60,90,120,150,180,210,240,270,300,330]
for i in namelist1:
    if not os.listdir(path+"\\Pending\\"+i):  #判斷資料夾是否為空
          continue
    if not os.path.isdir(path+"\\New sample\\"+i):
            os.makedirs(path+"\\New sample\\"+i)  
    count =len(os.listdir(path+"\\New sample\\"+i))       #統計目前所有以處理相片
    namelist2=os.listdir(path+"\\Pending\\"+i)
    for j in namelist2:
        
        for ang in angle:
            count+=1
            img = Image.open(path+"\\Pending\\"+i+"\\"+j)
            new_img = img.rotate(ang) 
            new_img.save(path+"\\New sample\\"+i+"\\"+i+"{:0>5d}".format(count)+".jpg")
   


'''
for i in range(1,6):
    img = Image.open("chenting"+str(i)+".jpg")
    img2 = Image.open("shiru"+str(i)+".jpg")
    new_img = img.rotate(135) 
    new_img2 = img2.rotate(135) 
    new_img.save("chenting"+str(i+15)+".jpg")
    new_img2.save("shiru"+str(i+15)+".jpg")
    
    new_img = img.rotate(180) 
    new_img2 = img2.rotate(180) 
    new_img.save("chenting"+str(i+20)+".jpg")
    new_img2.save("shiru"+str(i+20)+".jpg")
    
    new_img = img.rotate(225) 
    new_img2 = img2.rotate(225) 
    new_img.save("chenting"+str(i+25)+".jpg")
    new_img2.save("shiru"+str(i+25)+".jpg")
    
    new_img = img.rotate(270) 
    new_img2 = img2.rotate(270) 
    new_img.save("chenting"+str(i+30)+".jpg")
    new_img2.save("shiru"+str(i+30)+".jpg")
    
    new_img = img.rotate(315) 
    new_img2 = img2.rotate(315) 
    new_img.save("chenting"+str(i+35)+".jpg")
    new_img2.save("shiru"+str(i+35)+".jpg")
    print(i)
'''