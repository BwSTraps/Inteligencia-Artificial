# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:29:04 2020

@author: crist
"""

import json 
Conocimiento = False

with open ("animales.json", "r") as read_file:
    data = json.load(read_file)
    Conocimiento = data['conocimiento']
    
def compara(animal,pertenencia,cosa,CON):
    if not CON:
        return False
    cont = 0
    f = len(CON)
    if pertenencia == "vive" or pertenencia == "tiene":
        while cont < f:
            if CON[cont][0] == animal and CON[cont][1] == pertenencia and CON[cont][2] == cosa:
                return True
                print("Datos correctos")
            cont = cont + 1
        else:
            return False
            print("Datos incorrectos")
    else:
        while cont < f:
            if CON[cont][0] == animal:
                if CON[cont][1] == pertenencia:
                    if CON[cont][2] == cosa:
                        return True
                        print("Datos correctos")
                    else:
                        animal = CON[cont][2]
                        cont = -1
            cont = cont + 1
        else:
            return False
            print("Datos inccorrectos")

def consulta(animal,pertenencia,cosa):
    return compara(animal,pertenencia,cosa,Conocimiento)

def main():
    print("CONSULTA SEMANTICA DE ANIMALES")
    print("EJEMPLO DE SINTAXIS")
    print('Escribe: consulta("tortuga","tiene","garras")')
    print("****Escribir como tal viene el ejemplo la cadena especificada****")
    print("Para salir escribe: salir")
    Finalizar= False
    while not Finalizar:
        Leer = input("> ")
        if Leer == 'salir':
            return
        Imprimir = eval(Leer)
        print(Imprimir)
        
if __name__ == "__main__":
     main()
    
