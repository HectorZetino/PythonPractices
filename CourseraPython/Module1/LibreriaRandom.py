import random
print(int(random.random()*10)%6+1) #valores random entre 1 - 6

print(random.choice([1,2,3,4,5,6])) #toma un valor de una lista en forma aleatoria
 
print(random.choices([1,2,3,4,5,6], k=2)) #toma segun los valores que querramos de una lista creada