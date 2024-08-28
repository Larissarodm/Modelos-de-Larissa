#Ejemplo de cada uno de los métodos de diccionarios

diccionario1 = {'llave1': 'menta', 'llave2': 'romero', 'llave3': 'tila', 'llave4': 'lavanda'}
print(diccionario1)

#pop
valor = diccionario1.pop('llave3')
print('valor eliminado', valor)
print('diccionario después de pop', diccionario1)
    #valor eliminado tila
    #diccionario después de pop {'llave1': 'menta', 'llave2': 'romero', 'llave4': 'lavanda'}

#get
valor_llave = diccionario1.get('llave1')
print('valor de la llave1', valor_llave)
    #valor de la llave1 menta

#copy
copia_diccionario = diccionario1.copy()
print('copia de diccionario', copia_diccionario)
    #copia de diccionario {'llave1': 'menta', 'llave2': 'romero', 'llave4': 'lavanda'}

#keys
claves = diccionario1.keys()
print('claves del diccionario', claves)
    #claves del diccionario dict_keys(['llave1', 'llave2', 'llave4'])

#items
items = diccionario1.items()
print('items del diccionario', items)
    #items del diccionario dict_items([('llave1', 'menta'), ('llave2', 'romero'), ('llave4', 'lavanda')])

#fromkeys
nuevas_claves = ['w', 'p', 'ñ']
nuevo_diccionario = dict.fromkeys(nuevas_claves, 0)
print('nuevo diccionario con nuevas claves', nuevo_diccionario)
    #nuevo diccionario con nuevas claves {'w': 0, 'p': 0, 'ñ': 0}

#popitem
ultimo_elemento = diccionario1.popitem()
print('ultimo elemento del diccionario', ultimo_elemento)
    #ultimo elemento del diccionario ('llave4', 'lavanda')

#setdefault
valor_llave6 = diccionario1.setdefault('llave6', 4)
print('valor de la llave6', valor_llave6)
    #valor de la llave6 4

#update
diccionario2 = {'a': 1, 'b': 2, 'c': 3}
diccionario1.update(diccionario2)
print('diccionario ya actualizado', diccionario1)
    #diccionario ya actualizado {'llave1': 'menta', 'llave2': 'romero', 'llave6': 4, 'a': 1, 'b': 2, 'c': 3}

#values
valores = diccionario1.values()
print("Valores del diccionario:", valores)
    #Valores del diccionario: dict_values(['menta', 'romero', 4, 1, 2, 3])

#clear
diccionario1.clear()
print('diccionario vacío', diccionario1)
    #diccionario vacío {}
