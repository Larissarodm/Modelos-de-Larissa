#Tuplas: se usan () y se parados por comas y con las comillas.
tupla = (3,2, 'ola')
print(tupla)

#cuando tenemos una tupla con un elemento

#slicing
tupla =(3,6,'ola', 'oso', 'pulpo', [9, 8])
print(tupla)
print('tupla:', tupla)
print('aplicando slicing:', tupla[4])
print('aplicando slicing con números negativos:', tupla[-4:-1])

#Mutabilidad
#las tuplas no tienen la capacidad de pider reemplazar valores que ya están definidos

#suma de tuplas
tupla1, tupla2 = (1,2,3), ('limonada', 'piña colada', 'almohada')
print('suma de tuplas:', tupla1 + tupla2)
print('aplicando la función len:', len(tupla1+tupla2))
print('multiplicando tuplas por un entero:', tupla1*4)

#Convertir tuplas a listas
print('convirtiendo tupla a lista:', list(tupla1), 'tiene tipo:', type(list(tupla1)))

#Convertir lista a tupla
print('convirtiendo lista a tupla:', tuple(['verde', 'camarón']), 'tiene tipo:', type(tuple(['verde', 'camarón'])))

#RANGOSSSS
#La función range retorna una sucesión de números en un rango dado, range(start, stop, step)
rango1 = range(5)
print(rango1)
print('ejemplo de rango:', rango1, 'rango1 es de tipo:', type(rango1))

#conversión de range a lista
print('convirtiendo el rango a lista:', list(rango1))

rango2 = range(3, 102, 3)
print('convirtiendo el rango a lista:', list(rango2))
#el incio, el final y, en este caso, irá de 3 en 3, o sea el paso
print('aplicando slicing al rango:', rango2[0])


#TIPOS DE DATOS BOLEANOS
#los tipos de datos boleanos representan uno de dos posibles valores: True o False
valor1 = True
valor2 = False
print('tipos de valores boleanos:', valor1, valor2)
print('usando type:', type(valor1), type(valor2))

print('usando and', valor1 and valor2)
print('usando or', valor1 or valor2)

#Conversiones a boleano
str() # convertir a cadena
bool() #convertir a boleano

print('entero a boleano', bool(0))
print('entero 1 a boleano', bool(1))
print('entero 5 a boleano', bool(5))
#todos los números que no sean 0 los convierte a boleano. Si son flotantes tmb!
print('entero -7.5 a boleano', bool(-7.5))

if (5+3-8*6):
    print('otra vez print')
else:
    print('ya ven')
#imprime la primera frase porque el número que sale no es cero!

#Conversión a boleano de strings
print("str '' a boleano", bool(''))
print("str '' a boleano", bool('a'))

#cadena nula:
print('lista vacía[] a boleano', bool([]))
print('lista vacía [] a boleano', bool([]))
print('diccionario vacío {} a boleano', bool({}))
#es falso porque estaban vacíos!

#DICCIONARIOS
#son un formato complejo para almacenar info en formatos key: value.
diccionario1 = dict()
print('ej de diccionario:', diccionario1, 'su tipo es:', type(diccionario1))

diccionario1 = {'llav1': 'lobo', 'llave2': -30, 34:'cosa', 'llave4': [2,3,4]}
print(diccionario1)

#slicing a diccionario
print(diccionario1['llave2'])
print(diccionario1['llave4'])

print('Usando len, el diccionario tiene:', len(diccionario1), 'elementos')

#LOS SETS O CONJUNTOS
#los conjuntos son una colección de valores no ordenados que no admiten duplicados, tmb están entre llaves y separados por comas
set1 = {8,9,10}
print(set1)
print(type(set1))

set1 = {'galleta', 'papitas', 'terror', 3, 3, 'galleta'}
print(set1)

#Asignadores
#En programación una variable se forma por un espacio en el sistema de almacenaje y un nombre simbólico asociado a ese espacio

variable = 'koala'
#internamente cuenta cada caracter de la cadena, y en base a cada uno reserva el tamaño de memoria en la compu
#cada tipo de dato tiene espacio de memoria diferente

variable1 = 5
print('la variable 1 =', variable1)

#hay dif tipos de operados de asignación:
#le sumamos 3.2
variable1 += 3.2
print('la variable 1 =', variable1)

#para restar
variable1 -= 17.2
print('la variable 1 =', variable1)

#para división de enteros
variable1 //= 2
print('la variable 1 =', variable1)

#para potenciación
variable1 **=6
print('la variable 1 =', variable1)

#CADENAS
cad1 = 'hola'
cad2 = 'ola'
print(cad1 + cad2)
#no se guarda el resultado solo lo muestro

cad1 += cad2
print(cad1)
#ya quedó guardado

#OPERADORES RELACIONALES -> para comparar
#Siempre el resultado será un boleano!!
# <,>, == (igual a), != (diferente de)

#OPERADORES LÓGICOS
#o, y y no
#not -> negación de la lógica

#el operador principal es "or". Del lado derecho hay boleano de carro, si es una cadena lo que sea entonces ésta es vdd
#Del lado iz tengo operador lógico and, 5<8 es true. Y el cero, que es FALSO. Vdd and FALSO = FALSO

#EXPRESIONES ANIDADAS
#Se solucionan usando las reglas de precedencia:
#
#1.- () prioridad
#2.- expresiones aritméticas
#3.- exp relacionales
#4.- exp lógicas

( 1 and 1) != True
#1=vdd
False

a=10
b=5

a*b - 2**b >= 20 and not (a % b) != 0
print(a*b - 2**b >= 20 and not (a % b) != 0 )

#CONTROLADORES DE FLUJO
#Estructura de control condicional, condiciones que pueden ser expresiones o exp anidadas y ver si son true or false
#si una o más condiciones se cumplen : evaluar qué acción se ejecutará

#sentencia if (si)
# permite div el flujo de un programa en dif caminos
#el if se ejecuta solo si la exp devuelve TRUE

if True:
    print('caso positivo')
if 'oración':
    print('oración')

var1, var2 =5,2
if var2/var1 < var1:
    print('segundo nivel de if')

#ejemplo de if else
condicional = (5 - 16) and False
if condicional:
    print('la condicional es vdd')
else:
    print('la condicional es falsa')

#ejemplo de if else
n = 15
if n %2 == 0:
    print('número par')
else:
    print('número impar')

#Tercer comando elif: si no se cumple condicional 1, entonces: si es vdd hace una cosa, si es falso
#verifica una segunda condicional
condicional = 32
if condicional < 10:
    print('condicional es pequeño')
elif condicional < 35:
    print('condicional es grande')
elif condicional <20:
    print('condicional no es tan pequeño')
else:
    print('no entró a ninguna elf')


#lo que es falso, no lo imprime.

#equivalencia con if else
condicional = 32
if condicional < 10:
    print('condicional es peque')
else:
    if condicional <20:
        print('condicional es grande')
    else:
        print('no entró a ninguna elf')

#COMANDO PASS
if condicional !=0:
    pass 