# -*- coding: utf-8 -*-

def encontrar_solitario():
    try:
        n = int(input())
        
        # O problema termina quando N é 0
        if n == 0:
            return
        
        # Lê os próximos N números
        entrada = list(map(int, input().split()))
        
        solitario = 0
        for item in entrada:
            solitario ^=item  # Aplica o XOR            
        print(solitario)
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    encontrar_solitario()