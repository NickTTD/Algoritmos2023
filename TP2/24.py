from Personajes import Personajes
from pila import Pila
from copy import deepcopy
Personaje1 = Personajes("Groot", 100)
Personaje2 = Personajes("Iron Man", 11)
Personaje3 = Personajes("Capitán América", 9)
Personaje4 = Personajes("Black Widow", 8)
Personaje5 = Personajes("Thor", 8)
Personaje6 = Personajes("Hulk", 7)
Personaje7 = Personajes("Rocket Raccoon", 3)

Personajes = Pila()
Personajes.push(Personaje1)
Personajes.push(Personaje2)
Personajes.push(Personaje3)
Personajes.push(Personaje4)
Personajes.push(Personaje5)
Personajes.push(Personaje6)
Personajes.push(Personaje7)

#A determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
#ción uno la cima de la pila;
print('---A---')
posicion = 0
Personajes_A = deepcopy(Personajes)
while Personajes_A.size() > 0:
    posicion += 1
    if Personajes_A.on_top().get_nombre() == "Rocket Raccoon" or Personajes_A.on_top().get_nombre() == "Groot":
        print(Personajes_A.on_top().get_nombre(), "se encuentra en la posición:", posicion)
    Personajes_A.pop()
print('---A---')

#B determinar los personajes que participaron en más de 5 películas de la saga, además indi-
#car la cantidad de películas en la que aparece;
print('---B---')
Personajes_B = deepcopy(Personajes)
while Personajes_B.size() > 0:
    if Personajes_B.on_top().get_total_peliculas() > 5:
        print(Personajes_B.on_top().get_nombre(), "Aparece en mas de 5 películas, con un total de: ",Personajes_B.on_top().get_total_peliculas() )
    Personajes_B.pop()
print('---B---')

#C determinar en cuantas películas participo la Viuda Negra (Black Widow);
print('---C---')
Personajes_C = deepcopy(Personajes)
while Personajes_C.size() > 0:
    if Personajes_C.on_top().get_nombre() == "Black Widow":
        print("Black Widow aparece en ", Personajes_C.on_top().get_total_peliculas(), " Películas")
    Personajes_C.pop()
print('---C---')

#D mostrar todos los personajes cuyos nombre empiezan con C, D y G.
print('---D---')
Personajes_D = deepcopy(Personajes)
while Personajes_D.size() > 0:
    if Personajes_D.on_top().get_nombre()[0] == "C":
        print(Personajes_D.on_top().get_nombre(), " Empieza con la letra 'C' ")
    elif Personajes_D.on_top().get_nombre()[0] == "D":
        print(Personajes_D.on_top().get_nombre(), " Empieza con la letra 'D' ")
    elif Personajes_D.on_top().get_nombre()[0] == "G":
        print(Personajes_D.on_top().get_nombre(), " Empieza con la letra 'G' ")
    Personajes_D.pop()
print('---D---')