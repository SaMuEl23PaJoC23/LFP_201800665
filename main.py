from archivo_menus import menus

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

while opcion != 5:
    try:
        menus.menu_principal()
        opcion = int(input('Ingrese opcion: '))
        print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
        if opcion < 1 or opcion > 5:
            print('\n>>> Utilizar solo numeros entre 1 y 5 <<<')
    except:
        print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
        print('\n>>>  !!Ingresar Solo Numeros!!  <<<')
    
print('Salio....')