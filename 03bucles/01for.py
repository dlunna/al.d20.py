foods = ['apples', 'bread', 'cheese', 'milk']

print(foods[0])
print(foods[1])

#Dentro del for
print("-----------")
print("Dentro del for")
print("-----------")

for food in foods:
    print(food)


#Dentro del for
print("-----------")
print("For Break")
print("-----------")

for food in foods:
    if food == 'cheese':
        print("Fin")
        break;

#Dentro del for
print("-----------")
print("For Continue")
print("-----------")

for food in foods:
    if food == 'cheese':
        print("Continua")
        continue
    print(food)


#Range
print("-----------")
print("ejemplo Range")
print("-----------")

for number in range(1,8):
    print(number)

#String
print("-----------")
print("Ejemplo String")
print("-----------")

for letter in "Hellow":
    print(letter)