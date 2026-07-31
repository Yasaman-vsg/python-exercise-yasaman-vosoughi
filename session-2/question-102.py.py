# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 08:30:50 2026

@author: 10
"""

name=str(input('enter full name:'))
firstname=(name[0])
s=name.index(" ")
family=name[s+1:]
print(firstname+"."+family)
