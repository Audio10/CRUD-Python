









# Introducción a PEP-8.

## Indentación.

Al programar en Python, la sangría es algo que definitivamente va a utilizar. Sin embargo, hay que tener cuidado con él, ya que puede conducir a errores de sintaxis. Por lo tanto, la recomendación es usar 4 espacios para el sangrado. Por ejemplo, esta declaración usa 4 espacios de sangría:

```python
if True:
    print("If works")
```

Y también este bucle con la declaración de impresión tiene sangría con 4 espacios:

```
for element in range(0, 5):
    print(element)
```

# 1.- Básicos del Lenguaje

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

# 2.- Uso de strings y ciclos.

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

# 3.- Estructuras de datos

## Listas

Python y todos los lenguajes nos ofrecen *constructos* mucho más poderosos, haciendo que el desarrollo de nuestro software sea

- Más sofisticado
- Más legible
- Más fácil de implementar

Estos *constructos* se llaman **Estructuras de Datos** que nos permiten agrupar de distintas maneras varios valores y elementos para poderlos manipular con mayor facilidad.

Las **listas** las vas a utilizar durante toda tu carrera dentro de la programación e ingeniería de Software.

Las **listas** son una secuencia de valores. A diferencia de los *strings*, las **listas** pueden tener cualquier tipo de valor. También, a diferencia de los strings, son mutables, podemos agregar y eliminar elementos.

En Python, las listas son referenciales. Una lista no guarda en memoria los objetos, sólo guarda la **referencia** hacia donde viven los objetos en memoria

Se inician con `[]` o con la *built-in function* `list`.

### Declaración.

```python
countries = ['Mexico', 'Venezuela','Colombia']
```

### Agregar elementos.

```python
countries[0] = 'Ecuador'
```

## Alias

Es cuando una variable apunta a otra en este caso **countries** ya existe pero **global_countries** no y a esta se le asigna **countries**. Por lo cual si se alteran una variable se cambia la otra.

```python
global_countries = countries
```

## Modulo copy (Copiar listas).

- Para copiar listas y evitar errores de alias se ocupa el modulo copy que permite copiar listas sin afectar la lista original.

```python
import copy

countries = ['Mexico', 'Venezuela','Colombia']

# Donde el metodo copy copia la lista en una nueva variable sin hacer alias.
global_countries = copy.copy(countries)


```

- Aunque no es la unica forma de copiar listas. puedes utilizar el método list.copy método interno (disponible desde Python 3.3):

```python
global_countries = countries.copy()
```

- Hacer Slice.

```python
global_countries = countries[:]
```

- Puedes usar la built in function **list()**

```python
new_list = list(old_list)
```

- Si quieres copiar Objetos dentro de una lista tal cual.

```python
import copy
new_list = copy.deepcopy(old_list)
```

## Ciclar en una lista

```python
for country in countries:
	print(country)
```

## Operadores con Listas.

Ahora que ya entiendes cómo funcionan las **listas**, podemos ver qué tipo de operaciones y métodos podemos utilizar para modificarlas, manipularlas y realizar diferentes tipos de cómputos con esta Estructura de Datos.

- El operador **+(suma)** concatena dos o más listas.
- El operador ***(multiplicación)** repite los elementos de la misma lista tantas veces los queramos multiplicar

Sólo podemos utilizar **+(suma)** y ***(multiplicación)**.

Las listas tienen varios métodos que podemos utilizar.

- `append` nos permite añadir elementos a listas. Cambia el tamaño de la lista.

- `pop` nos permite sacar el último elemento de la lista. También recibe un índice y esto nos permite elegir qué elemento queremos eliminar.

  ```
  # Por indice
  some_frunt = fruits.pop(0)
  # Cualquier elemento
  some_frunt = fruits.pop()
  ```

- `sort` modifica la propia lista y ordenarla de mayor a menor. Existe otro método llamado `sorted`, que también ordena la lista, pero genera una nueva instancia de la lista

  ```python
  for i in range(10):
       random_numbers.append(random.randint(0,15)) 
  
  random_numbers
  [4, 11, 5, 4, 8, 2, 9, 12, 9, 15]
  
  #Ordenando en nueva variable
  order_numbers = sorted(random_numbers)
  
  #Ordenando la misma lista
  order_numbers.sort()
  ```

- `del`nos permite eliminar elementos vía indices, funciona con *slices*

  

- `remove` nos permite es pasarle un valor para que Python compare internamente los valores y determina cuál de ellos hace match o son iguales para eliminarlos.

## Operaciones Listas en Proyecto

- Para agregar datos usamos **lista.append()**
- Para listar recorremos con un **enumerate** que te ayuda a recibir el índice del elemento.
- Para actualizar se busca por medio del método **index()** en donde esta el elemento y se remplaza.
- 

```python
clients=['pablo','ricardo']


def create_client(client_name):
    global clients

    if client_name not in clients:
        clients.append(client_name)
    else:
        print('Client already is in the client\'s list')


def list_clients():
    global clients

    for idx, client in enumerate(clients):
        print('{}: {}'.format(idx, client))


def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
    else:
        _not_found()


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        _not_found()


def search_client(client_name):
    global clients
    
    for client in clients:
        if client != client_name:
            continue
        else: return True
```

## Diccionarios.

Los diccionarios se conocen con diferentes nombres a lo largo de los lenguajes de programación como HashMaps, Mapas, Objetos, etc. En Python se conocen como **Diccionarios**.

Un diccionario es similar a una lista sabiendo que podemos acceder a través de un indice, pero en el caso de las listas este índice debe ser un número entero. Con los diccionarios puede ser cualquier objeto, normalmente los verán con **strings** para ser más explicitos, pero funcionan con muchos tipos de llaves…

Un diccionario es una asociación entre llaves(**keys**) y valores(**values**) y la referencia en Python es muy precisa. Si abres un diccionario verás muchas palabras y cada palabra tiene su definición.

### Declaración.

Para iniciar un diccionario se usa `{}` o con la función `dict`

Estos también tienen varios métodos. Siempre puedes usar la función `dir` para saber todos los métodos que puedes usar con un objeto.

Si queremos ciclar a lo largo de un diccionario tenemos las opciones:

**keys**: nos imprime una lista de las llaves
**values** nos imprime una lista de los valores
**items**. nos manda una lista de tuplas de los valores

###   Ciclar un Diccionario.



```
#Trae solo las claves
for key in my_dic.keys():
	pass

#Trae solo los valores
for key in my_dic.values():
	pass

#Trae clave y valor
for key, value in my_dic.items():
	pass
	
```

### Obtener un valor por llave

Dentro de la declaración **get** se establecen dos parámetros la llave por la cual se va a buscar el elemento y un valor default que es el que saldrá si no encuentra nada.

```
dic.get(llave, valor_defaul)
```

## **Tuplas y conjuntos**

### Tuplas

**PUEDE TENER DUPLICADOS**

Tuplas(**tuples**) son iguales a las listas, la única diferencia es que son **inmutables**, la diferencia con los *strings* es que pueden recibir muchos tipos valores. Son una serie de valores separados por comas, casi siempre se le agregan paréntesis para que sea mucho más legible.

Para poderla inicializar utilizamos la función `tuple`.

Uno de sus usos muy comunes es que cuando queremos regresar más de un valor en nuestra función.

Una de las características de las Estructuras de Datos es que cada una de ellas nos sirve para algo especifico. No existe en programación una navaja suiza que nos sirva para todos. los mejores programas son aquellos que utilizan la herramienta correcta para el trabajo correcto.

Declarar

```
tupla = (1,2,3)
```

### Conjunto

**NO TIENE DUPLICADOS**

Conjutos(**sets**) nacen de la teoría de conjuntos. Son una de las Estructuras más importantes y se parecen a las listas, podemos añadir varios elementos al conjuntos, pero **no pueden existir elementos duplicados**. A diferencia de los **tuples** podemos agregar y eliminar, son **mutables**.

Los sets se pueden inicializar con la función **set**. Una recomendación es inicializarlos con esta función para no causar confusión con los diccionarios.

- `add` nos sirve añadir elementos.
- `remove` nos permite eliminar elementos.

