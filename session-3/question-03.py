# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 09:52:34 2026

@author: 10
"""
total2=0
total1=0
for i in range(1,11):
    if i%2!=0:
     x=i*5
     total2=total2+x 
     print(x,'= 5*',i)
    if i%2==0:
        r=i+5
        total1=total1+r
        print(r,'= 5+',i)
total=total1+total2        
print('total:',total)        