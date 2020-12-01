# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:44:15 2020

@author: Cristian
"""

tablero=[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ]

print(tablero)

def reinas(tablero):
    listaindices=[]
    for n, fila in enumerate(tablero):
        print("------------")
        

        for x,celda in enumerate(fila):
            if tablero[n][x] == 0:
                tablero[n][x] = 1
                #dar valores de 2
                print()
                for t in tablero:
                    print (t)
                
                for column, celdacel in enumerate(fila):
                    if tablero[n][column] == 0:
                       tablero[n][column]=2 
                for ar, arrow in enumerate(tablero):
                    if tablero[ar][x]==0:
                       tablero[ar][x]=2 
                filawhile=n
                columnawhile=x
                print()
                for t in tablero:
                    print (t)
                ####diagonal inferior derecha
                for i in range(0, 3, 1):
                    if columnawhile==3 or filawhile==3 or filawhile<0 or columnawhile<0:
                        break

                    filawhile=filawhile+1
                    columnawhile=columnawhile+1
                    j=filawhile,columnawhile
                    listaindices.append(j)
                print()
                for t in tablero:
                    print (t)
                
                print(listaindices)
                for li in listaindices:
                    tablero[li[0]][li[1]]=2
                print(listaindices)
                listaindices=[]
                print()
                for t in tablero:
                    print (t)
                fw=n
                cw=x
                
                ####diagonal inferior derecha
                for i in range(0, 3, 1):
                    if cw<0 or fw<0 or cw==3 or fw==3:
                        break
                    fw=fw+1
                    cw=cw-1
                    m=fw,cw
                    listaindices.append(m)
                print(listaindices,"sentido contrario")
                for li in listaindices:
                    tablero[li[0]][li[1]]=2
                print(listaindices,"guitarra")
                listaindices=[]
                
                print()
                for t in tablero:
                    print (t)
                
                ####diagonal inferior derecha----------------------
                fw=n
                cw=x
                for i in range(0, 3, 1):
                    if cw==0 or fw==0 or cw==3 or fw==3:
                        break
                    fw=fw-1
                    cw=cw+1
                    m=fw,cw
                    listaindices.append(m)
                print(listaindices,"sentido contrario")
                for li in listaindices:
                    tablero[li[0]][li[1]]=2
                listaindices=[]
                print()
                for t in tablero:
                    print (t)
                                
                ####diagonal inferior derecha----------------------
                fw=n
                cw=x
                for i in range(0, 3, 1):
                    if cw==0 or fw==0 or cw==3 or fw==3:
                        break
                    fw=fw-1
                    cw=cw-1
                    m=fw,cw
                    listaindices.append(m)
                print(listaindices,"sentido contrario")
                for li in listaindices:
                    tablero[li[0]][li[1]]=2
                listaindices=[]
                
                print()
                for t in tablero:
                    print (t)
    
                    
    print(filawhile,",-----------",columnawhile)
    terminar=0
    for t in tablero:
        for r in t:
         if r==1:
             terminar=terminar+1
    print(terminar)
    for t in tablero:
            print (t)
    
reinas(tablero)