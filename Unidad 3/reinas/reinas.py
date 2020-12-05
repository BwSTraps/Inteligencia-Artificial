# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:44:15 2020

@author: Cristian
"""

reina = 4
posicion =[]
llave = 0
tabldr =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
xls = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]


def reinacont(reina, tabldr, llave, xls):
    tbldr2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    m = 0
    print("# de reinas: "+str(reina))
    if reina == 1:
        return fin(tabldr)
    else: 
        for i in range(len(tabldr)):
            for j in range(len(tabldr[i])):
                if m == 0:
                  if xls[i][j] != 3:
                        if(tabldr[i][j] == 0):
                            if reina == 4:
                                xls[i][j] = 3
                            tabldr[i][j] = 1
                            m = m + 1
                            posicion.append([i,j])
        tabldr = arrg(tabldr,posicion)
        posicion.pop(0)
        for i in tabldr:
            if 0 in i:
               llave = 0
            else:
               llave = 1
        if llave == 1:
            print(llave)
            for i in tbldr2:
                print(i)
            reina=4
            llave=0
            return reinacont(reina,tbldr2,llave,xls)
        if llave == 0:
            print(llave)
            reina=reina-1
            return reinacont(reina,tabldr,llave,xls)
        
        

def arrg(tabldr,posicion):
    print("recorrido")
    a = posicion[0][0]
    b = posicion[0][1]
    j = range(len(tabldr))
    d = b
    c = a
    print(posicion)
    
    for i in range(len(tabldr)):
        for j in range(len(tabldr[i])):
            tabldr[a][j] = 2
            tabldr[i][b] = 2
    printf(tabldr)
    for t in range(len(tabldr)):
        d = d - 1
        c = c - 1
        if (d >= 0)and(c >=0):
            print("- -")
            tabldr[c][d] = 2
    d = b
    c = a
    printf(tabldr)
    for t in range(len(tabldr)):
        c = c + 1
        d = d + 1
        if (c <= j)and(d <= j):
            print("+ +")
            tabldr[c][d] = 2

    d = b
    c = a
    printf(tabldr)
    for i in range(len(tabldr)):
        d = d+1
        c = c -1
        if (d < j)and(c >=0):
            print("+ -")
            tabldr[c][d] = 2
    d = b
    c = a
    printf(tabldr)
    for t in range(len(tabldr)):
        d = d-1
        c = c + 1
        if (d >= 0)and(c <j):
            print("- +")
            tabldr[c][d] = 2
    tabldr[a][b]= 1
    printf(tabldr)
    print("")
    print("posicionado con éxito")
    return tabldr


   
def fin(tabldr):
    for i in range(len(tabldr)):
        for j in range(len(tabldr[i])):
            if (tabldr[i][j]) == 0:
                tabldr[i][j] = 1
    print("tablero finale")
    print("")
    print("************")
    for i in tabldr:
        print(i)
        
        

def printf(tabldr):
   print("")
   print("------------------------")
   for i in tabldr:
       print(i)
       

reinacont(reina,tabldr,llave,xls)
