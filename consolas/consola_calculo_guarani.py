from calculadora_monedaextranjera import convertir_a_guarani
def main():
    peso = int(input("Ingrese la cantidad de Pesos que desea convertir a Guarani: "))
    guarani = convertir_a_guarani(peso)
    print(f"Cantidad de Pesos ingresada: ${peso}")
    print(f"Valor en Guaranies: ₲{guarani}")

main()