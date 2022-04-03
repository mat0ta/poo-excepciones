from math import comb
import re
email = ''

def comprobarMail():
    global email
    if email == '':
        email = str(input('Por favor, introduzca su email: '))
    busqueda = ['@', '.']
    for i in range(len(busqueda)):
        result = re.search(busqueda[i], email)
        if result == None:
            email = str(input('Email no váido, por favor, introduzcalo de nuevo: '))
            return comprobarMail()
    print('Email válido, gracias.')

comprobarMail()