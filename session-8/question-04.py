# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 01:30:33 2026

@author: 10
"""

def get_values():
    a=int(input('enter number:'))
    list1=[]
    for i in range(1,a):
        i=input('enter your list:')
        list1.append(i)
        
    return list1    


def add_uniqe():
    uniqe_list=[]
   
    list1=get_values()
    for i in list1:
        if i not in uniqe_list:
            uniqe_list.append(i)
            
        else:
            pass
        
    return uniqe_list 
   

def process_values():
    
    list1=get_values()
    uniqe_list=add_uniqe()
    len_uniqe=len(uniqe_list)
    len_duplicate=len(list1)-len(uniqe_list)
    return len_duplicate,len_uniqe
print(process_values())    
def show_report():
    uniqe_list=add_uniqe()
    len_duplicate=process_values()
    len_uniqe=process_values()  
    return 'uniqe list:',uniqe_list,'\n','len duplicate:',len_duplicate,'\n','len uniqe:',len_uniqe
   
print(show_report())    
    
    
    
    