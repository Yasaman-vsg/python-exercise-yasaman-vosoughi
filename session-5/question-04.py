# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 01:42:03 2026

@author: 10
"""

s=input('enter your sentences:')
l=s.split()

c=0
most_common_word=''
word={}
for i in l:
    if i in word:
        word[i]=word[i]+1
    else :
        word[i]=1
   
for   i,count in word.items():
      if count>c:
          c=count
          most_common_word=i
print('most_common_word=',most_common_word)          