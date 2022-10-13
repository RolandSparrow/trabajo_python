#ESTRUCTURA DE DATOS

#LISTAS:

#Puedes acceder a una posición usando el nombre de la variable y corchetes "[]" indicando en su interior el índice que quieres obtener.
#Las posiciones de las listas arrancan enumeradas desde cero, así la primera posición se accede como [0] y la última sería el tamaño total menos 1
#Se pueden usar índices negativos, así accediendo a los elementos de la lista contando desde atrás. Así un modo sencillo de obtener el último elemento es con [-1]
#Si accedes a un índice que no existe, el programa fallará.

#métodos de una lista:

#Estructuras de datos

#Ejercicio 1
number = [1,2,3,4,5,6,3,5,7,1]
number.append('texto')
print(number)
#Ejercicio 2

# crear lista
prime_numberss = [2, 3, 5]

# crear otra lista

numbers = [1, 4]
# agregar lista prime_numbers a numbers

numbers.extend(prime_numberss)

print('extend', numbers)

#Ejercicio 3

number.insert(0,'0')
print(number)

#Ejercicio 4
animals = ['cat', 'dog', 'rabbit', 'guinea pig']
animals.remove('dog')
print(animals)

#Ejercicio 5
animals.pop()
print(animals)

#Ejercicio 6
animals.clear()
print(animals)

#Ejercicio 7
index = number.index(5)
print(index)

#Ejercicio 8
cont = number.count(5)
print(cont)

#Ejercicio 9
prime_numbers = [11, 3, 7, 5, 2]
prime_numbers.sort()
print(prime_numbers)

#Ejercicio 10
number.reverse()
print(number)

#Ejercicio 11
copy = prime_numbers.copy()
print('COPIADO:', copy)

# listas como pilas
# Los métodos de lista hacen que resulte muy fácil usar una lista como una pila, donde el último elemento añadido es el primer elemento retirado («último en entrar, primero en salir»). Para agregar un elemento a la cima de la pila, utiliza append(). Para retirar un elemento de la cima de la pila, emplea pop() sin un índice explícito.

pila = [1,2,4]
pila.append(8)
pila.append(9)
print(pila)

# Listas como colas
# También es posible utilizar una lista como una cadena, donde el primer elemento agregado es el primer elemento eliminado (“antes de, antes de”); sin embargo, los nombres no funcionan para este propósito. Sumar y restar desde el final de la lista es rápido, pero sumar o restar desde el principio de la lista es lento (porque cada elemento debe ser reemplazado por otro). Para crear una cola, use collections.deque, que está diseñado para agregarse y eliminarse rápidamente en ambos lados.


from collections import deque
cola = deque(['Hector','Juan','Miguel'])
cola.append('Maria')
cola.append('Arnaldo')
print(cola.popleft())
persona = cola.popleft()
print(persona)
print(cola)

# Comprensión de listas
# Comprender los guiones proporciona un atajo para ocasionar conversaciones. A menudo se usa para crear nuevos registros donde cada elemento es el resultado de una operación diferente aplicada a cada miembro de una secuencia o repetición, o para crear una secuencia de estos elementos para satisfacer la condición dada.

lista = []
for numero in range(0,11):
    lista.append(numero**2)

pares = []   
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

#Listas por comprensión anidadas
# El primer tipo de comprensión narrativa puede ser cualquier afirmación abstracta, incluida alguna comprensión narrativa.

matriz = [[0, 1, 2, 3, 4],
        [0, 1, 2, 3, 4],
        [0, 1, 2, 3, 4],
        [0, 1, 2, 3, 4],
        [0, 1, 2, 3, 4]]
matrix = [] 

for i in range(5): 
    
    
    matrix.append([]) 
    
    for j in range(5): 
        matrix[i].append(j) 
    
print(matrix) 

# La instrucción de1
# Hay una manera de eliminar un elemento de una lista por su índice en lugar de su valor:
# Declaración Esto es diferente del método pop(), que devuelve un valor. La declaración del también se puede utilizar para eliminar elementos de una lista o para eliminar una lista completa.

a = [-2, 1, 77.5, 888, 888, 5123.9]
del a[0]
print(a)
del a[2:4]
print(a)

# Tuplas y secuencias
# Hemos visto que las matrices y las cadenas comparten propiedades, como las operaciones de indexación y partición. Estos son dos ejemplos de tipos de datos. Dado que Python es un lenguaje cruzado, se puede agregar cierta información de cadena. 

x = ("manzana", "plátano", "cereza")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

lista_enteros = [10, 5, 1, 130, -2]
print(f'El tipo de {lista_enteros} es {type(lista_enteros)}.')
x = lista_enteros[0]
y = lista_enteros[1]
z = lista_enteros[4]
print(x, y, z)

# Conjuntos
# Python también incluye un tipo de datos para matrices. Un conjunto es una colección aleatoria sin elementos repetidos. Su uso principal consiste en verificar miembros y eliminar duplicados. Los conjuntos también admiten operaciones matemáticas como unión, intersección, diferencia y diferencia simétrica.

group_a = set(['a', 'b', 'c', 'd'])
group_b = {'f', 'G', 'h', 'i'}
group_c = {'j', 'k', 'l', 'm'}
all_students = group_a.union(group_b).union(group_c)
print(all_students)

# Diccionarios
# Otro cualquiera de apunte herramienta incluido en Python es el diccionario. Los diccionarios se encuentran a veces en otros lenguajes como «autobiografía asociativa» o «arreglos asociativos». A discrepancia de las secuencias, que se indexan mediante una jerarquía numérica, los diccionarios se indexan con claves, que pueden ser cualquier cualquiera inmutable; las esposas y números siempre pueden ser claves. Las tuplas pueden estar de moda como claves si nada más contienen esposas, números o tuplas; si una tupla contiene cualquier impresión mutable directa o indirectamente, no puede estar de moda como clave. No puedes disfrutar listas como claves, ya que las listas pueden variar usando paga por índice, paga por sección, o métodos como append() y extend().
import random
clientes = ["Alex","Rick","jorge","Miguel","Luis","valentina","sofia"]
diccionario_descuentos = {cliente:random.randint(1,100) for cliente in clientes}
print(diccionario_descuentos)
