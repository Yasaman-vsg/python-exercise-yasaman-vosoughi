# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 05:35:36 2026

@author: 10
"""

transactions = [
    ("Ali", "deposit", 50000000, 10),
    ("Ali", "withdraw", 2000000, 11),
    ("Ali", "withdraw", 3000000, 12),
    ("Ali", "withdraw", 4000000, 13),
    ("Ali", "withdraw", 5000000, 14),
    ("Ali", "withdraw", 6000000, 15),
    ("Sara", "deposit", 50000000, 20),
    ("Sara", "withdraw", 60000000, 21),
    ("Reza", "deposit", 150000000, 30)
]
def chek_large_transaction(transactions):
    dic1={}
    fraud_transaction=[]
    for i in transactions:
        name=i[0]
        Type=i[1]
        amount=[2]
        time=[3]
        if i[2]>100000000:
          
            fraud_transaction.append(i)
       
    return fraud_transaction  
        
def chek_repeated_withdrawals(transactions):
    withdra_count=0
    froud_transactions=[]
    for i in transactions:
        if i[1]=='withdraw':
            withdra_count+=1
            if withdra_count>3:
                froud_transactions.append(i) 
        else:
            withdra_count=0
    return  froud_transactions
def chek_balance(transactions):
    balance={}
    froud_transactions=[]
    for i in transactions :
        if i[0] not in balance:
            balance[i[0]]=0
        if i[1]=='deposit':
            balance[i[0]]+=i[2]
        elif i[1]=='withdraw':
            if i[2]>balance[i[0]]:
                froud_transactions.append(i)
            else:
                balance[i[0]]-=i[2]
    return froud_transactions

def generate_fraud_report(large,repeated,balance):
    report=large+repeated+balance
    return report

def detect_fraud(transactions):
    large=chek_large_transaction(transactions)
    repeated=chek_repeated_withdrawals(transactions)
    balance=chek_balance(transactions)
    return generate_fraud_report(large, repeated, balance)
print(detect_fraud(transactions))
          
                
        