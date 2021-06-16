import random
print("cuantos dados desea lanzar?")
dados=int(input("inserte numero de dados: "))
print("cuantos caras tiene el dado")
caras=int(input("inserte numero de dcaras: "))
x=0
for x in range(0,dados):
    x=x+1
    numero= random.randint(1,caras)
    print(numero)