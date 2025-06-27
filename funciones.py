from os import system
from msvcrt import getch

pacientes = []

def registrar_paciente():
    print("REGISTRAR PACIENTE")
    rut = validar_rut()
    nombre = validar_nombre()
    sexo = validar_sexo()
    paciente = {
        "rut": rut,
        "nombre": nombre,
        "sexo": sexo
    }
    pacientes.append(paciente)
    print("Paciente registrado con éxito!")

def buscar_paciente():
    print("BUSCAR PACIENTE")
    rut = validar_rut()
    #para buscar o eliminar en una lista, debo recorrer la lista, con el rango del largo de la lista:
    for x in range(len(pacientes)):
        if rut==pacientes[x]["rut"]:
            print(f"Nombre: { pacientes[x]["nombre"] }, Sexo: { pacientes[x]["sexo"] }")
            return
    print("Paciente no encontrado!")

def eliminar_paciente():
    print("ELIMINAR PACIENTE")
    rut = validar_rut()
    for x in range(len(pacientes)):
        if rut==pacientes[x]["rut"]:
            pacientes.pop(x)
            print("Paciente eliminado con éxito!")
            return
    print("Paciente no encontrado!")

def listar_pacientes():
    print("LISTAR PACIENTES")
    for x in range(len(pacientes)):
        print(f"Rut: { pacientes[x]["rut"] }, Nombre: { pacientes[x]["nombre"] }, Sexo: { pacientes[x]["sexo"] }")

#FUNCIONES DE VALIDACIONES:
def validar_rut():
    while True:
        rut = input("Ingrese rut(12345678-9): ")
        partes = rut.split("-")
        if partes!=2:
            print("Formato de escritura incorrecto!")
        digitos,dv = partes
        if digitos.isdigit() and dv in('0','1','2','3','4','5','6','7','8','9','k','K'):
            return rut
        
def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ").strip().title()
        if len(nombre)>=3 and nombre.isalpha():
            return nombre
        print("Nombre incorrecto! muy corto!")

def validar_sexo():
    while True:
        sexo = input("Ingrese sexo(F-M): ").upper()
        if sexo in ('F','M','O'):
            return sexo
        print("Sexo mal escrito, es F o M!")