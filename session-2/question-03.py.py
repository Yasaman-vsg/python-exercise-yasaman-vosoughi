# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:26:06 2026

@author: 10
"""

i=str(input("enter id card:"))
n=i[0:4]
print(n)
if n=="6037":
    print("bank mellat")
elif n=="6038":
    print("bank melli")
elif n=="5892":
    print("bank sepah")
else     :
    print("unknown bank")