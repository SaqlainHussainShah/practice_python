#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 00:46:38 2019

@author: saqlain
"""
import numpy as np


##CReating an array of zeros and defining column types
##i4 32 bit integer,f4 32 bit float,a10 string with 10 char
#recarr = np.zeros((2,), dtype=('i4,f4,a10'))
#toadd = [(1,2.,'Hello'),(2,3.,"World")]
#recarr[:] = toadd
#
##zip will create list of tuples 
##creating array with zeros and defining types
#recarr=np.zeros((2,),dtype=('i4,f4,a10'))
#
##creating cols to add
#col1=np.arange(2)+1
#col2=np.arange(2, dtype=np.float32)
#col3=["Hello", ' World']
#
##create list of tuples identical to previous toadd list
#toadd=zip(col1,col2,col3)
#
##Assigning values to recarr
#recarr[:]=toadd
#recarr.dtype.names=("Integers","Floats",'Strings')
#recarr['Integers']



############################# Indexing and slicing
alist=[[1,2],[5,3]]
#print(alist)
#print("alist[0][1]   ", alist[0][1]) #print 2
## print(alist[0,1]) is error cannot acces list element using [0,1]
#
##convert this list to array
#arr=np.array(alist)
#print("arr[0][1]     ", arr[0][1]) #print 2
#print("arr[0,1]      ", arr[0,1]) #print 2 in array
#print("arr[:,1]      ", arr[:,1])
#print("arr[:][1]     ",arr[:][1])
#print("arr[1,:]      ",arr[1,:])
#print("alist[1][:]   ",alist[1][:])

## indexing based on conditions ##
arr=np.arange(5)
index=np.where(arr>2)
print("index",index)
new_arr=arr[index]
print("np.where(arr>2) : ", new_arr)
del_arr=np.delete(arr,index)
print("np.delete(arr,index)", del_arr)

## boolean function instead of where
## BOOLEAN IS FASTER
## ~ can be used to invert 
index=arr>2
index=~index  #instead of index<2 can invert using ~ #faster
print(index)
new_arr=arr[index]
print("arr[index], index=arr<2 and ~ : ", new_arr)
