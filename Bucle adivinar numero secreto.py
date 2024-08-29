numero_secreto = 777
import time

print(
"""
+================================+
| Bienvenido al juego            |
| Introducí un número entero     |
| y adiviná qué número elegí     |
| ¿Cuál es el número secreto?    |
+================================+
"""
)

numero = int(input("Ingresá el número: "))

while numero != numero_secreto:
    print("Estás atrapado en mi bucle")
    time.sleep(1)
    
    numero = int(input("Ingresá el número nuevamente: "))

print("bien hecho, sos libre")

