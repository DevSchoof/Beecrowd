# -*- coding: utf-8 -*-



while True:
    try:
        casos = int(input())
    except (ValueError, EOFError):
        continue
    if 0 < casos < 10001:
        break

for c in range(casos):
    while True:
        try:
            texto = str(input())
        except (ValueError, EOFError):
            continue
        if 0 < len(texto) < 1001:
            break
                
        
    resultado = ''.join(chr(ord(ch) + 3) if ch.isalpha() else ch for ch in texto)
    resultado = resultado[::-1]

    metade = len(resultado) // 2
    resultado = resultado[:metade] + ''.join(chr(ord(ch) - 1)  for ch in resultado[metade:])

    print(resultado)