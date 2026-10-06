# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 01:30:33 2026

@author: 10
"""

def get_values():
    a=int(input('enter number:'))
    list1=[]
    for i in range(a):
        value=input('enter your list:')
        list1.append(value)
        
    return list1    
#print(get_values())

def add_uniqe(value,uniqe_list,position_list,position):
    if value=='':
        return 'empty'
    duplicate=False
    for item in uniqe_list:
        if value.lower==item.lower:
            duplicate=True
            index=uniqe_list.index(item)
            first_position=position_list[index]
    if duplicate==False:
        uniqe_list.append(value)
        position_list.append(position)
        return 'new'
    else:
        return 'duplicate',first_position
    
            
    uniqe_list=[]
   
    list1=get_values()
    for value in list1:
       result=add_uniqe(value, uniqe_list)
    print(result) 
   

def process_values():
    
    list1=get_values()
    uniqe_list=[]
    position_list=[]
    unique_count=0
    duplicate_count=0
    position=1
    for value in list1:
        result=add_uniqe(value, uniqe_list,position_list,position)
        position+=1
        if result=='new':
            unique_count+=1
        else:
            duplicate_count+=1
    return uniqe_list,unique_count,duplicate_count        
def show_report():
    uniqe_list,uniqe_count,duplicate_count,position_list=process_values()
      
    print('uniqe list:',uniqe_list)
    print ('len duplicate:',duplicate_count)
    print ('uniqe_count:',uniqe_count)
    print('first positions:')
    for i in range(len(uniqe_list)):
        print(uniqe_list[i],':',position_list[i])
show_report()    
    
    
    
    