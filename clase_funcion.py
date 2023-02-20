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
            linea=linea.replace('\n','')
            pelicula = linea.split(';')
            actores=pelicula[1].split(',')
            pelicula[1]=actores
            
            peliculas.append(pelicula)
            
        return peliculas
            
    def MostrarPeliculas(self, peliculas):
        print('===================================')
        i=0
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
        