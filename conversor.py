pesos_que_da_usuario = input("¿Cuántos pesos mexicanos tienes?: ")
pesos_que_da_usuario = float(pesos_que_da_usuario)
valor_dolar_en_pesos = 21.77
dolares_que_tiene_usuario = pesos_que_da_usuario / valor_dolar_en_pesos
dolares_que_tiene_usuario = round(dolares_que_tiene_usuario, 2)
dolares_que_tiene_usuario = str(dolares_que_tiene_usuario)
print("Tienes $" + dolares_que_tiene_usuario + " dólares")
