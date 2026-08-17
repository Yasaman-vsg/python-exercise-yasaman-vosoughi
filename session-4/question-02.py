# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 10:18:59 2026

@author: 10
"""

import random
while True:
    pc=random.choice(['sang','kaghaz','gheychi'])
    user=input("sang/kaghaz/gheychi\nbaraye khoroj az bazi exit benevisid\nentekhab kon:")
    if user=='exit':
        print('bye')
        break
    elif user!='sang' and user!='kaghaz' and user!='gheychi':
        print('vorodi eshtebah ast!!')
    elif user==pc :
        print('mosavi')
    elif   (user=='sang' and pc=='gheychi') or (user=='kaghaz' and pc=='sang')or ( user=='gheychi' and pc=='kaghaz') :
        print('user win')
    elif   (pc=='sang' and user=='gheychi') or (pc=='kaghaz' and user=='sang')or ( pc=='gheychi' and user=='kaghaz') :
        print('pc win')
    print('pc choice:',pc)   
    print('____________________________________')      