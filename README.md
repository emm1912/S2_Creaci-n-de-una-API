# Creación de una API
Ejercicios de prueba para NT, resumen de programas utilizados:
* IDE PyCharm 2023.1.1
* Python 3.11

Estructura del proyecto:

<code>
├── main.py
└── README.md

</code>


## Description
Calcular el numero faltante de un conjunto de los primeros 100 números naturales del cual se extrajo uno.

Especificaciones:
* La aplicación se debe implementar con python.
* Se debe de implementar una clase que represente al conjunto de los primero 100 números naturales.
* La clase implementada debe de tener el método Extract para extraer un cierto número deseado.
* La clase implementada debe de poder calcular que numero se extrajo y presentarlo.
* Debe de incluir validación del input de datos (numero, número menor de 100).
* La aplicación debe de poder ejecutarse con un argumento introducido por el usuario, que utilice nuestra clase y muestre que pudo calcular que número se extrajo.

#### PyCharm
El codigo se escribio con IDE PyCharm, no se necesitaron librerias extra. 

## Comentarios
La parte mas interesante de este ejercicio fue encontrar el metodo de obtener el numero que se extrae de la lista de los 100 numeros naturales, ya que hay diversas maneras:
* Utilizando la formula de sumatoria
* Utilizando la tecnica de XOR
* Utilizando la tecnica de Hashing

Se recomienda para conjuntos mas largos utilizar la tecnica de XOR ya que no hay riesgo de que ocurra un desborde de memoria si fuera un conjunto muy largo y este riesgo
tambien existe con la tecnica de Hashing.

Pequeña descripción de uso:
Al iniciar el programa este pide un numero a retirar, el cual se remueve de la lista y se calcula por medio de la formula de sumatoria. Seguido nos muestra la lista sin el
numero seleccionado (a valores cada nueva linea) y nso dice el numero extraido resultado del calculo.


## Para finalizar
El codigo probado.
![Screenshot](/Images/fin.png)
Si se ingresa un numero menor a 100.
![Screenshot](/Images/fin2.png)
Si se ingresa cero.
![Screenshot](/Images/fin3.png)
Si no se ingresa un digito.
![Screenshot](/Images/fin4.png)
