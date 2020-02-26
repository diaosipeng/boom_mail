#!/bin/bash


import yagmail
with open('./config.txt','r',encoding='utf-8') as f:
    object_mail = f.readlines()[0]
yag = yagmail.SMTP(user='3172700250@qq.com',password='uvqrtexrwvledgdc',host='smtp.qq.com',port=25,smtp_ssl=True)                               
content = ['刁思鹏尝试轰炸你一下']
num = 0
while True:
    if str(num) == '50':
        break
    try:
        yag.send(to=object_mail,subject='收到没有?试验一下,这是第%s封' % str(num+1),contents=content)
        num += 1
    except:
        print('发出去了{}封'.format(str(num)))
        
