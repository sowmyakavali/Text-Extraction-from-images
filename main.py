import re
import cv2
import os, io
import argparse
import datefinder
import pandas as pd
from datetime import datetime 
from google.cloud import vision
from pre_processing import pre_process
from date import get_fields , get_pattern
from google.oauth2 import service_account


credentials = service_account.Credentials. from_service_account_file('silver-catwalk-276005-f9b869bc2c8e.json')
client = vision.ImageAnnotatorClient(credentials=credentials)

parser = argparse.ArgumentParser()
parser.add_argument('input', type=str, help='images path')
args = parser.parse_args()

def get_details():
    path = args.input
    all_values = []
    for i in os.listdir(path):
        single_img = []
        if i.endswith(".jpg"):
           #filename = i
           image_path = f'{os.path.join(path,i)}'
           image = pre_process(image_path)
           with io.open(image_path, 'rb') as image_file:
                content = image_file.read()           
           image = vision.types.Image(content=content)  # construct an iamge instance
           # annotates Image Response
           response = client.text_detection(image=image)  # returns TextAnnotation
           texts = response.text_annotations
           all_={}
           nums=[]
           dates = []
           pattern = get_pattern()
           for text in texts:
               if (re.match("^[A-Z]{2}[0-9]{1,2}[A-Z0-9]{1,3}[0-9]{3,4}$" , re.sub('\W+','', text.description ))):
                   all_['Reg No'] = text.description
               if (re.match("^[^\\Wioq]{11,18}$" , text.description) and re.search("[0-9]{5,6}$", text.description)):
                   nums.append(text.description )
               if (get_fields(pattern.fullmatch(text.description))):
                   dates.append(get_fields(pattern.fullmatch(text.description))) 
               if (re.match('^[0-9]{1,2}[-|\/]{1}[0-9]{1,2}[-|\/]{1}[0-9]{4}$' ,text.description)): 
                   dates.append(text.description)
           if len(nums)==1:
              all_['VIN No/Chassis No'] = nums[0]
           elif len(nums)>1 and len(nums)<3:
              all_['VIN No/Chassis No']=sorted(nums,key=len)[-1]
              all_['Engine No']=sorted(nums,key=len)[-2]
           if len(dates)>=1:
              for i in dates:
                  if(len(i)==2):
                     i['day']='01'
              D=[]
              for j in dates:
                 try:
                   if (len(j)==3):
                      D.append(j['year']+'-'+j['month']+'-'+j['day'])
                      D.sort()
                      #print(j)
                 except KeyError:
                      D=D
              #for k in D:
                  #all_.append(k) 
              if len(D)>1:
                 all_['MFG DT'] = D[0]
                 all_['REG DT'] = D[1]

           else:
              all_['MFG DT']=dates[0]
           #print(all_)
           all_values.append(all_)
    with open('detailsss.txt','w+') as f:
         f.write(str(all_values))      
    return all_values

get_details()

