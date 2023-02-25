from graphviz import render

class GrafoPeliculas:
    
    def crear_grafoPeliculas(self, paraGrafoEnv):
        #paraGrafo y paragrafoSN
        # =[
        #   [Nom.Act, Peli, year, genero, Peli1, year1, genero1],
        #   [Nom.Act2, Peli2, year2, genero2],
        #    ...]
        #enviar[paragrafoSN(0), paraGrafo(1)]
        
        paraGrafoSN = paraGrafoEnv[0]
        paraGrafo = paraGrafoEnv[1]
        
        nombreImagenSalida="grafos/ActorPeliculas.dot"
        
        EscribirA = open(nombreImagenSalida,'w')
        EscribirA.write('digraph peliculas { \n')
        EscribirA.write('rankdir=LR \n')
        
        
#----------NODOS para las peliculas----------------------        
        yaCreado=[] #alamcena el nombre de las peliculas ya agregadas al diseno
        # tablas
        i=1
        j=0
        while j < len(paraGrafo):
            if paraGrafoSN[j][i] not in yaCreado:
                NomNodoP = paraGrafoSN[j][i]
                
                yaCreado.append(NomNodoP)
                
                if ":" in NomNodoP or "." in NomNodoP:
                    NomNodoP=NomNodoP.replace(":","")
                    NomNodoP=NomNodoP.replace(".","")
                
                
                EscribirA.write(''+NomNodoP+' [shape=none, margin=0, label=<\n')
                EscribirA.write('<table border="0" cellborder="1">\n')
                EscribirA.write('<tr>\n')
                EscribirA.write('<td colspan="2" bgcolor="aquamarine">'+paraGrafo[j][i]+'</td>\n')
                EscribirA.write('</tr>\n')
                EscribirA.write('<tr>\n')
                EscribirA.write('<td>'+paraGrafoSN[j][i+1]+'</td>\n')
                EscribirA.write('<td>'+paraGrafoSN[j][i+2]+'</td>\n')
                EscribirA.write('</tr>\n')
                EscribirA.write('</table>>];\n')
            
            i+=3
            if i >= len(paraGrafo[j]):
                j+=1
                i=1
           
#----------NODOS para los actores-----------------------
        j=0
        while j < len(paraGrafo):
            
            NomNodoAct = paraGrafoSN[j][0]
            NomNodoAct = NomNodoAct.replace(".","")
            
            EscribirA.write(''+NomNodoAct+' [shape=none, margin=0, label=<\n')    
            EscribirA.write('<table border="0" cellborder="1">\n')
            EscribirA.write('<tr>\n')
            EscribirA.write('<td colspan="2" bgcolor="chartreuse">'+paraGrafo[j][0]+'</td>\n')
            EscribirA.write('</tr>\n')
            EscribirA.write('</table>>];\n')
            j+=1
#----------Direccionamiento de los NODOS----------------
        
        j=0
        c=1
        while j < len(paraGrafo):
            for peli in yaCreado:
                if peli in paraGrafoSN[j]:
                    
                    if ":" in peli or "." in peli:
                        peli=peli.replace(".","")
                        peli=peli.replace(":","")
                    
                    NomNodoAct=paraGrafoSN[j][0]
                    if "." in NomNodoAct:
                        NomNodoAct=NomNodoAct.replace(".","")
                    
                    EscribirA.write(peli+'->'+NomNodoAct+';\n')
                    c+=3
                    
                if c >= len(paraGrafoSN[j]):
                    c=1
                    j+=1
                    break
            

#-------------------------------------------------------    
        EscribirA.write('}\n')
        EscribirA.close()
        
        render('dot','png',nombreImagenSalida)
    #EscribirA.write('') 
    #dot -Tpng prueba.dot -o salida1.png