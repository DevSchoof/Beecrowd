# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while True:
    try:
        linha = input().split()
        if not linha:
            break
        
        h1, m1, h2, m2 = map(int, linha)
    
        if h1==0 and m1==0 and h2==0 and m2==0:
            break
        
        if h1<0 or m1<0 or h2<0 or m2<0:
            break
        
        if h1>23 or h2>23 or m1>59 or m2>59:
            break
    
        tm = (h2*60 + m2) - (h1*60 + m1)
    

        
        if tm <= 0:
            tm += (24*60)
        print(tm)
    except (EOFError, ValueError):
        break
