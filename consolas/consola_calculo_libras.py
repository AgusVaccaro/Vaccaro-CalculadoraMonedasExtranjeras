from calculadora_monedaextranjera import convertir_a_libras
def main():
    peso = int(input("Ingrese la cantidad de Pesos que desea convertir a Libras Esterlinas: "))
    libras = convertir_a_libras(peso)
    print(f"Cantidad de Pesos ingresada: ${peso}")
    print(f"Valor en Libras Esterlinas: £{libras}")

main()