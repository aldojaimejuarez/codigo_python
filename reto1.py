dolares = input("¿Cuántos dólares estadounidenses tienes?: ")
dolares = float(dolares)
valor_pesos = 0.0459347726
pesos = dolares / valor_pesos
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " MXN")