# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 09:56:44 2026

@author: 10
"""

p=float(input("enter purchase amount:"))
if p>=1000000:
    p=p*0.85
    print(p)
elif  500000<p<1000000:
    p=p*0.9
    print(p)
else : print(p)    