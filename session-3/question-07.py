# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:01:22 2026

@author: 10
"""

c1=input('enter color 1:')
c2=input('enter color 2:')
c3=input('enter color 3:')
if c1==c2 or c1==c3 or c2==c3:
    print('two color are the same')
elif c1==c2==c3:
    print('three color are the same')
else :
    print('all three colors are different')