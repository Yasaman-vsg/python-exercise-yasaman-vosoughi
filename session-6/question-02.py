# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:12:09 2026

@author: 10
"""

inventory = {'apple':20,'banana':5,'orange':0,'milk':12,'bread':0}
l_av=[]
l_out=[]
dic_av={}
dic_out={}
for i in inventory:
    l:[]
    if inventory[i]!=0:
         l_av.append(i)
         dic_av[i]=inventory[i]
        
    else:
        l_out.append(i)
        dic_out[i]=inventory[i]
print('out of stock')
print(l_out)        
print(dic_out)       
print('availble')
print(l_av)
print(dic_av)
