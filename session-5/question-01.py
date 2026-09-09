# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:18:39 2026

@author: 10
"""

while True:
    pas=True
    password=input('enter your password:')
    if len(password)<8:
        print('password must be more than 8 characters')
        pas=False
        
    if password.isdigit() or password.isalpha():
        print('it mist contain both letters and numbers')
        pas=False
    if password.islower() or password.islower():
        print('it must be contain uppercase and lowercase letters')
        pas=False
        
    
        
    if  not any(char in '#@&.'for char in password):
        print('it must be contain special character')
        pas=False
    if pas==True :
         print('succesfully registered')
         break