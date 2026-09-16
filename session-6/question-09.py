# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:50:58 2026

@author: 10
"""
list_mojody=[]
list_namojod=[]
max_value=0
max_product=''
price={}
total=0
products = {
'P01': ('Laptop', 1200, 5),
'P02': ('Phone', 800, 0),
'P03': ('Tablet', 500, 12),
'P04': ('Mouse', 50, 25),
'P05': ('Keyboard', 100, 0)
}
for p,t in products.items():
    if t[2]!=0:
        list_mojody.append(t[0])
    else:
        list_namojod.append(t[0])
for p,t in products.items():
    price[p]=t[1]*t[2]
    
for p,value in price.items():
    if value>max_value:
        max_value=value
        max_product=p
for value in price.values():        
    total=total+value
print('list mojody:',list_mojody) 
print('list namjod:',list_namojod)
print('max_product:',max_product) 
print(price)
print('total:',total)  
    
                