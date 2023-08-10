import os
import sys

def clear_screen(): 
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def display_menu():
    clear_screen()
    print("MENU")
    print("1. Ingrese 1 para la calculadora de Dolares.")
    print("2. Ingrese 2 para la calculadora de Euros.")
    print("3. Ingrese 3 para la calculadora de Reales.")
    print("4. Ingrese 4 para la calculadora de Libras.")
    print("5. Ingrese 5 para la calculadora de Yenes.")
    print("6. Ingrese 6 para la calculadora de Guaranies.")
    print("Ingrese 0 para salir.")

    choice = input("Ingrese el número de opción: ")
    return choice

def execute_file(filename): 
    clear_screen()
    print(f"Ejecutando {filename}...")
    print()
    folder = "consolas" 
    filepath = os.path.join(folder, filename)
    os.system(f"python {filepath}")
    input("Presione Enter para continuar...")

def menu():
    while True:
        choice = display_menu()

        if choice == '1':
            execute_file("consola_calculo_dolar.py")
        elif choice == '2':
            execute_file("consola_calculo_euro.py")
        elif choice == '3':
            execute_file("consola_calculo_reales.py")
        elif choice == '4':
            execute_file("consola_calculo_libras.py")
        elif choice == '5':
            execute_file("consola_calculo_yen.py")
        elif choice == '6':
            execute_file("consola_calculo_guarani.py")
        elif choice == '0':
            clear_screen()
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()
