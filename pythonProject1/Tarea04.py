#
calif_1 = 10
print(calif_1)
calif_2 = 7
print(calif_2)
calif_3 = 4
print(calif_3)

primera_nota = 15
print(primera_nota)
segunda_nota = 35
print(segunda_nota)
tercera_nota = 50
print(tercera_nota)

final_1 = (10*calif_1)/primera_nota
print(final_1)
final_2 = (10*calif_2)/segunda_nota
print(final_2)
final_3 = (10*calif_3)/tercera_nota
print(final_3)

final_1+final_2+final_3
print('promedio:', final_1+final_2+final_3)

# Matriz original
matriz = [[1, 1, 1, 3], [2, 2, 2, 7], [3, 3, 3, 9], [4, 4, 4, 13]]

# Corrección de la matriz
for fila in matriz: #va a ser una variable temporal que representa cada sublista
    suma = fila[0] + fila[1] + fila[2] #suma los primeros tres y los compara con el cuarto valor
    if fila[3] != suma: # escoges el 3 porque es el 4 valor y ya te diste cuenta de que está mal
        print("Corrigiendo la fila {}: {} debería ser {}".format(fila, fila[3], suma))
        # si if es verdader dice que fila debe ser corregida
        fila[3] = suma
    else:
        print("La fila {} es correcta.".format(fila))

# Mostrar la matriz corregida
print("\nMatriz corregida:")
for fila in matriz:
    print(fila)