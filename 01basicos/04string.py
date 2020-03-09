myStr = "Hellow, world, this is me"

#Nos da la ayuda del tipo de datos
dir(myStr)
print(dir(myStr))

#Utiliza el metodo UPPER
print(myStr.upper())
print(myStr.title())
print(myStr.capitalize())
print(myStr.split())
print(myStr.swapcase())
#tamaño de la cadena
print(myStr.__len__())
print(len(myStr))
print(myStr.replace("world", "fix"))
print(myStr.count('l'))
#Ver si empieza con H
print(myStr.startswith('H'))
print(myStr.endswith('d'))

#separar por caracter
print(myStr.split(','))
#Encontrar un caracter
print(myStr.find('o'))

#Que tipo es
print(myStr.isalpha())

#Un caracter en el vector
print(myStr[4])
#Imprime el ultimo caracter
print(myStr[-1])

#Concatenar
print("-->" + myStr)
#Poner dos
print("-->" , myStr)

#Con formato
print(f"--> {myStr}")
print(">>> {0}".format(myStr))