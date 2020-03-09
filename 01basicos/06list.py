demo_list = [1, 'hello', 1.34, True, [1,2,3]]
colors = ['red','green','blue']

#Se tiene que enviar en una tupla,
#ya que list solo acepta 1 parametro
number_list = list((9,8,7,6))
print(type(number_list))

#Genera numeros de x a y
range(50, 69)
#Pon los numeros en una lista
list(range(50, 69))
#Asigna la lista a una variable
nuevo_rango = list(range(50, 69))
print (nuevo_rango)

#Que metodos puedo obtener de una lista
print(dir(colors))

#Cual es la longitud de la lista
print("Longtud de la lista -->", len(colors))

#Imprime una posicion especifica
print("Imprime vertor[1] -->", colors[1])

#Para saber si un elemento esta en la lista
print("???  -->", 'green' in colors)

#Cambiando valores de la lista
print(colors)
colors[2] = 'yellow'
print(colors)

#Agregando elementos a la lista
colors.append('violet')
print(colors)

#Agregando varios elementos
#Pero lo mismo solo recibe un parametro
#Una lista o una tupla
colors.extend(('black','orage'))
colors.extend(['purple','brown'])
print(colors)

#Insertando en una posicion especifica
colors.insert(1,'dark blue')
print(colors)
colors.insert(-1,'pink')
print(colors)
colors.insert(len(colors), 'ligt green')
print(colors)

#Para quitar el ultimo elemento de la lista
colors.pop()
print(colors)

#Para quitar uno en especifico
colors.remove('red')
print(colors)

#Para quitar uno por indice
colors.pop(1)
print(colors)


#Para ordenar alfabeticamente
colors.sort()
print("Ordenados alfabeticamente")
print(colors)
#Para ordenar alfabeticamente
colors.sort(reverse=True)
print("Ordenados inversa")
print(colors)


#conseguir un indice
print("Conseguir un indice")
print(colors.index('yellow'))

#Contar el numero de apariciones de un elemento
print("# de veces que aparece un elemento")
print(colors.count('yellow'))



#Limpiar por completo la lista
colors.clear()
print(colors)