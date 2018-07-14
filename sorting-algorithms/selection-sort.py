# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 18:08:05 2018

@author: naren
"""

# Implementation of Selection Sort in Ascending order

#-------------------------------------------------
def selection(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr

#-------------------------------------------------

# Input:
     
arr=[10,2,78,65,44,79,90,120,103]
selection(arr)                
                
                
                
                