# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 12:20:31 2026

@author: 10
"""

s=input('enter your str:')
world=s.split()
longest=world[0]
for i in world:
    if len(i)>len(longest):
        longest=i
print(longest)