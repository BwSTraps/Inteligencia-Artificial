import json

Conocimiento = False

with open ("probabilidades.json", "r") as read_file:
    data = json.load(read_file)
    conocimiento = data['Probabilidades']

frase = open('tweet.txt', "r")
palabras = list(frase)

def probabilidad():    
    pila = []
    tweet=palabras[0]
    separatweet = tweet.split(" ")
    suma=0
    for sc in separatweet:
        for probabilidad in conocimiento:
            if sc == probabilidad[0]:
                x=(float(probabilidad[1]),probabilidad[0])
                suma = float(probabilidad[1])+suma
                pila.append(x)
                print(suma)
                
    if     (suma/len(pila)) >0.55:
        print("stream")
    else:
        print("no stream")

    print(suma/len(pila))
    print(pila)