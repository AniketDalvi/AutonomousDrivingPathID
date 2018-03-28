#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 01:28:45 2018

@author: yashshah
"""
from PIL import Image
import glob

def import_images(checker,start,end):
    
    image_list=[]
    required_list = []
    if(checker):
        for filename in sorted(glob.glob('Images/Training/RGB/*.png')):
            im=Image.open(filename)
            image_list.append(im)
        
       
        for x in range(start, end+1):
            required_list.append(x)
            
    else:
        for filename in sorted(glob.glob('Images/Testing/RGB/*.png')):
            im = Image.open(filename)
            image_list.append(im)
            
        for x in range(start, end+1):
            required_list.append(x)
            
        # for x in required_list:
         #gfv.FeatureVectorGenerator.generate_feature_vector(x, cell_width, cell_length, training, bins)