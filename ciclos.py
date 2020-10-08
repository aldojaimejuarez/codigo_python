# def run():
#     LIMITE = 1000

#     contador = 0
#     potencia_2 = 2**contador
#     while potencia_2 < LIMITE:
#         print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
#         contador = contador + 1
#         potencia_2 = 2**contador


# if __name__ == '__main__':
#     run() 

def run():
# BREAK
    LIMITE = 12
    constante = 1
    contador = 0
    suma = 1 + contador

    while suma < LIMITE:
        print(str(contador) + " más " + str(constante) + " es igual a " + str(suma)) 
        contador = contador + 1
        suma = 1 + contador
        if suma == 5:
            break

# CONTINUE
    contador = 1
    print(contador)
    while contador < 10:
        contador += 1
        if contador == 5:
            continue
        print(contador)



if __name__ == '__main__':
    run()

# contador = 1
# print(contador)
# while contador < 10:
#     contador += 1
#     print(contador)