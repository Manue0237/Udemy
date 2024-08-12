from random import randint


nombre= input('Ingrese su nombre: ')

print(f'Hola {nombre} descubre el numero secreto del 1 al 100 en 8 intentos')

numero_secreto = randint(1,100)
intentos = 0
numero_usuario = int(input('Adivina el numero secreto: '))


while numero_secreto != int(numero_usuario):
    intentos += 1
    if intentos == 8:
        print('Perdiste')
        break
    if numero_usuario<1 or numero_usuario>100:
        print('Numero fuera de rango')
        numero_usuario = int(input('Adivina el numero secreto: '))
        continue
    elif numero_usuario > numero_secreto:
        print('El numero secreto es menor')
        numero_usuario = int(input('Adivina el numero secreto: '))
        continue
    elif numero_usuario < numero_secreto:
        print('El numero secreto es mayor')
        numero_usuario = int(input('Adivina el numero secreto: '))
        continue

else:
    print(f'Adivinas el numero secreto {numero_usuario} en {intentos} intentos')