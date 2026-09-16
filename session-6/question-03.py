# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 03:59:19 2026

@author: 10
"""
my_list=[]
my_dic={}
my_str=input('enter str:')
for i in my_str:
    my_list.append(i)
#print(my_list)
for i in my_list:
    if i not in my_dic:
        my_dic[i]=1
    else:
        my_dic[i]+=1
  
       
print(my_dic)        