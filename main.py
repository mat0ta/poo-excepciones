import sys
sys.path.insert(1, './modules')
from modules import email
from src.totareadme import readme

array_ejercicios = {
  1: 'email.comprobarMail()'
}

if __name__ == "__main__":
    readme('C:/Users/marti/Documents/GitHub/poo-excepciones')
    start = input('Bienvenido a la plataforma de ejercicios de excepciones. Por favor, introduzca el número del ejercicio que quiere probar (1) o introduzca 0 para salir: ')
    while int(start) >= 1 and int(start) <= 2:
        eval(str(array_ejercicios[int(start)]))
        start = input('Por favor, introduzca el número del ejercicio que quiere probar (1) o introduzca 0 para salir: ')