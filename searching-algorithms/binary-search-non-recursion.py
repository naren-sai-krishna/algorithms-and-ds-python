# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 19:32:41 2018

@author: naren
"""

# Implementation of binary search in python (NON RECURSION)

# NOTE --> The list must be SORTED.

#------------------------------------
def bin_search(arr,key):
    start=0
    end=len(arr)-1
    
    while start<=end:
            mid = (end+start)//2
            if key==arr[mid]:
                return mid
            elif key>arr[mid]:
                start=mid+1
            else:
                    end=mid-1
    return -1

            
#------------------------------------     
#Input :
        
arr=[133,12,34,45,15,46]
arr.sort()
print("arr=",arr)
bin_search(arr,13)    
    
    



