from random import randint

def obtener_numero_intentos():
    while True:
        try:
            numero_intentos = int(input('ingrese el numero de intentos (1-10): '))
            if 1 <= numero_intentos <=10:
                return numero_intentos
            else:
                print('el numero de intentos debe estar entre 1-10 ')
        except ValueError:
            print('ingrese un numero entero.')

intentos = obtener_numero_intentos()
contador = 0
numero_computador = randint(1,10)

while contador <= intentos:
    print('juego de adivinanza')
    numero_usuario = int(input('ingrese un numero entre 1 y 25: '))
    contador += 1
    
    if numero_computador > numero_usuario:
        print('intenta con un numero mayor ')
    elif numero_computador < numero_usuario:
        print('intenta con un numero menor')
    else:
        print(f'el numero {numero_computador}, es correcto, lo lograste en {contador} intentos')
        break
