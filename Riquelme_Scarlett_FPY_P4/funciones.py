from os import system
from msvcrt import getch

productos=[]
def menu():
    menu="""MENU REGISTRO DE PRODUCTO
         ===========================================
        
            1.- Registrar producto
            2.- Listar productos con stock
            3.- Eliminar producto por código
            4.- Salir
         ============================================
  
         """
    while True:
        print(">>>Presione tecla para continuar<<<")
        system("cls")
        print(menu)
        opc=input("Ingrese opcion del 1 al 4: ")
        
        if opc=="1":
            registrar_producto()
        elif opc=="2":
            listar_producto()
        elif opc=="3":
            eliminar_producto()
        elif opc=="4":
            print("salio del sistema")
            break
        else:
            print("Error de opcion")
            
        
        getch()     

        

def registrar_producto():
    
    print("--Agregar producto--")
    codigo=input("Ingrese codigo del producto: ")
    nombre=input("Ingrese nombre del producto: ")
    stock=input("Ingrese stock del producto: ")
    precio=input("Indique precio del producto $:")
    producto={
        "codigo"==codigo,
        "nombre"==nombre,
        "stock"==stock,
        "precio"==precio
    }
    productos.append(producto)
    print("Producto agregado con exito!!")

def listar_producto():
    print("--Buscar producto--")
    codigo = input("Ingrese codigo a buscar")
    for x in productos:
        if codigo==x["codigo"]:
            x=["nombre"],["codigo"],["stock"],["precio"]
            
            print("producto encontrado")
            return x
      
       

def eliminar_producto():
    print("--Eliminar producto--")
    
   
    codigo = input("Ingrese codigo a eliminar:")  
    for x in productos:
        if codigo==x["codigo"]:
            productos.remove(x)
            return
        print("producto eliminado con exito")
    
    



    