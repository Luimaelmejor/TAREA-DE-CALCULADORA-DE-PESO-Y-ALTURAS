peso_libras = float(input('Ingrese su peso en libras: '))
altura_metros = float(input('Ingrese su altura en metros: '))
peso_kg = peso_libras / 2.20462262
indice_masa_corporal = peso_kg / (altura_metros ** 2)
print(f'Su índice de masa corporal (IMC) es: {indice_masa_corporal:.2f}')