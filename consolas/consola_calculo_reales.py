from calculadora_monedaextranjera import convertir_a_reales
def main():
    peso = int(input("Ingrese la cantidad de Pesos que desea convertir a Reales: "))
    real = convertir_a_reales(peso)
    print(f"Cantidad de Pesos ingresada: ${peso}")
    print(f"Valor en Reales: R${real}")

main()