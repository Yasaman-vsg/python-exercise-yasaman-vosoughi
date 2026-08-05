# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:12:50 2026

@author: 10
"""
while True:
    b=int(input('enter balance:'))
    w=int(input('enter the withdrawal amount:'))

    if b>0 and w<=b and w>0:
        b=b-w
        print('new balance:',b)
        break
    elif b>0 and w>b:
          print('insufficient balance')  
    elif w<=0:
          print('error')      
