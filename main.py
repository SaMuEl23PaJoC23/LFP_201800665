from clase_menu import menus
from clase_funcion import funciones
cargar=funciones()
#Datos Programador
print("""
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
---- Lenguajes Formales y de Programacion ----- 
---------------- Seccion A- -------------------     
---------------- 201800665 --------------------
------- Samuel Alejandro Pajoc Raymundo -------
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
""")
input()

opcion = 0
ruta = ""
peliculas=[]
Flag=False

while opcion != 5:
    try:
        menus.menu_principal()
        opcion = int(input('Ingrese opcion: '))
        print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
        
        if opcion == 1:
            ruta=cargar.SeleccionarArchivo()
            if ruta != None:
                peliculas = cargar.ExtraerInfo(ruta)
                Flag=True
                print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
            else:
                print('\n>>> Debe seleccionar un archivo <<<\n')
                Flag=False
            
        elif opcion == 2:
            if Flag== False:
                print('\n>>> Primero debe seleccionar un archivo<<<\n')
            else:
                opcion2 = ""
                while opcion2 != 'c':
                    menus.menu_gestionar()
                    opcion2 = str(input('Ingrese opcion: '))
                    opcion2 = opcion2.lower()
                    print('*********************************************')
                    
                    if opcion2 == 'a':
                        cargar.MostrarPeliculas(peliculas)
                        input('Presiona enter para CONTINUAR...')
                        
                    elif opcion2 == 'b':
                        print('Opcion B')
                        
        
        elif opcion == 3:
            print('OPCION 3')
        
        elif opcion == 4:
            print('OPCION 4')
            
        
        elif opcion < 1 or opcion > 5:
            print('\n>>> Utilizar solo numeros entre 1 y 5 <<<')
    except:
        print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
        print('\n>>>  !!Ingresar Solo Numeros!!  <<<\n')
    
print('Salio....')