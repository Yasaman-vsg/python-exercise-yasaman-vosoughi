# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 03:12:32 2026

@author: 10
"""

logs_txt='C://Users//10//Documents//python-exercise-yasaman-vosoughi//session-8//logs.txt.txt'

def count_succesful_login():
    count_login=0
    with open(logs_txt,'r')as file:
        for line in file:
            data=line.strip().split(',')
            if data[1]=='LOGIN' and data[2]=='200':
                count_login +=1
    return count_login
    
def count_failed_login():
    count_failed=0
    with open(logs_txt,'r')as file:
        for line in file:
            data=line.strip().split(',')
            if data[1]=='LOGIN' and data[2]!='200':
                count_failed+=1
    return count_failed
    
def find_suspicious_users():
    users={}    
    with open(logs_txt,'r')as file:
        for line in file:
            data=line.strip().split(',')
            username=data[0]
            if data[2]=='403':
                if username not in users:
                    users[username]=1
                
                else :
                    users[username]+=1
    suspicious=[]           
    for username in users:
         if users[username]>=3:
            suspicious.append(username) 
    return suspicious            
    
def generat_report():
    successful=count_succesful_login()
    failed=count_failed_login()
    suspicious=find_suspicious_users()
    operations={}
    with open(logs_txt,'r')as file:
        for line in file:
            data=line.strip().split(',')
            if data[0] not in operations:
                operations[data[0]]=1
            else :
                operations[data[0]]+=1
                
           
        print('login_successful:',successful)  
        print('failed_login:',failed)
        print('suspicious:',suspicious)
        print('operations:',operations)
            
            
generat_report()            
        
        
        
        
    
    
    
    
    
    
    
    