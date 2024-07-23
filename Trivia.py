#!/usr/bin/python3
import random
import os
import json

#Color de fuentes

rojo=chr(27)+"[31;1m"
amarillo=chr(27)+"[33;1m"
verde=chr(27)+"[32;1m"
blanco=chr(27)+"[33;97m"

scenery = \
'''   
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''

def menu():
    os.system('clear')
    print(amarillo + scenery)
    print (blanco +"Desarrollado por Grupo Saturno.\n\n")
    print('Te damos la bienvenia a la triva de paises de America del sur')
    letter = input('presione una tecla  para continuar...').lower()
    os.system('clear')
    print('Reglamento:\n\n')
    print('Tendras que adivinar las capitales de todos los paises de America del sur.\nCada acierto suma 2 puntos, por contrario, cada falla resta 2 puntos y si utilizamos una pista se resta un punto\n\n')
    pause= input(verde +'Presione una tecla  para continuar...').lower()

def carga_data():
    with open("paises.json") as file:
        data=json.load(file)
        return data
    
def paises(data):
        for i, j  in zip(data.keys(), data.values()):
            if i == "pais":
                pais=j.lower()
            if i == "capital":
                capital=j.lower()
            return capital

def pistas(data):
    for i, j in zip(data.keys(), data.values()):
        if i == "pista1":
            pista1=j
        if i == "pista2":
            pista2=j
        if i == "pista3":
            pista3=j
    pista = [pista1, pista2, pista3]
    pista=random.choice(pista)
    return pista

def normalizar(s):
    reemplazar = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in reemplazar:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def start():
    menu()
    lista=carga_data()
    puntos=0
    aciertos=0
    errores=0
    total_pistas=0
    os.system("clear")
    for i in lista:
        pais=i["pais"]
        capital=i["capital"]
        respuesta = input(blanco + f"¿Cuál es la capital de {pais}?\n")
        respuesta=normalizar(respuesta)
        if respuesta.lower() == capital.lower():
            os.system("clear")
            print(verde + "¡Correcto!")
            print("")
            puntos += 5
            aciertos+=1
        else:
            os.system("clear")
            print(rojo + "Incorrecto.")
            print("")
            errores += 1
            puntos -= 2
            opcion_pista = input(blanco + "¿Quieres una pista? (sí/no):\n").strip().lower()
            opcion_pista=normalizar(opcion_pista)
            while (opcion_pista != "si" and opcion_pista != "no"):
                opcion_pista = input("Ingresaste una opcion incorrecta por favor ingresar (si/no):\n").strip().lower()
                opcion_pista=normalizar(opcion_pista)
            if opcion_pista == 'si':
                os.system("clear")
                puntos -= 1
                total_pistas += 1
                pista = pistas(i)
                print ("Pista:")
                print (amarillo + f"{pista}")
                print (blanco + "")
                respuesta_ayuda = input(f"Ultimo intento.\n\n¿Cuál es la capital de {pais}?\n")
                respuesta_ayuda=normalizar(respuesta_ayuda)
                if respuesta_ayuda.lower() == capital.lower():
                    os.system("clear")
                    print(verde + "¡Correcto!")
                    print("")
                    puntos += 5
                    aciertos += 1
                else:
                    os.system("clear")
                    print(rojo + "Incorrecto nuevamente.")
                    print ("")
                    print(blanco + f"La capital de {pais} es " + amarillo +  f"{capital}.")
                    print("")
                    errores += 1
                    puntos -= 2
            elif opcion_pista == 'no':
                 os.system("clear")
                 print (f"Ultimo intento para adivinar la capital.\n")
                 respuesta = input(f"¿Cuál es la capital de {pais}?\n")
                 respuesta=normalizar(respuesta)
                 if respuesta.lower() == capital.lower():
                    os.system("clear")
                    print(verde + "¡Correcto!")
                    print("")
                    puntos += 5
                    aciertos+=1
                 else:
                    os.system("clear")
                    print(rojo + "Incorrecto.")
                    print ("")
                    errores += 1
                    puntos -= 2
                    print(blanco + f"La capital de {pais} es " + amarillo +  f"{capital}.")
                    print("")
    os.system("clear")
    print (blanco + f"Felicidades has terminado  la trivia.\n\n")
    print (f"Su puntuacion total es de:\n\n") 
    print ("Puntos: " + verde + f"{puntos} " + blanco + "sobre " + verde + "60 " + blanco + "pustos.\n\n") 
    print(verde + f"Correctas: {aciertos}")
    print(rojo + f"Erroneas: {errores}")
    print(amarillo + f"Cantidad de pistas utilizadas: {total_pistas}")
    salida=input(blanco + f"\n\n¿Queres volver a jugar? (si/no)\n")
    salida=normalizar(salida)
    while (salida != "si" and salida != "no"):
        salida = input("Ingresaste una opcion incorrecta por favor ingresar (si/no):\n").strip().lower()
        salida=normalizar(salida)
    if salida == 'si':
        start()
    else:
        os.system("clear")
        exit(1)

if __name__ == '__main__':
	
	start()
