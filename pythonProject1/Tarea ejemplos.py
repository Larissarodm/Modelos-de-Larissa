# Tarea: ejemplo de cada método visto en clase
# Lista de cosas que disfruto:
list = ["café", "libros", "hamburguesa","elote","animales" ]
print(list)
#para agregar un elemento a mi lista
list.append("cannabis")
print(list)
#Para añadir elementos de otra lista al final de mi lista existente
lista2 = ["Silvana Estrada", "techno", "18"]
print(lista2)
list.extend(lista2)
print(list)
#Para insertar un item en una posición particular
list.insert(0, "verde")
print(list)
#Para remover un elemento de mi lista
list.remove("elote")
print(list)
#Para quitar un item de posición específica
item_eliminado= list.pop(1)
print(item_eliminado)
print(list)
#Para remover todos los items de la lista
list.clear()
print(list)
#Para encontrar la posición de elemento x en la lista.
list = ["verde", "libros", "cannabis", "animales", "hamburguesa", "Silvana Estrada"]
print(list)
indice_cannabis = list.index("cannabis",0)
print(indice_cannabis)
#Para contar el número de veces que aparece x elemento en la lista
conteo_animales = list.count("animales")
print(conteo_animales)
#Para ordenar los elementos de una lista de manera ordenada.
print(list)
list.sort(key=len)
print(list)
#Para invertir el orden de los elementos de una lista.
list.reverse()
print(list)
#Para crear una copia de una lista
copia_list = list.copy()
print(copia_list)
copia_list.append('elote')
print(copia_list)
print(list, copia_list)