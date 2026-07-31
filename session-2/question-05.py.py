# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:41:58 2026

@author: 10
"""
h=int(input("enter hour:"))

if 12<=h<=15:
    print("noon")
elif 16<=h<=19:
      print("afternoon")
elif  20<=h<=23:
      print("night")
elif  0<=h<=4:
     print("midnight")
elif   5<=h<=11:
       print("morning")
else  : 
      print("error")       
    