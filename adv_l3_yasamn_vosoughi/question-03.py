# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 09:53:28 2026

@author: 10
"""
list1=[]
while True:
    my_users=input('enter name:')
    list1.append(my_users)
    c=0
    for i in list1:
        if i[0]=='a' or i[0]=='A':
            c=c+1
    if my_users=='stop':
        break
print(c)