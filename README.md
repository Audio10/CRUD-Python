# Introducción a PEP-8.

[Articulo Original](https://www.datacamp.com/community/tutorials/pep8-tutorial-python-code#intro)

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

Cuando escribe una expresión grande, es mejor mantener la expresión alineada verticalmente. Cuando haga esto, creará una "sangría colgante".

Estos son algunos ejemplos de sangría colgante en expresiones grandes, que muestran algunas variaciones de cómo puede usarlo:

```
value = square_of_numbers(num1, num2,
                       num3, num4)
```

```
def square_of_number(
     num1, num2, num3, 
     num4):
 return num1**2, num2**2, num3**2, num4**2
```

```
value = square_of_numbers(
              num1, num2,
              num3, num4)
```

```
list_of_people = [
 "Rama",
 "John",
 "Shiva"
]
```

```
dict_of_people_ages = {
 "ram": 25,
 "john": 29,
 "shiva": 26
}
```

Cada desarrollador, que trabaja con Python u otro lenguaje de programación, se hace la pregunta en algún momento si usar tabs o espacios para la sangría. La diferencia entre tabs y espacios es una discusión continua en la comunidad. Mira, por ejemplo, [este artículo](https://translate.googleusercontent.com/translate_c?depth=1&rurl=translate.google.com&sl=en&sp=nmt4&tl=es&u=https://stackoverflow.blog/2017/06/15/developers-use-spaces-make-money-use-tabs/&xid=17259,1500004,15700019,15700186,15700191,15700256,15700259,15700262,15700265&usg=ALkJrhhmbN16ZVBAssV9SLNQZk_wvpZHxQ) .

En general, los espacios son el medio de sangría preferido, pero si encuentra que algunos scripts de Python ya usan las tabs , debe seguir haciendo sangría con tabs. De lo contrario, debe cambiar la sangría de todas las expresiones en su script con espacios.

**Tenga en cuenta** que Python 3 no permite mezclar tabs y espacios para la sangría. ¡Es por eso que debes elegir uno de los dos y seguir con él!

## Longitud máxima de línea

En general, es bueno apuntar a una longitud de línea de 79 caracteres en su código Python.

Seguir este número objetivo tiene muchas ventajas. Algunos de ellos son los siguientes:

- Es posible abrir archivos uno al lado del otro para comparar;
- Puede ver toda la expresión sin desplazarse horizontalmente, lo que aumenta la legibilidad y la comprensión del código.

Los comentarios deben tener 72 caracteres de longitud de línea. ¡Aprenderá más sobre las convenciones más comunes para comentarios más adelante en este tutorial!

Al final, depende de usted qué convenciones y estilo de codificación le gusta seguir si trabaja en un grupo pequeño y es aceptable que la mayoría de los desarrolladores se desvíen de la guía de longitud máxima de línea. Sin embargo, si está realizando o contribuyendo a un proyecto de código abierto, probablemente quiera y / o deba cumplir con la regla de longitud máxima de línea establecida por PEP-8.

Mientras usa el operador `+` , puede usar mejor un salto de línea adecuado, lo que hace que su código sea más fácil de entender:

```
total = (A +
         B +
         C)
```

```
total = (A
         +   B
         +   C)
```

Alternativamente, también puedes escribir:

```
 total = A + B + C 
```

## Líneas en blanco

En los scripts de Python, la función y las clases de nivel superior están separadas por dos líneas en blanco. Las definiciones de métodos dentro de las clases deben estar separadas por una línea en blanco. Puede ver esto claramente en el siguiente ejemplo:

```python
class SwapTestSuite(unittest.TestCase):
    """
        Swap Operation Test Case
    """
    def setUp(self):
        self.a = 1
        self.b = 2

    def test_swap_operations(self):
        instance = Swap(self.a,self.b)
        value1, value2 =instance.get_swap_values()
        self.assertEqual(self.a, value2)
        self.assertEqual(self.b, value1)


class OddOrEvenTestSuite(unittest.TestCase):
    """
        This is the Odd or Even Test case Suite
    """
    def setUp(self):
        self.value1 = 1
        self.value2 = 2

    def test_odd_even_operations(self):
        instance1 = OddOrEven(self.value1)
        instance2 = OddOrEven(self.value2)
        message1 = instance1.get_odd_or_even()
        message2 = instance2.get_odd_or_even()
        self.assertEqual(message1, 'Odd')
        self.assertEqual(message2, 'Even')
```

Las clases `SwapTestSuite` y `OddOrEvenTestSuite` están separadas por dos líneas en blanco, mientras que las definiciones de métodos, como `.setUp()` y `.test_swap_operations()` solo tienen una línea en blanco para separarlas.

## Espacios en blanco en expresiones y declaraciones

Debe intentar evitar espacios en blanco cuando vea que su código está escrito tal como en los siguientes ejemplos:

```python
#DEBES USAR!!
func( data, { pivot: 4 } )
# Y NO!!
func(data, {pivot: 4})


#DEBES USAR!!
indexes = (0,)
# Y NO!!
indexes = (0, )


#DEBES USAR!!
if x == 4: print x, y; x, y = y, x
# Y NO!!
if x == 4 : print x , y ; x , y = y , x


#DEBES USAR!!
spam(1)
# Y NO!!
spam (1)

#DEBES USAR!!
dct['key'] = lst[index]
# Y NO!!
dct ['key'] = lst [index]


#DEBES USAR!!
x = 1
y = 2
long_variable = 3

# Y NO!!
x             = 1
y             = 2
long_variable = 3


#DEBES USAR!!
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# Y NO!!
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)



```

## Importaciones

Importar bibliotecas y / o módulos es algo que suele hacer cuando trabaja con Python para la ciencia de datos. Como ya sabrás, siempre debes importar las bibliotecas al comienzo de tu script.

**Tenga en cuenta** que si realiza muchas importaciones, debe asegurarse de indicar cada importación en una sola línea.

Eche un vistazo a la siguiente tabla para comprender esto un poco mejor:

```
#Deberías usar...	
from config import settings 
  
#O

import os 
import sys 
```

Además, debe tener en cuenta que hay un orden que debe respetar al importar bibliotecas. En general, puede seguir este orden:

1. Importaciones de bibliotecas estándar.
2. Importaciones de terceros relacionadas.
3. Aplicación local / importaciones específicas de la biblioteca.

## Comentarios.

Los comentarios se utilizan para la documentación en código en Python. Se suman a la comprensión del código. Existen muchas herramientas que puede utilizar para generar documentación, como comentarios y cadenas de documentos, para su propio módulo. Los comentarios deben ser más detallados para que cuando alguien lea el código, la persona obtenga la comprensión adecuada del código y de cómo se está utilizando con otras partes del código.

Los comentarios comienzan con el símbolo `#` . Cualquier cosa escrita después del hashtag no es ejecutada por el intérprete. Por ejemplo, el siguiente fragmento de código solo devolverá `"This is a Python comment"` .

```python
# This is a Python single line comment print("This is a Python comment") 
```

**Recuerde** : en la sección anterior, ¡leyó que los comentarios deben tener 72 caracteres de longitud de línea!

Dicho esto, hay tres tipos de comentarios:

- Utiliza los comentarios de bloque para explicar el código que es más complejo o desconocido para otros. Estos suelen ser comentarios de formato más largo y se aplican a algunos o todos los códigos que siguen. Los comentarios de bloque están sangrados al mismo nivel que el código. Cada línea de un comentario de bloque comienza con el hashtag `#` y un solo espacio. Si necesita usar más de un párrafo, deben estar separados por una línea que contenga un solo `#` .

Eche un vistazo al siguiente extracto, [tomado de la biblioteca `scikit-learn`](https://translate.googleusercontent.com/translate_c?depth=1&rurl=translate.google.com&sl=en&sp=nmt4&tl=es&u=https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/least_angle.py&xid=17259,1500004,15700019,15700186,15700191,15700256,15700259,15700262,15700265&usg=ALkJrhgxMEiYaV51XWGr3fM7y3B_WgikYg) , para comprender cómo son estos comentarios:

```python
if Gram is None or Gram is False:
        Gram = None
        if copy_X:
            # force copy. setting the array to be fortran-ordered
            # speeds up the calculation of the (partial) Gram matrix
            # and allows to easily swap columns
            X = X.copy('F')
```

- Debe usar los comentarios en línea con moderación, aunque pueden ser efectivos cuando necesita explicar algunas partes de su código. También pueden ayudarlo a recordar lo que significa una línea específica de código o puede ser útil cuando colabora con alguien que no está familiarizado con todos los aspectos de su código. Utiliza comentarios en línea en la misma línea de una declaración, siguiendo el código mismo. Estos comentarios también comienzan con `#` y un solo espacio.

Por ejemplo:

```
counter = 0 # initialize the counter 
```

Usted escribe cadenas de documentación o cadenas de documentación al comienzo de los módulos, archivos, clases y métodos públicos. Este tipo de comentarios comienzan con `"""` y terminan con `"""` :

```python
""" This module is intended to provide functions for scientific computing """ 
```

# 1.- Básicos del Lenguaje

## Funciones básicas.

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

### Declaración de una función.

```python
suma_de_dos_numeros(x, y):
	return x + y
```

### Visualización de funciones de un elemento o objeto.

**dir** es utilizado para imprimir todas las funciones disponibles por un objeto, elemento o tipo de dato.

```
dir(elemento)
```

## Scope

Dentro de python el scope funciona de tal forma que una variable global no es visible para las demás funciones, amenos que esta sea invocada explícitamente.

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

Declaración y operaciones con Strings.

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

Para buscar donde vive la variable se ocupa la función id

```python
id(variable)
```

## Funciones de un objeto.

Para ver los métodos que tiene un objeto se ocupa el método dir()

```python
dir(platzi)
```

Donde todos los métodos que tenga doble guion bajo al final y al principio son métodos que se pueden sobre escribir.

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

- Aunque no es la única forma de copiar listas. puedes utilizar el método list.copy método interno (disponible desde Python 3.3):

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

- `del`nos permite eliminar elementos vía índices, funciona con *slices*

  

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

Un diccionario es similar a una lista sabiendo que podemos acceder a través de un índice, pero en el caso de las listas este índice debe ser un número entero. Con los diccionarios puede ser cualquier objeto, normalmente los verán con **strings** para ser más explícitos, pero funcionan con muchos tipos de llaves…

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

## Tuplas

**PUEDE TENER DUPLICADOS**

Tuplas(**tuples**) son iguales a las listas, la única diferencia es que son **inmutables**, la diferencia con los *strings* es que pueden recibir muchos tipos valores. Son una serie de valores separados por comas, casi siempre se le agregan paréntesis para que sea mucho más legible.

Para poderla inicializar utilizamos la función `tuple`.

Uno de sus usos muy comunes es que cuando queremos regresar más de un valor en nuestra función.

Una de las características de las Estructuras de Datos es que cada una de ellas nos sirve para algo especifico. No existe en programación una navaja suiza que nos sirva para todos. los mejores programas son aquellos que utilizan la herramienta correcta para el trabajo correcto.

### Declarar

```
tupla = 1,2,3
tupla = (1,2,3)
```

### Acceso

El acceso es por índice.

```
tupla[0]
tupla[1]
```

### Funciones.

Solo cuenta con dos métodos públicos.

- **count** que retorna la cantidad de elementos que están repetidos dentro de la tupla.

```
a = (1,1,1,2,3,4)

a.count(1)
#3

a.count(2)
#2
```

- **index** que retorna el índice donde aparece por primera vez el elemento buscado.

```
a.index(1)
#0
```

## Conjunto

**NO TIENE DUPLICADOS**

Conjuntos(**sets**) nacen de la teoría de conjuntos. Son una de las Estructuras más importantes y se parecen a las listas, podemos añadir varios elementos al conjuntos, pero **no pueden existir elementos duplicados**. A diferencia de los **tuples** podemos agregar y eliminar, son **mutables**.

Los sets se pueden inicializar con la función **set**. Una recomendación es inicializarlos con esta función para no causar confusión con los diccionarios.

- `add` nos sirve añadir elementos.
- `remove` nos permite eliminar elementos.

### Declaración

```
a = set([1,2,3])

b = {3,4,5}


```

### Acceso

No se puede acceder por medio del índice solo se puede acceder.

### Agregación

Los elementos solo se agregan con la función add y estos solo se agregan si no hay algún duplicado dentro del set.

```
a.add(elemento)
```

### Operaciones

**intersection** sirve para todos los elementos que están en a como en b

```
a.intersection(b)
```

**union** une todos los elementos de ambos sets.

```
a.union(b)
```

**difference** imprime los elementos de a que no estan en b.

```
a.difference(b)
```

**difference** imprime los elementos de b que no estan en a.

```
b.difference(a)
```

**remove** elimina determinado elemento.

```
a.remove(elemento)
```

## Introducción al modulo collections.

El módulo collections nos brinda un conjunto de objetos primitivos que nos permiten extender el comportamiento de las built-in collections que poseé Python y nos otorga estructuras de datos adicionales. Por ejemplo, si queremos extender el comportamiento de un diccionario, podemos extender la clase UserDict; para el caso de una lista, extendemos UserList; y para el caso de strings, utilizamos UserString.

Por ejemplo, si queremos tener el comportamiento de un diccionario podemos escribir el siguiente código:

```python
class SecretDict(collections.UserDict):

   def _password_is_valid(self, password):
        …

    def _get_item(self, key):
        … 

    def __getitem__(self, key):
         password, key = key.split(‘:’)
         
         if self._password_is_valid(password):
              return self._get_item(key)
         
         return None

my_secret_dict = SecretDict(...)
my_secret_dict[‘some_password:some_key’] # si el password es válido, regresa el valor
```

Otra estructura de datos que vale la pena analizar, es namedtuple. Hasta ahora, has utilizado tuples que permiten acceder a sus valores a través de índices. Sin embargo, en ocasiones es importante poder nombrar elementos (en vez de utilizar posiciones) para acceder a valores y no queremos crear una clase ya que únicamente necesitamos un contenedor de valores y no comportamiento.

```python
Coffee = collections.NamedTuple(‘Coffee’, (‘size’, ‘bean’, ‘price’))
def get_coffee(coffee_type):
     If coffee_type == ‘houseblend’:
         return Coffee(‘large’, ‘premium’, 10)
```

El módulo collections también nos ofrece otros primitivos que tienen la labor de facilitarnos la creación y manipulación de colecciones en Python. Por ejemplo, Counter nos permite contar de manera eficiente ocurrencias en cualquier iterable; OrderedDict nos permite crear diccionarios que poseen un orden explícito; deque nos permite crear filas (para pilas podemos utilizar la lista).

En conclusión, el módulo collections es una gran fuente de utilerías que nos permiten escribir código más “pythonico” y más eficiente.

## Python comprehensions

Las Comprehensions son constructos que nos permiten generar una secuencia a partir de otra secuencia.

Existen tres tipos de comprehensions:

- List comprehensions

```python
[element for element in element_list if element_meets_condition]
```

- Dictionary comprehensions

```python
{key: element for element in element_list if element_meets_condition}
```

- Sets comprehensions

```python
{element for element in element_list if elements_meets_condition}
```

```python

#LISTAS
lista = list(range(100))
pares = [numero for numero in lista if numero % 2 ==0] 


#DICCIONARIOS
>>> student_uid = [1,2,3]
>>> students = ['Juan','Jose','Larsen']
>>> students_with_uid = {uid:student for uid, student in zip(student_uid, students)}
>>> students_with_uid
{1: 'Juan', 2: 'Jose', 3: 'Larsen'}


#SETS
>>> import random
>>> random_numbers = []
>>> for i in range(10):
...     random_numbers.append(random.randint(1,3))
>>> random_numbers
[3, 2, 2, 3, 1, 2, 2, 3, 2, 2]
>>> non_repeated = {number for number in random_numbers}
>>> non_repeated
{1, 2, 3}

```

## Búsqueda Binaria.

Uno de los conceptos más importantes que debes entender en tu carrera dentro de la programación son los algoritmos. No son más que una secuencia de instrucciones para resolver un problema específico.

Búsqueda binaria lo único que hace es tratar de encontrar un resultado en una lista ordenada de tal manera que podamos razonar. Si tenemos un elemento mayor que otro, podemos simplemente usar la mitad de la lista cada vez.

```python
import random

def binary_search(data,target, low, high):
    if low > high:
        return False

    mid = (low + high) // 2

    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data,target, low, mid-1)
    else:
        return binary_search(data, target, mid+1, high)


if __name__ == '__main__':
    data = [random.randint(0,100) for i in range(10)]
    data.sort()
    print(data)
    target = int(input('What number would you like to find?'))
    found = binary_search(data, target,0, len(data)-1)
    print(found)
```

## Manipulación de archivos en Python 3

En esta clase aprenderás a persistir datos en python, para esto aprenderás a utilizar la función Open, y la función close, una vez tengas claro eso, podrás comenzar a manipular tus archivos, en este caso utilizaremos un CSV que es un estándar de archivos separados por comas.

Para la manipulación de archivos existen dos **readers** y dos **writers**.

- **csv.render** y **csv.writer** nos permiten manipular los valores a través de listas que representan filas.
  - Solo se puede acceder por índice a los valores.

- **csv.DicReader** y **csv.DictWriter** nos permiten manipular los valores a través de diccionarios que representan filas.
  - Se puede acceder a través de llaves a los valores.

