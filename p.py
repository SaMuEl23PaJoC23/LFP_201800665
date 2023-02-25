"""
peliculas2=[] #Unicamente se utiliza para la extraccion de: 0,NombrePelicula   1,ListaActores
        #0, pelicula
        #1, Lista actores
        for peli in peliculas:
            aux=[]
            aux.append(peli[0])
            aux.append(peli[1])
            peliculas2.append(aux)
            
        peliculas2Aux=[]
        for peli in peliculas2:
            aux=[] #lista: 0,NombrePelicula   1,ListaActores*
            aux2=[] # *ListaActores, sin espacios y en minusculas
            aux.append(peli[0])
            for act in peli[1]:
                act=act.replace(" ","")
                act=act.lower()
                aux2.append(act) 
            aux.append(aux2)
            peliculas2Aux.append(aux)
        
        i=0 #indice pelicula    
        j=0 #indice actor
        ParaGrafo=[] #Lista donde se alamcenaran todas las listas de actorPeliculas
        
#------------revisar de aqui en adelante-------------    
        bandera=False
        while bandera==False:
            if i >= len(peliculas2):
                bandera=True
                break
            
            actor=peliculas2[i][1][j]
            
            for elemento in ParaGrafo:
                if actor == elemento[0]:
                    j+=1
                    if j >= len(peliculas2[i][1]):
                        j=0
                        i=+1
                        
                    if i >= len(peliculas2):
                        bandera=True
                        break
                        
                    actor=peliculas2[i][1][j]
                    break
                    
            if bandera == True:
                break
            
            actorPeliculas=[actor] #Se crea una lista donde se almacenara el actor y las peliculas que interpreta    
            actor=actor.replace(" ","")
            actor=actor.lower()
            
            
            aux2=[]
            for peli in peliculas2Aux:
                if actor in peli[1]:
                    aux2.append(peli[0])
                    
            actorPeliculas.append(aux2)
            
            j+=1
            if j>= len(peliculas2[i][1]):
                j=0
                i=+1
            ParaGrafo.append(actorPeliculas)"""
            
lista=[1,2,3]   
i=0      
while i < len(lista):
    print("A")
    i+=1
    