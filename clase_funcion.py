import easygui

class funciones:
    
    def SeleccionarArchivo(self):
        print("Esperando....")
        ruta= easygui.fileopenbox()
        return ruta
    
    
    def ExtraerInfo(self, rutaArchivo):
        DataArchivo = open(rutaArchivo)
        TextoArchivo = DataArchivo.readlines()
        DataArchivo.close()
        
        peliculas = []
        
        #0, NomPelicula
        #1, Lista-Actores
        #2, year
        #3, Genero
        indice = 0
        
        
        for linea in TextoArchivo:
            bandera=False
            i=0
            
            linea=linea.replace('\n','')
            pelicula = linea.split(';')
            actores=pelicula[1].split(',')
            pelicula[1]=actores
            
            if len(peliculas)>0:
                while bandera == False:
                    if pelicula[0].replace(" ","")==peliculas[i][0].replace(" ",""):
                        peliculas[i]=pelicula
                        bandera=True
                    i+=1
                    if i >= len(peliculas):
                        break
            
            if bandera==True:
                continue
            peliculas.append(pelicula)
            
        if len(peliculas)>0:
            print('\n>>> Carga completa !!\n')
        else:
            print('\n>>> Ocurrio un error, verificar documento de entrada <<<\n')
        
        input('Presiona enter para CONTINUAR...\n')
        return peliculas
    
 #-------------- Funciones GESTIONAR PELICULAS --------------
    def MostrarPeliculas(self, peliculas):
        print('===================================')
        i=1
        for peli in peliculas:    
            print('----- Pelicula No. '+str(i)+' -----')
            print(peli[0])
            
            print('\n---Actores---')
            j=1
            for actor in peli[1]:
                print(str(j)+"). "+actor)
                j+=1
                
            print('\nAño de estreno: ', peli[2])
            print('Genero: ', peli[3])
            i+=1
            print('===================================')
        
        
    def MostrarActores(self, peliculas):
        i=1
        opcionActor = 0
        banderaActor = False
        print('===================================')
        for peli in peliculas:    
            print('----- Pelicula No. '+str(i)+' -----')
            print(peli[0]+'\n')
            i+=1
        print('===================================')
        try:
            while banderaActor == False:
                opcionActor=int(input('Ingrese No. de pelicula: '))
                if opcionActor > 0 and opcionActor <= len(peliculas):
                    print('===================================')
                    print('pelicula: '+peliculas[opcionActor-1][0])
                    print('\n---Actores---')
                    j=1
                    for actor in peliculas[opcionActor-1][1]:
                        print(str(j)+"). "+actor)
                        j+=1    
                    return True
                else:
                    print('\n>>> ingrese un numero de PELICULA valido <<<\n')
                    input('Presiona enter para CONTINUAR...\n')
        except:
            print('\n>>>  !!Ingresar Solo Numeros!!  <<<\n')
            input('Presiona enter para CONTINUAR...\n')
            
        print('===================================')
        
#-------------- Funciones FILTRADO --------------
    def filtrado_actor(self, peliculas):
        actorB=input('Nombre del actor a buscar: ')
        print('===================================')
        actorB=actorB.replace(" ","")
        actorB=actorB.lower()
        
        
        pelisActor=[]
        for peli in peliculas:
            for actor in peli[1]:
                actor=actor.replace(" ","")
                actor=actor.lower()
                if actorB == actor:
                    pelisActor.append(peli[0])
                    break
                
        if pelisActor == []:
            print('\n>>> Actor no encontrado...\n')
            input('Presiona enter para CONTINUAR...\n')
        
        else:
            i=1
            print('======Este actor participo en:')
            for peli in pelisActor:
               print(str(i)+'). '+peli) 
               i+=1
            input('\nPresiona enter para CONTINUAR...\n')
                
        print('===================================')
    
    
    def filtrado_year(self, peliculas):
        try:
            yearB=int(input('Ingrese -year- a buscar: '))
            print('===================================')
            pelisYear=[]
            for peli in peliculas:
                if yearB == int(peli[2]):
                    auxpeli=[] 
                    #0, Nombre pelicula
                    #1, Genero pelicula
                    auxpeli.append(peli[0])
                    auxpeli.append(peli[3])
                    pelisYear.append(auxpeli)
                    
            if pelisYear == []:
                print('\n>>> No existe pelicula con ese -year-...\n')
                input('Presiona enter para CONTINUAR...\n')
            
            else:
                i=1
                print('====== Las peliculas encontradas son:')
                for peli in pelisYear:
                    print(str(i)+'). Pelicula:'+peli[0]+' - Genero: '+peli[1]) 
                    i+=1
                input('\nPresiona enter para CONTINUAR...\n')
                    
            print('===================================')
            
        except:
            print('\n>>>  !!Ingresar Solo Numeros!!  <<<\n')
            input('Presiona enter para CONTINUAR...\n')
            
            
    def filtrado_genero(self, peliculas):
        generoB=input('Ingrese genero a buscar: ')
        print('===================================')
        pelisGenero=[]
        generoB = generoB.replace(" ","")
        generoB = generoB.lower()
        
        for peli in peliculas:
            peli[3]=peli[3].replace(" ","")
            peli[3]=peli[3].lower()
            
            if generoB == peli[3]:
                pelisGenero.append(peli[0])
                    
                    
        if pelisGenero == []:
            print('\n>>> No existe pelicula con ese genero...\n')
            input('Presiona enter para CONTINUAR...\n')
            
        else:
            i=1
            print('====== Las peliculas encontradas son:')
            for peli in pelisGenero:
                print(str(i)+'). '+peli) 
                i+=1
            input('\nPresiona enter para CONTINUAR...\n')
                    
        print('===================================')
     
     
        
    def organizar(self, peliculas):
        actores=[] #Lista que contendra a todos los actores (No almacenara nombres repetidos)
        actoresAux=[] #Lista que contendra a todos los actores -MINUSCULA Y SIN ESPACIOS- (No almacenara nombres repetidos)
        peliculasAux=[]
        
        for peli in peliculas:
            aux=[]
            aux2=[]
            
            aux.append(peli[0]) #Almacena el nombre de la pelicula en curso
            aux.append(peli[2]) #Almacena el year de la pelicula en curso
            aux.append(peli[3]) #Almacena el genero de la pelicula en curso
            
            for act in peli[1]:
                actAux=act.replace(" ","")
                actAux=actAux.lower()
                aux2.append(actAux) #almacena el nombre de cada actor sin espacios y en minuscula
                #para crear lista copia de pelicula, nombre actores sin espacios
                
                #alamcena genero y year sin espacios
                
                
                if not actAux in actoresAux: #almacena el nombre de cada actor sin repetirse
                    actores.append(act) #nombre actor con espacios
                    actoresAux.append(actAux) #nombre actor SIN espacios
                    
            aux.append(aux2)
            peliculasAux.append(aux) #almacena: 0,pelicula -- 1,year -- 2,genero -- 3,Lista actores sin espacio y en minuscula
                    
        
        paraGrafo=[]
        i=0
        for actor in actoresAux:
            aux=[] # 0, Nombre actor    1, Lista de peliculas en las que participa [nom.peli, year, genero]
            aux.append(actores[i])
            
            for peli in peliculasAux:
                if actor in peli[3]: #Verifica si el actor ACTUAL(actor) se encuentra en la lista de actores de la pelicula a evaluar
                # si es verdadero, agreaga a: AUX, nom.Pelicula, year, genero
                    
                    aux.append(peli[0]) #Nom.pelicula
                    
                    year=peli[1].replace(" ","")
                    aux.append(year)    #year
                    
                    genero=peli[2].replace(" ","")
                    genero=genero.lower()
                    aux.append(genero)  #Genero
            i+=1
            paraGrafo.append(aux)
            
        """print("----Actores y peliculas----")
        for i in paraGrafo:
            print(i)"""
            
        
        
        paragrafoSN=[]
        for elemento in paraGrafo:
            aux=[]
            
            act=elemento[0].replace(" ","")
            act=act.lower()
            aux.append(act)
            
            i=1
            while i < len(elemento):
                NomPeli=elemento[i].replace(" ","")
                NomPeli=NomPeli.lower()
                aux.append(NomPeli)         #Nom. Pelicula   
                aux.append(elemento[i+1])   #year
                aux.append(elemento[i+2])   #Genero
                i+=3
            paragrafoSN.append(aux)
            
            
            
        """print("-----------SN---------------!!!!")
        print("----Actores y peliculas----")
        for i in paragrafoSN:
            print(i)"""
        
        enviar=[]
        
        #paraGrafo y paragrafoSN
        # =[
        #   [Nom.Act, Peli, year, genero, Peli1, year1, genero1],
        #   [Nom.Act2, Peli2, year2, genero2],
        #  ]
        #enviar[paragrafoSN(0), paraGrafo(1)]
        enviar.append(paragrafoSN)
        enviar.append(paraGrafo)
            
        return enviar