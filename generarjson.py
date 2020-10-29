# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:47:01 2020

@author: crist
"""

import json
import numpy as np

apnpa = ['¿', '?', '¡', '!', '-', '+', ',', ':', ';', '@', '#', 'a', 'con', 'de', 'en', 'cierto', 'claro', 'efectivamente', 'alrededor', 'hoy', 'mañana', 'deprisa',
               'sobre', 'tras', 'ante', 'bajo','sã­',
               'ahí', 'allí', 'respecto', 'aquí', 'arriba', 'abajo', 'fuera', 'ahora', 'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'abajo', 'cerca', 'lejos', 'encima',
          'a', 'de', 'desde', 'despues', 'durante', 'en', 'hasta', 'por',
          'sobre', 'tras', 'encima', 'según', 'sin', 'muy', 'mas', 'poco',
          'bastante', 'acaso', 'tampoco', 'probablemente', 'dónde', 'cuándo', 'qué', 'mal', 'bien', 'regular', 'ni', 'despacio', 'y',
          'similar', 'facilmente', 'mejor', 'peor', 'así', 'algo', 'casi', 'tal vez', 'le', 'mis',
          'acaso', 'quizás', 'que', 'este', 'sí', 'un', 'al']

puntuacion = [':', '(', ')', '=', '¿', '?', '¡', '!',
                 '-', '+', ',', ':', ';', '@', '#', '.','0','1','2','3','4','5','6','7','8','9']

def abrirJson():
    with open("tweets.json", "r") as read_file:
        data = json.load(read_file)
        conocimiento = data['Tweets']
    
    streams=[]
    
    for c in conocimiento:
        if c['Stream']==True:
            tweet=c["texto"]
            tweet=tweet.split(" ")
            
            for t in tweet:
                letraC=t.lower()
                streams.append(letraC)
    filtrar_remplazar(streams)

def filtrar_remplazar(streams):
    print(streams)
    print("\n  \n")
    filtrado=[]
    indice = 0
    for s in streams:
        for e in apnpa:
            if s == e:
                filtrado.append(indice)
        indice=indice+1
    
    for f in reversed(filtrado) :
        streams.pop(f)

   
    
    
    for n, i in enumerate(streams):
        for sig in puntuacion:
            if str.__contains__(i, sig):
                streams[n] = streams[n].replace(sig,"")

    espacio=[]
    ind=0
    for s in streams:
        if s == '':
            espacio.append(ind)
        ind=ind+1
    
    if len(espacio)>0:
        for espa in reversed(espacio):
            streams.pop(espa)
    
    final=[]
    mas=[]
    for s in streams:
        contador_palabra = s, streams.count(s)
        mas.append(streams.count(s))
        final.append(contador_palabra)
    final=sorted(set(final))
    
    
    mayor=max(mas)
    
    generaJson(final,mayor)

def generaJson(final,mayor):
    print(mayor)
    print(final)
    texto=''
    for f in final:
        texto = texto+str('["')+str(f[0])+str('",')+str(f[1]/mayor)+str("], \n")
    temp=len(texto)
    texto = texto[:temp - 3]
    
    texto= '{ "Probabilidades": [ \n' + texto + " \n ]}"

    file = open("C:/Users/crist/desktop/pruebaleoprobabilidades2/resultado.json", "w")
    file.write(texto)
    file.close()
    