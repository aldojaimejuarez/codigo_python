# menu = """ 
# Bienvenido al conversor de monedas 💰

# 1.- Pesos mexicanos
# 2.- Pesos argentinos
# 3.- Pesos colombianos

# Elige una opción: """

# opcion = int(input(menu))

# if opcion == 1:
#     pesos= input("¿Cuántos pesos mexicanos tienes?: ")
#     pesos = float(pesos)
#     valor_dolar = 21.77
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $" + dolares + " dólares")
# elif opcion == 2:
#     pesos= input("¿Cuántos pesos argentinos tienes?: ")
#     pesos = float(pesos)
#     valor_dolar = 65
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $" + dolares + " dólares")
# elif opcion == 3:
#     pesos= input("¿Cuántos pesos colombianos tienes?: ")
#     pesos = float(pesos)
#     valor_dolar = 3875
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $" + dolares + " dólares")
# else:
#     print("Ingresa una opción correcta por favor")




def cambios(nacionalidad, valor_dolar):
    pesos= input("¿Cuántos pesos " +  nacionalidad  + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
    return valor_dolar


menu = """ 
Bienvenido al conversor de monedas 💰

1.- Pesos mexicanos
2.- Pesos argentinos
3.- Pesos colombianos

Elige una opción: """



opcion = int(input(menu))

if opcion == 1:
    cambios("mexicanos", 21.77)
elif opcion == 2:
    cambios("argentinos", 65)
elif opcion == 3:
    cambios("colombianos", 3875)
else:
    print("Ingresa una opción correcta por favor")