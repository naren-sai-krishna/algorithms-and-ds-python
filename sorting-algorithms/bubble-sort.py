# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 18:02:36 2018

@author: naren
"""


# Implementation of Bubble Sort in python


#-----------------------------------------------
def bubble(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            #print(i," ",j," ",arr)
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
                
#------------------------------------------------
    
#Input:
arr=[5,2,17,21,9,1]
bubble(arr)
                
                
                
