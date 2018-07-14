# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 17:50:38 2018

@author: naren
"""

# Implementation of binary search in python

# NOTE --> The list must be SORTED.

#------------------------------------
def bin_search(arr,start,end,key):
    
    if start<=end:
        mid = start+(end-start)//2
        if key==arr[mid]:
            return mid
        elif key>arr[mid]:
            return bin_search(arr,mid+1,end,key)
        else:
            return bin_search(arr,start,mid-1,key)
    else:
        return -1

            
#------------------------------------     
#Input :
        
arr=[133,12,34,45,15,46]
arr.sort()
print("arr=",arr)
bin_search(arr,0,len(arr)-1,12)    
    
    



