# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 17:45:55 2018

@author: naren
"""

# Implementation of Linear Search in Python

#-----------------------------
def lin_search(arr , key):
    for i in range(0 , len(arr)):
        if arr[i]==key:
            return i
    return -1


#-----------------------------
    
#Input:
    
lin_search([20,30,40,50,60],70)