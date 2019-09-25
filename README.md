# Curso Practico de Python

## Funiciones basicas.

### Archivo Main

Todo punto de entrada o archivo principal es declarado con la sentencia.

```python
if __name__ == '__main__':
	pass
```

### None

Declara que la variable tiene un espació pero este no tiene un valor.

```python
client_name = None
```

### Revisar el tipo de dato.

```python
type($variable)
```

### Parsear Datos.

```python
int($variable)
str($variable)
bool($variable)
float($variable)
```

### Declaracion de una función.

```python
suma_de_dos_numeros(x, y):
	return x + y
```

## Scope

Dentro de python el scope funciona de tal forma que una variable global no es visible para las demas funciones, amenos que esta sea invocada explicitamente.

Aunque si solo invocas la variable pero no la modificas no es necesario agregar el global.

```python
clients='pablo,ricardo,'


def create_client(client_name):
  #Llamando a la variable global clients.
    global clients
    clients+= client_name


if __name__ == '__main__':
    clients += 'david'
    print(clients)
```

## Condicionales.

```python
if condicion:

elif condicion:

else:
```



## Strings en Python.

Declaracion y operaciones con Strings.

```python
country = "Colombia"

#Longitud.
len(country)

#Convierte a mayusculas.
country.upper()

#Convierte a minusculas.
country.lower()

#Busca una determinada cadena y devuelve el indice de la primera coincidencia.
country.find()

#Si empieza con determinado caracter.
country.startswith()

#Si termina con determinado caracter.
country.endswith()

#Convierte la primera letra en mayuscula.
country.capitalize()

#Si todos los valores son alfabeticos.
country.isalpha()

#Si todos los valores son digitos.
country.isdigit()

```

## Direcciones de memoria.

Para buscar donde vive la variable se ocupa la funcion id

```python
id(variable)
```

## Metodos de un objeto.

Para ver los metodos que tiene un objeto se ocupa el metodo dir()

```python
dir(platzi)
```

Donde todos los metodos que tenga doble guion bajo al final y al principio son metodos que se pueden sobre escribir.

```
__METODO__
```

## DocStrings

Es la forma de dar documentacion al codigo en python.

```python
def my_function():
	""" Descripcion del metodo"""
	pass
```

Esta se puede mostrar ocupando el método.

```python
help(my_function)
```

## Slices

Son rebanadas de cadenas o Listas. Estos tienen un Comienzo un Fin y los pasos que son de cuanto en cuanto se tomaran los elementos.

```python
my_name = 'Claudio'

my_name[Comienzo:Final:pasos]
```

## For loops

La funcion range(10) retorna un rango del 0 al 9.

```python
for i in range(10):
	print(i)
```

## While loops

Sirven para iterar mientras una condición sea verdadera.

```python
while n > 0:
	print(n)
	n-= 1
```

### Operador not

El operador not se utiliza para verificar si una variable existe o contiene algo.

```python
def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name?')
    
    return client_name

```

