x = 40

if (x < 40):
    print("Aun")
else:
    print("Ya no")

color = "blue"
if (color == "pink"):
    print("Es color rosa")
elif (color == "black"):
    print("Es color negro")
else:
    print("Otro color")

x = 54
if x >= 10 & x <= 20:
    print('Esta del 10 al 20')
else:
    print('No esta del 10 al 20')


if x >= 10 and x <= 20:
    print('AND: Esta del 10 al 20')
else:
    print('AND: No esta del 10 al 20')



y = 54
if y <= 10 or y >= 20:
    print('YY: Esta del 10 al 20')
else:
    print('YY: No esta del 10 al 20')

# Reverse the result, returns False if the result is true
if not(x and y):
    print('not: no son iguales')
else:
    print('not: si son iguales')
