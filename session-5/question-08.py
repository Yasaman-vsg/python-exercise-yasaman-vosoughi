# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 14:14:57 2026

@author: 10
"""

my_str=input('enter str:')
total_characters=len(my_str)
total_letters=0
total_digit=0
total_lawercase=0
total_uppercase=0
total_space=0
for i in my_str:
    if i.isalpha():
        total_letters+=1
        if i.islower():
            total_lawercase+=1
        if i.isupper():
             total_uppercase+=1  
    if i.isdigit():
        total_digit+=1
    if i.isspace():
        total_space+=1
        
my_dic1={}
num_rep_char=0
for i in my_str:
    if i in my_dic1:
        my_dic1[i]+=1
    else:
        my_dic1[i]=1
for i,j in my_dic1.items():
    if j>num_rep_char:
        num_rep_char=j
        most_rep_char=i
        
my_list=my_str.split()
total_words=len(my_list)
my_dic2={}
num_rep_word=0
for i in my_list:
    if i in my_dic2:
         my_dic2[i]+=1   
    else :
        my_dic2[i]=1
for i,j in my_dic2.items():
    if j>num_rep_word:
        num_rep_word=j
        most_rep_word=i
len_max=0
len_min=1000000        
for i in my_dic2:
    if len(i)>len_max:
        len_max=len(i)
        longest_word=i
    if len(i)<len_min and i!=' ':
        len_min=len(i)
        shortest_word=i
print('total charactar:',total_characters,'\n'
      'total letters:',total_letters,'\n'
      'total world:',total_words,'\n'
      'total digits:',total_digit,'\n'
      'total spaces:',total_space,'\n'
      'total uppercase::',total_uppercase,'\n'
      'total lowercase:',total_lawercase,'\n'
      'longest word:',longest_word,'\n'
      'shortes word:',shortest_word,'\n'
      'most repeated charactar:',most_rep_char,'\n'
      'most repeated world:',most_rep_word)        