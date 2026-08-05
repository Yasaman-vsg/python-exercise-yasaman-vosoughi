# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 07:30:51 2026

@author: 10
"""


x=[15,50,70,1,90,20,4,108,6]
larjest=x[0]
for i in x:
    if i>larjest:
        larjest=i
print(larjest,'بزرگترین:')       


x=[15,50,70,1,90,20,4,108,6]
small=x[0]
for i in x:
    if i<small:
        small=i
print(small,'کوچکترین:')      