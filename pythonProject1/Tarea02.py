#Determinar si los tipos de dato range cumplen: mutabilidad, suma, producto por entero, slicing, convertirse en lista o tupla, y función len

rango1 =range(8,20,1)
print(rango1)

#mutabilidad
    #Los rangos son inmutables, para aplicar mutabilidad debo volerlo una lista primero.
rango1 = range(8, 20, 1)
lista_rango = list(rango1)
print(lista_rango)
lista_rango[5]=100
print(lista_rango)
    #aquí, ya en la posición 5 está ahora el número 100

#Suma
    #da error, debo convertir esto en listas
rango1 = range(8, 20, 1)
rango2 = range(6, 20, 3)
lista_sumada = list(rango1) + list(rango2)
print(lista_sumada)
    #[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 6, 9, 12, 15, 18]

#Slicing
rango3 = range(14, 500, 2)
print(rango3)
print('aplicando slicing:', rango3[16])
    #aplicando slicing: 46

#Convertir tupla (porque ya lo convertí a lista)
print('convirtiendo el rango a tupla:', tuple(rango1))
print('convirtiendo tupla a lista:', list(rango1))
lista1 = list(rango1)
print(lista1)

print('convirtiendo el rango a lista:', list(rango2))
lista2 = list(rango2)
print(lista2)

#Función len
print('aplicando la función len:', len(lista1 + lista2))
    #aplicando la función len: 17

#Producto por entero
    #da error, debo convertirlo en lista
lista1 = list(rango1)
print(lista1)
list_multiplicada = lista1 * 2
print(list_multiplicada)