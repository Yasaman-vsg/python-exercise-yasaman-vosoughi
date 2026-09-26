# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 03:39:43 2026

@author: 10
"""

users_txt='‪C://Users//10//Desktop//users_txt.txt'

def add_user(username,password,status):
    with open(users_txt,'r')as file:
        for line in file:
            data=line.strip().split(',')
            
            if username.lower()==data[0].lower():
                return 'user already exists'
                
    with open(users_txt,'a')as file:   
        file.write(f'{username},{password},{status}\n')
    return 'user added succesfully'

def find_user(username):
    dic_user={}
    with open(users_txt,'r')as file:
        for line in file:
            data=line.strip().split(',')
            if username.lower()==data[0].lower():
                dic_user={'username':data[0],
                          'password':data[1],
                          'status':data[2]
                          }
                return dic_user
        return None
def delet_user(username):
    with open(users_txt,'r')as file:
        lines=file.readlines()
        found=False
        
    with open(users_txt,'w')as file :
        for line in lines:
            data=line.strip().split(',')
            if username.lower()==data[0].lower():
                found=True
               
            else:
                file.write(line)
                return ' user not found'
            
        if found:
              return 'user deleted successfully'
        else:
              return ' user not found'
            
        
def generat_report():
    active=0
    bloked=0
    with open(users_txt,'r')as file :
        for line in file:
            data=line.strip().split(',')
            if data[2]=='active':
                active+=1
                
            else:
                bloked+=1
        
        return { 'active':active,
                'bloced':bloked}
    
print(add_user('mohamad',137786, 'bloked'))
print(find_user('ali'))
print(delet_user('Rzea'))
print(generat_report())
        
        
        
        
        
        
        
        
        
        
        
        
        
        