# Creación de una API
Ejercicios de prueba para NT, resumen de programas utilizados:
* IDE PyCharm 2023.1.1
* Python 3.11

Estructura del proyecto:

<code>
├── Images
├── main.py
└── README.md

</code>

## Descripción
Realizar una API que calcule el numero faltante de un conjunto de los primeros 100 números naturales del cual se extrajo uno.
 
Especificaciones:
* La aplicación se debe implementar con python.
* Se debe de implementar una clase que represente al conjunto de los primero 100 números naturales.
* La clase implementada debe de tener el método Extract para extraer un cierto número deseado.
* La clase implementada debe de poder calcular que numero se extrajo y presentarlo.
* Debe de incluir validación del input de datos (numero, número menor de 100).
* La aplicación debe de poder ejecutarse con un argumento introducido por el usuario, que utilice nuestra clase y muestre que pudo calcular que número se extrajo.

Para ejecutar la API usar lo siguiente en la terminal:
<code>uvicorn main:app --reload</code>


![Screenshot](/Images/test1.png)

Al utilizar "--reload" con uvicorn la API se recarga constantemente, en la terminal nos mostrara la ip donde encontraremos la API con su puerto:
<code>INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)</code>

Ingresamos la ip "http://127.0.0.1:8000" en nuestro explorador y tendremos los siguientes endpoints disponibles

### "/listAll": 
Se accede a este endpoint usando -> http://127.0.0.1:8000/listAll y nos devuelve todos los numeros que estan en la lista actualmente.

![Screenshot](/Images/listAll.png)

### "/extract": 
Se accede a este endpoint usando -> http://127.0.0.1:8000/extract, pero para poder probar este endpoint desde el explorador 
ingresar -> http://127.0.0.1:8000/docs#/default/extractNumber_extract_delete y dar click en el boton superior derecho "Try it out" e ingresar en Parametros el numero a 
extraer de la lista seguido presionar "Execute".

Si el borrado es satisfactorio nos devolvera una respuesta "Exito!": "Numero Borrado".

![Screenshot](/Images/exitoborrado.png)

### "/faltante": 
Se accede a este endpoint usando -> http://127.0.0.1:8000/faltante solo nos devolvera el numero calculado faltante de la lista.

![Screenshot](/Images/faltante.png)

## PyCharm
El codigo se escribio con IDE PyCharm, se instalaron algunas librerias las cuales se puden agregar desde la siguiente ventana 
![Screenshot](/Images/pythonInterpreter.jpg)

Accede a esta ventana desde File -> Settings -> Project (name) -> Python Interpreter.

Las librerias necesarias son:
* fastapi 0.98.0
* uvicorn 0.22.0

###### Tambien se pueden instalar de manera manual con el archivo "requirements.txt" si se requiere.

## Comentarios
Fue muy interesante investigar como poder mandar llamar el metodo de una clase con "FastApi" ya que es la primera vez que utilizo dicha libreria (he utilizado django),
ademas analizar cuales verbos HTTP serian los mas adecuados de utilizar.

Se utilizaron los siguientes verbos HTTP:
* GET: Para obtener la lista completa de numeros y para pedir al metodo "extractNumber" (endpoint "/faltante") nos devuelva el numero faltante calculado de la lista.
* DELETE: Para eliminar un numero deseado de la lista.

Otra parte interesante de este ejercicio fue encontrar el metodo para calcular el numero que se extrajo de la lista, ya que hay diversas maneras:
* Utilizando la formula de sumatoria
* Utilizando la tecnica de XOR
* Utilizando la tecnica de Hashing

Se recomienda para conjuntos mas largos utilizar la tecnica de XOR ya que no hay riesgo de que ocurra un desborde de memoria si fuera un conjunto muy largo (este riesgo
tambien existe con la tecnica de Hashing).

## Para finalizar imagenes de algunas excepciones.

Si se ingresa un numero mayor a 100.

![Screenshot](/Images/mas101.png)

Si se ingresa un numero menor a cero.

![Screenshot](/Images/cero.png)

Si ya se borro el numero en la lista.

![Screenshot](/Images/yaborrado.png)

Si aun no se borra ningun numero y se usa el endpoint "/faltante".

![Screenshot](/Images/notmissing.png)
