# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 11:38:04 2026

@author: 10
"""

while True:
    ramz=input('ramz ra vared konid:')
    if len(ramz)==8 :
        
       if ramz[0:4].isalpha() and ramz[5:].isdigit():
               print("ramz motabar ast")
               break
       else :
               print("ramz bayad 8 ragham va 4 ragham aval horof bashad")
    else :
        print("ramz bayad 8 ragham va 4 ragham aval horof bashad")
 
  