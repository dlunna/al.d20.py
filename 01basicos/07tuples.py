x = (1,2,3,4)
print(x)
print(type(x))

months = ('enero', 'febrero', 'marzo')
print(months)

#Para crear una tupla
y = tuple(('a','b','c'))
print(y)

#Metodos disponibles en la tupla
print(dir(x))

#Entero vs tupla
print("Entero", type((1)))
print("Tupla", type((1,)))

#Imprimir una posicion en la tupla
print("imprime valor de x en 0 -->", x[0])


# Borrando la tupla
del x