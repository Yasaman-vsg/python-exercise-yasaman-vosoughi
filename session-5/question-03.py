# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 13:23:47 2026

@author: 10
"""

a=input('enter :')
digit=0
letters=0
uppercase=0
lowercase=0
spaces=0
special_charactor=0

for i in a:
    if i.isdigit():
        digit+=1
    if i.isupper():
        uppercase+=1
    if i.lower():
        lowercase+=1
    if i.isalpha():
        letters+=1
    if i.isspace():
        spaces+=1
    if not i.isalnum():
        special_charactor+=1
print('digit=',digit,'\n','letters=',letters,'\n','uppercase=',uppercase,'\n','loweercase=',lowercase,'\n','spaces=',spaces,'\n','special_character=',special_charactor)        
        
        
        