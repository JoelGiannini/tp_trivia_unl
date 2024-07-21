import random
import os
import json
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
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
Desarrollado por Grupo Saturno.
'''

def menu():
    os.system('clear')
    print(f'{scenery}')
    print('Te damos la bienvenia a la triva de paises de latinoamerica')
    letter = input('presione una tecla  para continuar...').lower()
    os.system('clear')
    print('Reglamento:\n\n')
    print('Tendras que adivinar las capitales de todos los paises de latino america.\nCada acierrto suma 2 puntos, por contrario, cada falla resta 2 puntos y si utilizamos una pista se resta un punto\n\n')
    pause= input('presione una tecla  para continuar...').lower()

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
        respuesta = input(f"¿Cuál es la capital de {pais}?\n")
        if respuesta.lower() == capital.lower():
            os.system("clear")
            print("¡Correcto!")
            puntos += 2
            aciertos+=1

        else:
            os.system("clear")
            print("Incorrecto.")
            errores += 1
            puntos -= 2
            opcion_pista = input("¿Quieres una pista? (sí/no):\n").strip().lower()
            while (opcion_pista != "si" and opcion_pista != "no"):
                opcion_pista = input("Ingresaste una opcion incorrecta por favor ingresar (si/no):\n").strip().lower()
            if opcion_pista == 'si':
                os.system("clear")
                puntos -= 1
                total_pistas += 1
                pista = pistas(i)
                respuesta_ayuda = input(f"Pista:\n{pista}.\n\nUltimo intento.\n\n¿Cuál es la capital de {pais}?\n")
                if respuesta_ayuda.lower() == capital.lower():
                    os.system("clear")
                    print("¡Correcto!\n")
                    puntos += 2
                    aciertos += 1
                else:
                    os.system("clear")
                    print(f"Incorrecto nuevamente. La capital de {pais} es {capital}.\n")
                    errores += 1
                    puntos -= 2
            elif opcion_pista == 'no':
                 os.system("clear")
                 print (f"Ultimo intento para adivinar la capital.\n")
                 respuesta = input(f"¿Cuál es la capital de {pais}?\n")
                 if respuesta.lower() == capital.lower():
                    os.system("clear")
                    print("¡Correcto!")
                    puntos += 2
                    aciertos+=1
                 else:
                    os.system("clear")
                    print("Incorrecto.")
                    errores += 1
                    puntos -= 2
                    print(f"La capital de {pais} es {capital}.\n")
            else:
                os.system("clear")
                print(f"La capital de {pais} es {capital}.\n")
        print()
    os.system("clear")
    print (f"Felicidades has terminado  la trivia.\n\nSu puntuacion total es de:\n\nPuntos: {puntos} sobre 22 puntos\nCorrectas:{aciertos}\nErroneas:{errores}\nCantidad de pistas utilizadas:{total_pistas}")


if __name__ == '__main__':
	
	start()
