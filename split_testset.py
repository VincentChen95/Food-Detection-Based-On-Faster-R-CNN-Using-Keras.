#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 15:00:14 2018

@author: chenanyi
"""
import numpy as np
import os
import pandas as pd
import cv2

imgs_dir = '/Users/chenanyi/SEALproject/project/keras-frcnn/dataset/'
#print(os.path.isdir(imgs_dir))
label_file = '/Users/chenanyi/SEALproject/project/keras-frcnn/dataset/dataset_labels.csv'
#print(os.path.isfile(label_file))
test_image_dir = '/Users/chenanyi/SEALproject/project/keras-frcnn/test_image/'
#print(os.path.isdir(test_image_dir))

def load_image(imgs_dir,label_file,test_image_dir):	
    test_class_name = []
    imgs_name = []
    test_class_count = {}
    count = 0
    with open(label_file,'r') as f:
        print('Parsing annotation CSV files')
        for line in f:
            if np.random.randint(0,8) == 0:
                count+=1
                line_split = line.strip().split(',')
                (filename,image_width,image_height,class_name,x1,y1,x2,y2) = line_split   
                if class_name not in test_class_count:
                    test_class_count[class_name] = 1
                else:
                    test_class_count[class_name] += 1
                    
                filepath = os.path.join(imgs_dir,filename)
                img = cv2.imread(filepath)
                savepath = os.path.join(test_image_dir,filename)
                cv2.imwrite(savepath, img)
                
                imgs_name.append(filename)
                test_class_name.append(class_name)
                
    dataframe = pd.DataFrame({'file_name':imgs_name,'class_name':test_class_name})
    dataframe.to_csv("testset.csv",index=False,sep=',')
    print(test_class_count)
    print("The total number of test set:",count)
    print("Split done")            
             
load_image(imgs_dir,label_file,test_image_dir)