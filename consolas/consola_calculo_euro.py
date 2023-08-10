from calculadora_monedaextranjera import convertir_a_euro
def main():
    peso = int(input("Ingrese la cantidad de Pesos que desea convertir a Euros: "))
    euro = convertir_a_euro(peso)
    print(f"Cantidad de Pesos ingresada: ${peso}")
    print(f"Valor en Euros: £{euro}")

main()