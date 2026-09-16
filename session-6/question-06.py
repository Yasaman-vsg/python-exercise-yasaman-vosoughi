# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 05:45:59 2026

@author: 10
"""
max_customer=''
max_purchase=0
max_price=0
result={}
product_count={}
revenu=0
sales = (
('Ali', 'Laptop', 1200),
('sara', 'Phone', 800),
('Ali', 'Phone', 800),
('Reza', 'Laptop', 1200),
('Sara', 'Laptop', 1200),
('Ali', 'Mouse', 50)
)
for i in sales:
    customer,product,price=i
    if customer not in result:
        result[customer]=0
    result[customer]+=price
    
for customer,total in result.items():
    if total>max_purchase:
        max_purchase=total
        max_customer=customer

for i in sales:
    customer,product,price=i
    if product not in product_count:
        product_count[product]=1
      
    else :
        product_count[product]+=1
        
for i in sales:
    customer,product,price=i
    revenu+=price

print(max_customer,':max_customer')
print(max_purchase,'max_purchase')
print(product_count)
print(result)
print('revenue:',revenu)






      