#Este es un simulador de dados
import random
contador = 1
booleano = False
def tiradas():
    "Este es el simulador de las tiradas de los dados"
    valor_a = 0
    valor_b = 0
    sumatoria = 0
    valor_a = int(random.random()*10)%6+1
    valor_b = int(random.random()*10)%6+1
    sumatoria = valor_a + valor_b
    print("Tirada No.", str(contador))
    print("Valor dado A: ", valor_a)
    print("Valor dado B: ", valor_b)
    print("Suma de los dados: ", sumatoria)

while booleano == False:
    "Ciclo while que realizara la funcion de control"
    pass
    if contador == 1:
        tiradas()
        contador += 1
    else:
        Respuesta = input("Ingrese el numero de la accion a realizar \n1. Realizar otra tirada \n2. Cerrar Programa: ")
        if Respuesta == "1":
            tiradas()
            contador += 1
            booleano = False
        else:
            print("Gracias por utilizar el programa")
            booleano = True

#Hector Zetino




    