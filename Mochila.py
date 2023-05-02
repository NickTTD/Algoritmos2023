'''El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
ayuda de la fuerza” realizar las siguientes actividades:
a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
queden más objetos en la mochila;
b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
car para encontrarlo;
c. Utilizar un vector para representar la mochila.'''

mochila = ['blaster', 'comida', 'repuestos','xd', 'sable de luz']
cont = 0

def usar_la_fuerza(mochila, cont):
    if len(mochila) == 0:
        return -1, cont
    elif mochila[0] == 'sable de luz':
        return cont+1, cont
    else:
        return usar_la_fuerza(mochila[1:], cont+1)

cont, eliminados = usar_la_fuerza(mochila, cont)
if cont != -1:
    print('Fue necesario sacar', eliminados, ' objetos')