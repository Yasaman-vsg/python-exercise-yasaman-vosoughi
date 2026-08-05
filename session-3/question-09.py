# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:35:00 2026

@author: 10
"""
count=int(input('haw many numbers should the list contain?'))
list1=[0]*count
list2=[0]*count
p=0
n=0
for i in range(0,count):
  num=int(input('enter number:'))
  if num>0:
      list1[p]=num
      p+=1
  elif num<0 :
       list2[n]=num
       n+=1
print(list2[:n])
      