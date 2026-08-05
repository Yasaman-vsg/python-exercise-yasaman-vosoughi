# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 12:10:17 2026

@author: 10
"""

a=input('enter;')
b=0

for i in(a):
    b+=1
if b%2==0:
   c=b//2
   print(a[:c])
else:
   c=b//2
   print(a[c:])
        