import json
from sys import exit
def profundidad(x,y):
    with open ("recorrido.json", "r") as read_file:
        data = json.load(read_file)
        grafo = data['nodos']
        
    siguiente=[]
    x=False

    while len(grafo)!=0:
        
        del siguiente[:]
        raiz=grafo[0][0]
        
        
        print(raiz," s1")
        
        if raiz == y:
            exit()
        

        
        contador=0;
        for nodo in  grafo:
            if raiz == nodo[0]:
                raiz = nodo[1]
                print(raiz, " cf1")
                siguiente.append(contador)
                if raiz == y:
                    exit()

            contador=contador+1;

        
        siguiente = sorted(siguiente, reverse=True)

        for sig in siguiente: 
            grafo.pop(sig)
            
        del siguiente[:]

        raiz=grafo[(len(grafo)-1)][1]
        
        print(raiz,"  s2")
        
        if raiz==y:
            exit()
        

        
        grafo2 = sorted(grafo, reverse=True)
        
        for nodo in grafo2:
            if raiz == nodo[1]:
                raiz = nodo[0]
                grafo.pop(grafo.index(nodo))
        
                
profundidad("10","5")
