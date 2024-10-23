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

# Mostrar los nombres de los personajes
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

print(f"\n¡Pelea en el {planeta_elegido}!")
print(f"\n¡{personaje1} vs {personaje2}!")


# Simular la pelea con probabilidad
ganador = random.choice([personaje1, personaje2])

print(f"El ganador es: {ganador}!")

# Enfrentamiento contra Bills
print(f"\n¡{ganador} se enfrenta a Bills!")

# Simular pelea contra Bills con 80% de probabilidad de que gane Bills
probabilidad_bills = 0.8
ganador_final = "Bills" if random.random() < probabilidad_bills else ganador

print(f"El ganador final es: {ganador_final}!")


# Cuestionario
print("\n¡Es hora del cuestionario!")

# Pregunta 1
print("\n1. ¿Cómo se llama el hijo de Bardock y protagonista de Dragon Ball?")
print("1. Goku")
print("2. Kakaroto")
print("3. Insecto")
print("4. Todas son correctas*")

respuesta1 = int(input("Selecciona el número de tu respuesta: "))
if respuesta1 == 4:
    print("¡Correcto!")
else:
    print("Incorrecto. La respuesta correcta es: Todas son correctas.")

# Pregunta 2
print("\n2. ¿Quién es el Saiyan legendario?")
print("1. Vegeta")
print("2. Broly*")
print("3. Freezer")
print("4. Bulma")

respuesta2 = int(input("Selecciona el número de tu respuesta: "))
if respuesta2 == 2:
    print("¡Correcto!")
else:
    print("Incorrecto. La respuesta correcta es: Broly.")

# Pregunta 3
print("\n3. ¿Cuál es la transformación más poderosa actualmente?")
print("1. Goku Ultra Instinto")
print("2. Vegeta Ultra Ego")
print("3. Gohan Beast*")
print("4. Broly Legendario")
print("5. Black Freezer")

respuesta3 = int(input("Selecciona el número de tu respuesta: "))
if respuesta3 == 3:
    print("¡Correcto!")
else:
    print("Incorrecto. La respuesta correcta es: Gohan Beast.")


