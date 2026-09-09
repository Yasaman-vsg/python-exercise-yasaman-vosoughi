# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 15:00:02 2026

@author: 10
"""

s1=input('enter sentences1:')
s2=input('enter sentences2:')
l1=s1.split()
l2=s2.split()
l3=[]
for word in l1:
    if word in l2:
        l3.append(word)
print('common word:',l3)        