# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 08:43:47 2026

@author: 10
"""
my_dic={}
orders = [
('Ali', 'Laptop'),
('Sara', 'Phone'),
('Ali', 'Phone'),
('Reza', 'Laptop'),
('Sara', 'Laptop'),
('Ali', 'Tablet'),
('Reza', 'Phone')
] 
for person,product in orders:
    if person not in my_dic:
        my_dic[person]=product
    else:
        my_dic[person]+=', '+product
for person,product in my_dic.items():
    print(person,':',product)