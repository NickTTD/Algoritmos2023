from Pelicula import Pelicula
from pila import Pila
from copy import deepcopy #Usé esta librería para copiar la pila de películas en cada uno de los puntos y
                          #no modificar la original (También se puede hacer con un for in range peliculas.size)
                          #o metiendo todo el código de abajo hasta la linea 23 en una función y llamandola en cada punto...

pelicula1 = Pelicula("Titanic", "Paramount Pictures", 1997)
pelicula2 = Pelicula("Avatar", "20th Century Fox", 2009)
pelicula3 = Pelicula("The Avengers", "Marvel Studios", 2012)
pelicula4 = Pelicula("Interstellar", "Paramount", 2014)
pelicula5 = Pelicula("Rogue One", "Lucasfilm", 2016)
pelicula6 = Pelicula("Deadpool", "Marvel Studios", 2016)
pelicula7 = Pelicula("Solo", "Lucasfilm", 2018)

Peliculas = Pila()
Peliculas.push(pelicula1)
Peliculas.push(pelicula2)
Peliculas.push(pelicula3)
Peliculas.push(pelicula4)
Peliculas.push(pelicula5)
Peliculas.push(pelicula6)
Peliculas.push(pelicula7)



#A
print('PUNTO A')
Peliculas_A = deepcopy(Peliculas)
print('Peliculas estrenadas en 2014:')
for i in range (Peliculas_A.size()):
    elemento = Peliculas_A.on_top()
    if elemento.get_año_estreno() == 2014:
        print('#####')
        print(elemento.get_titulo())
        print(elemento.get_estudio())
        print(elemento.get_año_estreno())
        print('#####')
    Peliculas_A.pop()

#B
print('-----------')
print('PUNTO B')
Peliculas_B = deepcopy(Peliculas)
contador = 0
for i in range(Peliculas_B.size()):
    if Peliculas_B.on_top().get_año_estreno() == 2018:
        contador += 1
    Peliculas_B.pop()
print('Total de películas de 2018:', contador)

#C
print('-----------')
print('PUNTO C; Peliculas de Marvel en 2016:')
Peliculas_C = deepcopy(Peliculas)
for i in range(Peliculas_C.size()):
    if Peliculas_C.on_top().get_estudio() == "Marvel Studios" and Peliculas_C.on_top().get_año_estreno() == 2016:
        print(Peliculas_C.on_top().get_titulo())
        print(Peliculas_C.on_top().get_estudio())
        print(Peliculas_C.on_top().get_año_estreno())
        print('-----------')
    Peliculas_C.pop()

