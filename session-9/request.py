# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 22:35:49 2026

@author: 10
"""

class Request:
    def __init__(self,id_r,title,assignee,priority,status):
        self.id_r=id_r
        self.title=title
        self.assignee=assignee
        self.priority=priority
        self.status=status
    def __str__(self):
        return f'id_r:{self.id_r},title:{self.title},\
            assignee:{self.assignee},priority:{self.priority},\
            status:{self.status}'
         

       