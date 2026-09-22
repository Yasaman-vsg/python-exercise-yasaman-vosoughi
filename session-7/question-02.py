# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 12:40:45 2026

@author: 10
"""

def process_order(customer:str,*products:str,**option:float):
    prices={'laptop':50000000,'mouse':1000000,'keyboard':400000}
    if 'discount' in option:
        discount=option['discount']
    else:
        discount=0
    if 'tax' in option:
        tax=option['tax']
    else:
        tax=0
    if 'shipping' in option:
        shipping=option['shipping']
    else:
        shipping=0
        
    total=0
    for product in products:
        total+=prices[product]
        
    discount_amount=total*discount/100
    price=total-discount_amount
    tax_amount=total*tax/100
    price=price+tax_amount
    price=price+shipping
    return{'customer':customer,'products':products,'discount':discount,'tax':tax,'shipping':shipping,'final_price':price}

   
result=process_order('ali','laptop','mouse','keyboard',discount=10,tax=9,shipping=200000)


print(result)
    
        
        
        
        
        
        