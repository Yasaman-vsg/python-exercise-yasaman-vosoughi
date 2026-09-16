# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 05:08:37 2026

@author: 10
"""

student={'ali':[18,17,20],'sara':[15,19,18],'reza':[12,14,10],'mina':[20,20,19]}
for i,num in student.items():
     avr=sum(num)/len(num)
     if avr>=15:
         status='passed'
     else   :
         status='failed'
     highest=max(num)
     print(i,avr,status)     
print('highest:',highest)     