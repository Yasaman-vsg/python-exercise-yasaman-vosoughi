# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:29:26 2026

@author: 10
"""
age_sum={}
langu_dic={}
avrage={}
oldest={}
most_used=''
max_count=0
users = [
('Ali', 25, 'Python'),
('Sara', 30, 'Java'),
('Reza', 22, 'Python'),
('Mina', 28, 'C++'),
('John', 35, 'Python'),
('David', 30, 'Java')
] 
for n,age,l in users:
    if l not in langu_dic:
        langu_dic[l]=n
    else:
        langu_dic[l]+=', '+n
for l,n in langu_dic.items():
    print(l,':',n)
for n,age,l in users:
    if l not in age_sum:
        age_sum[l]=age
    else:
         age_sum[l]+=age
for l in age_sum:
    avrage[l]=age_sum[l]/len(langu_dic[l])  
print(avrage) 
    
for n,age,l in users:   
    if l not in oldest:
        oldest[l]=(n,age )
    elif age>oldest[l][1]:
        oldest[l]=(n,age)
        
print(oldest)        

for l in langu_dic:
      if len(langu_dic[l])>max_count:
          max_count=len(langu_dic[l])
          most_used=l
          
print('most used:',most_used)          
        