from funciones import *

menu="""MENÚ OPCIONES
1. Registrar paciente
2. Buscar paciente
3. Eliminar paciente
4. Salir"""

while True:
    system('cls')
    print(menu)
    opc = input("Ingrese opción(1-4): ")
    system('cls')
    if opc=="1":
        registrar_paciente()
    elif opc=="2":
        buscar_paciente()
    elif opc=="3":
        eliminar_paciente()
    elif opc=="4":
        print("Adios!")
        break
    else:
        print("Opción incorrecta!")
    print("\n...presione una teclar para continuar...")
    getch()