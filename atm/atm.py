# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 00:41:56 2026

@author: 10
"""

print('\n','    *خوش امدید*','\n')
mojodi=500000
ramz=2020
tekrar=0
while True:
    v=int(input('رمز خودرا وارد کنید:'))
    if v==ramz:
        print('منو :')
        x=['\n','مشاهده موجودی','\n','واریز وجه','\n','برداشت وجه','\n','تغیر رمز','\n','خروج']
        c=0
        for i in x:
            if i!='\n':
              c=c+1
              print(c,'-',i)
        n=int(input('عدد گزینه مورد نظر را وارد کنید:'))
        if n==1 :
            print('500000')
        elif n==2 :
           s=int(input('مبلغ را وارد نمایید:'))
           if  s<=0 :
               print('مبلغ وارد شده قابل قبول نیست')
               s=int(input('مبلغ را وارد نمایید:'))
               if s>0 :
                   mojodijadid=s+mojodi 
                   print('درخواست شما با موفقیت انجام شد')
                   print('موجودی جدید:',mojodijadid)  
           elif s>0 :
               mojodijadid=s+mojodi 
               print('درخواست شما با موفقیت انجام شد')
               print('موجودی جدید:',mojodijadid)   
        elif n==3:
            
            s=int(input('مبلغ را وارد نمایید:'))
            while s>500000 :
                print('موجودی کافی نمیباشد')
                s=int(input('مبلغ را وارد نمایید:'))
            if s%100==0 :
                mojodijadid=mojodi-s
                print('درخواست شما با موفقیت انجام شد')
                print('موجودی جدید :',mojodijadid)
            while s%100!=0 :
                print('مبلغ وارد شده باید مضربی از 100 باشد')
                s=int(input('مبلغ را وارد نمایید:'))
                mojodijadid=mojodi-s
                print('درخواست شما با موفقیت انجام شد')
                print('موجودی جدید :',mojodijadid)
        elif n==4:
            while True:
                r=int(input('رمز قبلی را وارد کنید:'))
                if r==ramz:
                   ramz1=int(input('رمز جدید را وارد کنید:'))
                   ramz2=int(input('رمز جدید را مجدد وارد کنید:'))
                   if ramz1==ramz2:
                       ramz=ramz1
                       print('رمز با موفقیت تغییر یافت')
                       break
                   else : print('رمز مجدد اشتباه است')
                       
                else: print('رمز وارد شده صحیح نمیباشد') 
        elif n==5:
            print('روز خوبی داشته باشین خدانگهدار')
      
    else :
        tekrar=tekrar+1
        if tekrar>2:
          print('شما بلاک شدید')
          break
        print('رمز اشتباه است')            
           
        
    
