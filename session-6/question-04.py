# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 04:29:47 2026

@author: 10
"""
min_salary=10000000
max_salary=0
employees = {'E01':{'name':'ali','age':28,'salary':3000},'E02':{'name':'sara','age':32,'salary':4500},'E03':{'name':'reza','age':25,'salary':2800}}
for i, data in employees.items():
    if data['salary']>max_salary:
        max_salary=data['salary']
        max_employee=data['name']
        
    if data['salary']>3000:
          print('salary>3000:',data['name'])
    if data['salary']<min_salary:
          min_salary=data['salary']
          min_employee=data['name']   
          
print(max_salary,':max_salary',max_employee) 
print(min_salary,':min_salary',min_employee)         