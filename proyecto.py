from os import system
system("cls")
import lista_caballos;import random
from datetime import date, time, datetime
import time

dataApuesta = {}
dataTime = []
def apuesta(dataApuesta,dataTime):
    print("Bienvenidos a la sala de apuestas del Patridonomo")
    print("__Lista de caballos a participiar para la carrera__\n")
    caballos_apuesta = []
    cont = 0
    while True:
        caballo = random.choice(lista_caballos.names_caballos)
        if caballo in caballos_apuesta:
            continue
        else:
            caballos_apuesta.append([cont+1,caballo])
        print(f"{cont+1} {caballos_apuesta[cont][1]}")
        cont += 1    
        if len(caballos_apuesta) >= 10:
            break
        
    pregunta = int(input("¿Cuantas personas van a apostar?: "))
    for i in range(pregunta):
        caballoF = int(input(f"Cliente {i+1} eliga al caballo que desea apostar: "))
        n_apuesta = int(input(f"¿Cliente {i+1} Cuanto desea apostar?: "))
        dataApuesta.append([]) 
        dataApuesta[0].append(caballoF), dataApuesta[0].append(n_apuesta)
        dataTime.append(datetime.now())
    for j in range(1):
        ganador = random.choice(caballos_apuesta)
        print(f"¡¡¡El ganador de la carrera es el caballo  #{ganador[0]} {ganador[1]}!!!")
        time.sleep(1)
    if caballoF == ganador:
        '''pago = dataApuesta[ganador[1]] / 2 para el pago del ganador o ganadores y 
        la casa de apuesta, toca revisar'''
        print("¡¡¡Felicidades usted ha ganado!!!");print(f"Su recompensa fue de: {n_apuesta*2}")
    elif caballoF != ganador:
        print("Uy parece que haz perdido");print(f"Tu perdida fue: -{n_apuesta}")

apuesta(dataApuesta,dataTime)