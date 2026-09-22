# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 00:49:42 2026

@author: 10
"""

def analyze_text(text):
    list_letters=[]
    dic_letters={}
    words=[]
    cdigit=0
    most_letter_count=0
    most_letter=''
    most_word=''
    most_word_count=0
    dic_word={}
    for letter in text:
        list_letters.append(letter)
        words=text.split()
        bigest_word=max(words, key=len)
    for i in list_letters:
        if i not in dic_letters:
            dic_letters[i]=1
        else:
            dic_letters[i]+=1
    
        if i.isdigit():
            cdigit+=1
    for l,c in dic_letters.items():
        if c>most_letter_count:
            most_letter_count=c
            most_letter=l
            
    for word in words:
       
        if word not in dic_word:
            dic_word[word]=1
        else:
            dic_word[word]+=1
    for word,c in dic_word.items():
         if c>most_word_count:
             most_word_count=c
             most_word=word   
        
    print('letter:',len(list_letters))
    #print('letters:',dic_letters)
    print('worlds:',len(words))
    print('digit:',cdigit)
    print('most letters:',most_letter)
    print('most world:',most_word)
    print('bigest world:',bigest_word)        
text=input('enter text:')
analyze_text(text)          
            
            
            
            