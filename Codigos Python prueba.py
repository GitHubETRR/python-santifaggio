#codigos de prueba para python
nombre = input("ingresá tu nombre: ")
edad = input("ingresá tu edad: ")
print(f"Buenas {nombre}. Tu edad es de {edad} años.")


numero = 18       
euler = 2.718
es_estudiante = False  
mensaje = "Me llamo Santi"  


colores = ["rojo", "amarillo", "azul"]
print("Los colores primarios son:\n", colores)

autos = ("camaro", "challenger", "mustang")
print("autos:", autos)


#probando ciclos

print("Lista de colores:")
for color in colores:
    print(color)

for c in colores:
    print(c, len(c))

contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1


