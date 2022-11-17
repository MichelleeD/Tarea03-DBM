from collections import deque

# Creación de arreglo bidimensional de 1 a n 
n = 0

while n <= 0:
        try:
            n = int(input("Ingrese el número de cajas existentes en el banco: "))
        except:
            print("Por favor, ingrese un número.")

banco = []

for i in range(n):
    banco.append(deque([]))

# Agregar personas a la fila, marcando opción de corte 
corte = '1'

while corte == '1':
    persona = input("Ingrese el nombre de la persona a atender: ")

    caja = 0

    while caja <= 0 or caja > len(banco):
        try:
            caja = int(input("¿En cuál caja deberá ser atendida?: "))
        except:
            print("Por favor, ingrese un número.")

    banco[caja-1].append(persona)

    corte = input("¿Existen más personas por atender? \nIngrese 1 para SÍ y cualquier otra tecla para NO: ")
    print()

m = 0

for i in range(n):
    temp = len(banco[i])

    if temp > m:
        m = temp

corteCajas = []

#Creamos la fila para la única caja disponible
for i in range(m):
    for j in range(n):

        if len(banco[j]) > 0:
            corteCajas.append(banco[j][0])
            banco[j].popleft()

#Imprimimos fila de la única caja disponible
print("El orden de la fila para la única caja abierta es: ")
print(corteCajas)
