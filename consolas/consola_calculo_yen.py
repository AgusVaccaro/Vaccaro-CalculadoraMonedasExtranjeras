from calculadora_monedaextranjera import convertir_a_yen
def main():
    peso = int(input("Ingrese la cantidad de Pesos que desea convertir a Yen: "))
    yen = convertir_a_yen(peso)
    print(f"Cantidad de Pesos ingresada: ${peso}")
    print(f"Valor en Yenes: ¥{yen}")

main()