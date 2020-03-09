product = {
    "name":"book",
    "quan":3,
    "price":4.25,
}

person ={
    "name":"zoy",
    "first_name":"mol",
    "age":39,
}

print(type(product))
print(dir(product))
print(product)

#Obtener los indices o llaves del diccionario
print(product.keys())
print(product.values())
print(product.items())

tienda = [
    {"name":"chair", "price":150},
    {"name":"soap", "price":10},
    {'fifi':'8'}
]

print(tienda)