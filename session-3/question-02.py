# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 07:59:02 2026

@author: 10
"""


record=0
for i in range(10):
   r=float(input('enter new record:'))
   
   if record<=r:
       record=r
       print('max record:',record)
   else:    
       print('record tekrari','\n','max record:',record)