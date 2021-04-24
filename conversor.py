menu = """
Bienvenido al conversor de monedas ✔

1 - Pesos Colombianos
2 - Pesos Argentino
3 - Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿Cuántos pesos Colombiano tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 2:
    pesos = input("¿Cuántos pesos Argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 3:
    pesos = input("¿Cuántos pesos Mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
else: 
    print("Ingresa una opcion correcta")




