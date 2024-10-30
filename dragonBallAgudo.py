
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 23:54:01 2024

@author: Usuario
"""

import requests
import random

# URL
url = "https://dragonball-api.com/api/characters"

# Enviar una solicitud GET a la URL
respuesta = requests.get(url)
respuesta.raise_for_status()  # Lanza un error para respuestas malas

# Analizar la respuesta JSON
personajes = respuesta.json().get("items", [])

#------------------ Mostrar los nombres de los personajes----------------------
print("Personajes disponibles:")
for i, personaje in enumerate(personajes):
    print(f"{i + 1}. {personaje['name']}")

# Solicitar los personajes al usuario
eleccion1 = int(input("Elige el número del primer personaje: ")) - 1
eleccion2 = int(input("Elige el número del segundo personaje: ")) - 1

# Obtener los nombres de los personajes elegidos
personaje1 = personajes[eleccion1]["name"]
personaje2 = personajes[eleccion2]["name"]

# Elegir el planeta para la pelea
planetas = ["Tierra", "Namek", "Planeta Vegeta", "Planeta de Bills"]
print("\nElige el planeta para la pelea:")
for i, planeta in enumerate(planetas):
    print(f"{i + 1}. {planeta}")

eleccion_planeta = int(input("Elige el número del planeta: ")) - 1
planeta_elegido = planetas[eleccion_planeta]

print(f"\n---¡Pelea en el {planeta_elegido}!---")
print(f"\n{personaje1} vs {personaje2}")


#------------------- Simular la pelea con probabilidad-------------------------
ganador = random.choice([personaje1, personaje2])
print(f"El ganador es: {ganador} con !")

#--------------------- Enfrentamiento contra Bills-----------------------------
print(f"\n----¡{ganador} se enfrenta a Bills!----")

# Simular pelea contra Bills con 80% de probabilidad de que gane Bills
probabilidad_bills = 0.8
ganador_final = "Bills" if random.random() < probabilidad_bills else ganador

print(f"El ganador final es: {ganador_final}!")


#-------------------------------Cuestionario---------------------------------
print("\n¡Es hora del cuestionario!")

# Pregunta1
print("1. ¿Cómo se llama el hijo de Bardock y protagonista de Dragon Ball?")
print("1. Gohan")
print("2. Kakaroto*")
print("3. Vegeta")
print("4. Todas son correctas")

respuesta1 = int(input("Selecciona el número de tu respuesta: "))
if respuesta1 == 2:
    print("¡Correcto!")
else:
    print("Incorrecto. La respuesta correcta es: Kakaroto.")

# Pregunta2
print("\n2. ¿De que color es el pelo del SSJBlue?")
print("1. Rojo")
print("2. Amarillo")
print("3. Verde")
print("4. Azul*")

respuesta2 = int(input("Selecciona el número de tu respuesta: "))
if respuesta2 == 4:
    print("¡Correcto!")
else:
    print("Incorrecto. La respuesta correcta es: Azul.")

# Pregunta3
print("\n3. ¿Cuantas Esferas de dragon hay en la tierra?")
print("1. 2")
print("2. 3")
print("3. 5")
print("4. 6")
print("5. 7*")

respuesta3 = int(input("Selecciona el número de tu respuesta: "))
if respuesta3 == 5:
    print("¡Correcto!")
else:
    print("Incorrecto. La respuesta correcta es: 7.")


# ---------------------Preguntar por la cantidad de esferas--------------------
esferas = int(input("\n¿Cuántas esferas tienes? "))

# Función para pedir deseos
def pedir_deseos():
    deseos = []
    print("Tienes 7 esferas. ¡Puedes pedir deseos!")
    for i in range(3):
        deseo = input(f"Escribe tu deseo número {i + 1}: ")
        deseos.append(deseo)
    return deseos

# Pedir deseos si el usuario tiene 7 esferas
if esferas < 7:
    print("Debes buscar 7 esferas.")
elif esferas == 7:
    deseos = pedir_deseos()
    print("Tus deseos son:")
    for i, deseo in enumerate(deseos, start=1):
        print(f"Deseo {i}: {deseo}")
else:
    print("Tienes más de 7 esferas. ¡Sigue adelante con tu aventura!")