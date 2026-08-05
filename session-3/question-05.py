# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 12:45:41 2026

@author: 10
"""
while True:
    a=float(input("enter number1:"))
    c=input('(+,-,*,/,):')
    b=float(input("enter number2:"))
    if c=='+':
        answer=a+b
        print('answer:',answer)
    elif c=='-':
        answer=a-b
        print('answer:',answer)
    elif c=='*':
        answer=a*b
        print('answer:',answer)    
    elif c=='/': 
        answer=a/b
        print('answer:',answer)

    x=input('ادامه میدهید؟')
    if x=='خیر':
        break
    