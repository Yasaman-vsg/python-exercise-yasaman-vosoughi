# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:05:07 2026

@author: 10
"""

print("welcome yas shop")
list1=[]
while True:
    x=input("do you want to buy?")
    c=x.lower().strip()
    if c=="yes":
         print("here you are")
         while True:
             l=input('when you are done,type stop\nwhat do you want?')
             list1.append(l)
             if l=='stop':
                 print(list1)
                 p=input('select a payment method:\n1.credit card\n2.paybal\n3.banktransfer\n:')
                 if p=='3':
                     card_num=input('enter your card nember:')
                     if len(card_num)!=16:
                         print('invalid')
                     else :
                         print('payment was successful\nthank you for your purchase')
                          
                 break
                 
         break
    elif c=="no" :
         print("goodbye")    
         break
         
    else :
        print(" answer yes or no")