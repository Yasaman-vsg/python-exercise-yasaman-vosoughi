# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 23:00:23 2026

@author: 10
"""

from request import Request
tasks={101:{
    'id':101,
     'title':'fix login bug',
     'assignee':'ali',
     'priority':'high',
     'status':'open'},
     102:{'id':102,
          'title':'update api',
          'assignee':'sara',
          'priority':'medium',
          'status':'in_progress'},
     103:{'id':103,
          'title':'wright tests',
          'assignee':'ali',
          'priority':'low',
          'status':'done'},
     
       }
class Requestmanager:
    def __init__(self,tasks):
        self.tasks=tasks
        
    def create(self,id_r,title,assignee,priority,status):
        if priority not in ['low','high','medium']:
            print('invalid priority')
            return
        if status not in ['open','in_progress','done']:
            print('invalid status')
            return
        
        if id_r not in self.tasks:
            self.tasks[id_r]={'id':id_r,
                             'title':title,
                             'assignee':assignee,
                             'priority':priority,
                             'status':status}
            print('request created succesfully')
        else:
            print('exist')
            
    def read(self,id_r=None):
        if id_r is None :
            for task in self.tasks.values():
                print(task)
        else:
            if id_r in self.tasks:
                print(self.tasks[id_r])
            else:
                print('id not exist')
                
    def update(self,id_r,title=None,assignee=None,priority=None,status=None):
         if id_r in self.tasks:
             if title is not None:
                 self.tasks[id_r]['title']=title
             if assignee is not None:
                 self.tasks[id_r]['assignee']=assignee
             if priority is not None:
                 if priority not in ['high','medium','low']:
                     print('invalid priority')
                     return
                 else:
                     self.tasks[id_r]['priority']=priority
             if status is not None:
                 if status  not in ['open','in progress','done']:
                     print('invalid status')
                     return
                 self.tasks[id_r]['status']=status    
         
         elif id_r not in self.tasks:
             print('Request not found')
             return
             
    def  delete(self,id_r):
        if id_r in self.tasks:
            del self.tasks[id_r]
            print('delete successfulli')
            
        else:
            print('id not exist')
             
manager=Requestmanager(tasks)   
print('1-created Request')  
print('2-read Request')
print('3-update')
print('4-delete')
print('5-exit')
while True:
    request=input(' enter your Request number:')
    if request=='1':
        id_r=int(input('id:'))
        title=input('title:')
        assignee=input('assignee:')
        priority=input('priority:')
        status=input('status:')
        manager.create(id_r,title,assignee,priority,status)
    if request=='2':
       id_input=input('id:')
       if id_input.strip()=='':
           manager.read()
       else: 
           id_r=int(id_input)
           manager.read(id_r)
    if request=='5':
        break
    if request=='3':
        
        id_r=int(input('id:'))
        title=input('title:')
        assignee=input('assignee:')
        priority=input('priority:')
        if priority=='':
            priority=None
        
        status=input('status:')
        if status=='':
            status=None
        manager.update(id_r,title=None,assignee=None,priority=None,status=None)        
             
    if request=='4':
        id_r=int(input('id:')) 
        manager.delete(id_r)
      
            
                
            
            
            
            
            
            
            
            
            