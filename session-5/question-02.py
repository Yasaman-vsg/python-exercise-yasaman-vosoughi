# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 12:46:35 2026

@author: 10
"""
"""
a=input('enter:')
t=''
for i in a:
   if i not in t:
       t=t+i
       
print(t)        
"""

a=input("enter:")
my_list=[]
for i in a:
    if i not in my_list:
        my_list.append(i)
        my_list_new=''.join(my_list)
print(my_list_new)        