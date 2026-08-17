# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 09:34:13 2026

@author: 10
"""
answer=25
while True:
    
    x=int(input("enter your guess:"))
    if  x<answer :
        print("go higher")
    elif 100>x>answer :
        print("go lower")
    elif x>=100:
        print("the number is a two-digit number")
    elif x==25:
        print("thats it! well done")
        break