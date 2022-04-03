<h1 align="center">POO-EXCEPCIONES</h1>

En este [repositorio](https://github.com/mat0ta/poo-excepciones) quedan resueltos los ejercicios la tarea de esta semana. Puedes encontrar otros proyectos y tareas en mi perfil de GitHub: [mat0ta](https://github.com/mat0ta).

<h2>Comprobacion del email</h2>

Crear un algoritmo usando el modulo re para combrobar si el email introducido es o no correcto

El c�digo empleado para crear dicho algoritmo es el siguiente:

```py

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

```

