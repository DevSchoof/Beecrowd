# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
def encontrar_diamantes():
    try:
        n = int(input())
        for _ in range(n):
            linha = input().strip()
            diamantes = 0
            abertos = 0
            for item in linha:
                if item == '<':
                    abertos += 1
                elif item == '>' and abertos > 0:
                    diamantes += 1
                    abertos -= 1
            print(diamantes)



    except (EOFError, ValueError):
        pass
if __name__ == "__main__":
    encontrar_diamantes()
