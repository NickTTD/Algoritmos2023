# 2 Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los
# algoritmos necesarios para resolver las siguientes tareas:

from grafo import Grafo
grafo_personajes = Grafo(dirigido=False)
# a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
# cantidad de episodios en los que aparecieron juntos ambos personajes que se
# relacionan;

def insert_vertices():
    characters = [
        'Luke Skywalker',
        'Han Solo',
        'Princess Leia',
        'Darth Vader',
        'Yoda',
        'Obi-Wan Kenobi',
        'Chewbacca',
        'R2-D2',
        'C-3PO',
        'Boba Fett'
        'BB-8'
        'Kylo Ren'
        'Rey',
    ]
    for character in characters:
        grafo_personajes.insert_vertex(character)
insert_vertices()
def insert_arists():
    grafo_personajes.insert_arist('Chewbacca', 'Obi-Wan Kenobi', 2)
    grafo_personajes.insert_arist('Obi-Wan Kenobi', 'Darth Vader', 3)
    grafo_personajes.insert_arist('C-3PO', 'Luke Skywalker', 4)
    grafo_personajes.insert_arist('Luke Skywalker', 'Han Solo', 3)
    grafo_personajes.insert_arist('Luke Skywalker', 'Princess Leia', 4)
    grafo_personajes.insert_arist('Han Solo', 'Princess Leia', 2)
    grafo_personajes.insert_arist('Boba Fett', 'Darth Vader', 3)
    grafo_personajes.insert_arist('Darth Vader', 'Han Solo', 6)
    grafo_personajes.insert_arist('Yoda', 'Luke Skywalker', 3)
    grafo_personajes.insert_arist('R2-D2', 'Luke Skywalker', 3)
    grafo_personajes.insert_arist('Han Solo', 'Kylo Ren', 3)
    grafo_personajes.insert_arist('Kylo Ren', 'Luke Skywalker', 2)
    grafo_personajes.insert_arist('Kylo Ren', 'Rey', 3)
    grafo_personajes.insert_arist('BB-8', 'Rey', 3)
    grafo_personajes.insert_arist('BB-8', 'Luke Skywaler', 3)
insert_arists()

#b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
#Quise hacerlo de una manera que quede mas prolijo el print del árbol de expansión minimo usando
#mi kruskal modificado (Como hice en el tp6 ejercicio 14), pero no logré hacerlo funcionar
#por lo que usé el mismo código que hicimos en clase + agregué la lógica para yoda...

#Pero incluso si yoda no está en al árbol, es decir, es un vértice sin ninguna arista (Comentar linea 35), también cuenta como si estuviera ahi...
#Tampoco entiendo por que Boba fett (y otros personajes) quedan en el primer arbol, separado del segundo árbol, cuando en teoría Boba está conectado a Darth Vader (Linea 36)
#
def b():
    bosque = grafo_personajes.kruskal_original()
    yoda_present = False
    for arbol in bosque:
        if "Yoda" in arbol:
            yoda_present = True
        print('-----arbol------')
        for nodo in arbol.split(';'):
            print(nodo)

    if yoda_present:
        print("Yoda esta en el arbol de exp mininma")
    else:
        print("Yoda no esta en el arbol de exp minima")



#c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son.
def c():
    grafo_personajes.barrido_mas_pesado() #barrido modificado para esto

b()
