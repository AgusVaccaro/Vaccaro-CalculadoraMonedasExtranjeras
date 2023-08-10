from calculadora_monedaextranjera import convertir_a_dolar
def main():
    peso = int(input("Ingrese la cantidad de Pesos que desea convertir a Dolar: "))
    dolar = convertir_a_dolar(peso)
    print(f"Cantidad de Pesos ingresada: ${peso}")
    print(f"Valor en Dólares: USD${dolar}")

main()