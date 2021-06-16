import random
print("cuantos dados desea lanzar?")
dados=int(input("inserte numero de dados: "))
x=0
for x in range(0,dados):
    x=x+1
    numero= random.randint(1,6)
    print(numero)