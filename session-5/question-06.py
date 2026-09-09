# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 12:45:28 2026

@author: 10
"""

l=['hack','fraud','scam','password','attack']
s=input('enter sentence:')
l1=s.split()
for i in l:
    if i in l1:
        
        print(i,'-->',l1.count(i))        
        
        
        