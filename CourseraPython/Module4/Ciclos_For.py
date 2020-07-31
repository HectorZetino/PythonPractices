for i in range(10):
    print(i)

for i in "Hola Mundo":
    print(i)

def contador(n):
    c = 0 
    for i in range(n):
        c += 1
    return c

contador(10)

def sumatoria(numeros):
    acumulado = 0
    for n in numeros:
        acumulado += n
    return acumulado
    
sumatoria([1,2,3,4,5])

def tabla_multiplicar(numero):
    "Imprime la tabla de multiplicar"
    for indice in [1,2,3,4,5,6,7,8,9,10]:
        print(f"{numero} * {indice} = {numero * indice}")

tabla_multiplicar(8)

def sumatoriaCincuenta():
    sum = 0
    for value in range(2,102,2):
        print(value, end=",")
        sum += value
    return sum

sumatoriaCincuenta()


def ejercicio():
    s = 0 
    for nvalue in range(10):
        s += nvalue
    return s

ejercicio()

def es_primo(numero):

   resultado = True

   for divisor in range(2, numero):

       if (numero % divisor) == 0:

           resultado = False

           break

   return resultado 

es_primo(13)

def Ciclos():
    s = 0
    for n in range(1, 10):
        if n % 7 == 0:
            break;
    s += n

Ciclos()


def Prueba():
    s = 0
    for n in range(1, 10):
        if n % 2 == 0:
            continue;
        s += n

Prueba()

def Continues():
    s = 0

    for n in range(1, 10):

        if n % 2 != 0:

            continue;

            s += n

    else:

        s += 5

Continues()

class SumaDos:
    "Clase de Iteradores para sumar dos posiciones en lista"
    def __init__(self, datos):
        self.datos = datos
        self.indice = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.indice == len(self.datos):
            raise StopIteration()
        elemento = self.datos[self.indice] + 2
        self.indice += 1
        return elemento

print(list(SumaDos([1,2,3,4,5])))