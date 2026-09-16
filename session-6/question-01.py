# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 01:00:51 2026

@author: 10
"""

products = {'laptop': 1200,'phone': 800,'tablet': 500,'headphone': 150,'mouse': 50}
exp=0
cheap=100000
for i in products.values():
    if i>exp :
        exp=i
    elif i<cheap:
        cheap=i
c=0
for i in products.values():
    c=c+i        
    avr=c/5
for i in products:
    if products[i]>500:
        print('extra 500:',i)
        
print('expensive:',exp,'\n'
      'cheap:',cheap,'\n'
      'avrage:',avr)
        