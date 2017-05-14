# -*- coding: utf-8 -*-
posts = [] 
with open('C:\DB\Kurgansky_vowpal_wabbit.txt', 'r', encoding = 'utf-8') as f: 
    for s in f: 
        posts.append(s[6:])
