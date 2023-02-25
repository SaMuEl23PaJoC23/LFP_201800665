from clase_menu import menus
from clase_funcion import funciones
from clase_grafo import GrafoPeliculas

import webbrowser as wb

cargar = funciones()
crearG = GrafoPeliculas()
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
correcto=False
paraGrafo=[]

while opcion != 5:
    try:    
        menus.menu_principal()
        opcion = int(input('Ingrese opcion: '))
        print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
#------------------------------------------------------------------------------        
        if opcion == 1:
            ruta=cargar.SeleccionarArchivo()
            if ruta != None:
                peliculas = cargar.ExtraerInfo(ruta)
                Flag=True
                print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
            else:
                print('\n>>> Debe seleccionar un archivo <<<\n')
                input('Presiona enter para CONTINUAR...\n')
                Flag=False
#------------------------------------------------------------------------------
        elif opcion == 2:
            if Flag== False:
                print('\n>>> Primero debe seleccionar un archivo<<<\n')
                input('Presiona enter para CONTINUAR...\n')
            else:
                opcion2 = ""
                while opcion2 != 'c':
                    menus.menu_gestionar()
                    opcion2 = str(input('Ingrese opcion: '))
                    opcion2 = opcion2.lower()
                    print('*********************************************')
                    
                    if opcion2 == 'a':
                        cargar.MostrarPeliculas(peliculas)
                        input('Presiona enter para CONTINUAR...\n')
                        
                    elif opcion2 == 'b':
                        correcto=cargar.MostrarActores(peliculas)
                        if correcto== True:
                            print('===================================')
                            input('Presiona enter para CONTINUAR...\n')
                    
                    elif opcion2 == 'c':
                        break
                    
                    else:
                        print('\n>>> Ingrese una opcion valida <<<\n')
                        input('Presiona enter para CONTINUAR...\n')
#------------------------------------------------------------------------------
        elif opcion == 3:
            if Flag== False:
                print('\n>>> Primero debe seleccionar un archivo<<<\n')
                input('Presiona enter para CONTINUAR...\n')
            else:
                opcion2 = ""
                while opcion2 != 'd':
                    menus.menu_filtrado()
                    opcion2 = str(input('Ingrese opcion: '))
                    opcion2 = opcion2.lower()
                    print('*********************************************')
                        
                    if opcion2 == 'a':
                        cargar.filtrado_actor(peliculas)
                        
                    elif opcion2 == 'b':
                        cargar.filtrado_year(peliculas)
                            
                    elif opcion2 == 'c':
                        cargar.filtrado_genero(peliculas)
                        
                    elif opcion2 == 'd':
                            break
                        
                    else:
                        print('\n>>> Ingrese una opcion valida <<<\n')
                        input('Presiona enter para CONTINUAR...\n')
#------------------------------------------------------------------------------ 
        elif opcion == 4:
            if Flag== False:
                print('\n>>> Primero debe seleccionar un archivo<<<\n')
                input('Presiona enter para CONTINUAR...\n')
            else:
                paraGrafo=cargar.organizar(peliculas)
                input('\nPresiona enter para CONTINUAR...\n')
                
                crearG.crear_grafoPeliculas(paraGrafo)
                print("\n >>> Se genero archivo .dot <<<\n")
                input('\nPresiona enter de nuevo y espere\n un momento para CONTINUAR...\n')
                wb.open_new(r'grafos\ActorPeliculas.dot.png')
            
#------------------------------------------------------------------------------   
        elif opcion < 1 or opcion > 5:
            print('\n>>> Utilizar solo numeros entre 1 y 5 <<<\n')
            input('Presiona enter para CONTINUAR...\n')

    except:
        print('\n>>>  !!Ingresar Solo Numeros!!  <<<\n')
        input('Presiona enter para CONTINUAR...\n')
    
print("""
---- (ha finalizado...) -----
-------- Gracias por --------
--- utilizar este sistema ---
""")