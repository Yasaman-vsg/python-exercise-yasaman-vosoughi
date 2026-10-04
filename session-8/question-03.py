# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 23:09:15 2026

@author: 10
"""
transactions_txt='C://Users//10//Documents//python-exercise-yasaman-vosoughi//session-8//transactions_txt.txt'

def calculate_balance():
    balanc_dic={}
    with open(transactions_txt,'r')as file:
        for info in file:
            person=info.strip().split(',')
            if person[1]=='deposit':
                if person[0] in balanc_dic:
                    balanc_dic[person[0]]+=int(person[2])
                    
                else:
                     balanc_dic[person[0]]=int(person[2])
            elif person[1]=='withdraw'        :
                if person[0] in balanc_dic:
                    if balanc_dic[person[0]]>=int(person[2]):
                        balanc_dic[person[0]]-=int(person[2])
                else:
                    balanc_dic[person[0]]=0
                    
    return balanc_dic    
          
def total_deposit():
    
    deposit_dic={}
    with open(transactions_txt,'r')as file:
        for info in file:
            person=info.strip().split(',')
            if person[1]=='deposit':
                if person[0] in deposit_dic:
                    deposit_dic[person[0]]+=int(person[2])
                else:
                    deposit_dic[person[0]]=int(person[2])
                    
    return deposit_dic  


def total_withdraw():
    
    withdraw_dic={}
    with open(transactions_txt,'r')as file:
        for info in file:
            person=info.strip().split(',')
            if person[1]=='withdraw':
                if person[0] in withdraw_dic:
                    withdraw_dic[person[0]]+=int(person[2])
                else:
                    withdraw_dic[person[0]]=int(person[2])
                    
    return withdraw_dic  


def find_invalid_transactions():
    balanc_dic={}
    invalid_dic={}
    with open(transactions_txt,'r')as file:
        for info in file:
            person=info.strip().split(',')
            if person[1]=='deposit':
                if person[0] in balanc_dic:
                    balanc_dic[person[0]]+=int(person[2])
                else:
                    balanc_dic[person[0]]=int(person[2])
                    
            elif person[1]=='withdraw':
                if person[0] in balanc_dic:
                    if balanc_dic[person[0]]>=int(person[2]):
                        balanc_dic[person[0]]-=int(person[2])
                    else:
                        if person[0] in invalid_dic:
                            invalid_dic[person[0]]+=1
                        else:
                            invalid_dic[person[0]]=1
                            
                else:          
                      invalid_dic[person[0]]=1     
                            
    return invalid_dic


def generat_report():
    balanc_dic=calculate_balance()
    deposit_dic=total_deposit()
    withdraw_dic=total_withdraw()
    invalid_dic=find_invalid_transactions()  
    for user,balance in balanc_dic.items():
        deposit=deposit_dic.get(user,0)
        withdraw=withdraw_dic.get(user,0)
        invalid=invalid_dic.get(user,0)
        
        print('name:',user,'>>>','deposit:',deposit,'/','withdraw:',withdraw,'/','invalid:',invalid)
       
        
print('=========transaction report==========')        
generat_report()        
        
        
        







                     
                            
                            




             