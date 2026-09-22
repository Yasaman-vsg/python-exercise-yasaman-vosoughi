# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:06:13 2026

@author: 10
"""



logs = [
    ("Ali", "LOGIN", 200),
    ("Ali", "DOWNLOAD", 200),
    ("Sara", "LOGIN", 403),
    ("Reza", "LOGIN", 200),
    ("Sara", "LOGIN", 403),
    ("Sara", "LOGIN", 403),
]
def analyze_logs(logs):
    log_count=0
    users={}
    mashkok=[]
    for log in logs:
        name=log[0]
        action=log[1]
        status=log[2]
       
        if name not in users:
            users[name]={'success':0,
                         'failed':0,
                         'operation':0}
        users[name]['operation']+=1    
        if action=='LOGIN' and status==200:
            users[name]['success']+=1      
          
        elif action=='LOGIN' and status==403:
            users[name]['failed']+=1
            
        if users[name]['failed']>=3:
            mashkok.append(name)
    return users,mashkok
users,mashkok=analyze_logs(logs) 
for name in users:
    print(name,':',users[name])        
print('suspicious users:',mashkok)  

     