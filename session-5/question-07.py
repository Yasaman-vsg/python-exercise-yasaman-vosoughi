# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:07:33 2026

@author: 10
"""

s=input('enter world:')
result=''
c=1
for i in range(len(s)):
    if i+1<len(s) and s[i]==s[i+1]:
        c+=1
    else:
        result+=s[i]+str(c)
        c=1
print(result)        