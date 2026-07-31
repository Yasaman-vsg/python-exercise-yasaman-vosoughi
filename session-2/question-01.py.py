# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 09:12:52 2026

@author: 10
"""

s=float(input("enter km:"))
if s<=2:
    print("car hire =20000t")
elif s>2:
    k=s-2
    n=k*5000
    p=20000+n
    print(p)