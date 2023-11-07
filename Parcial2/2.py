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
        'Boba Fett',
        'BB-8',
        'Kylo Ren',
        'Rey',
    ]
    for character in characters:
        grafo_personajes.insert_vertex(character)
insert_vertices()
def insert_aristas():
    grafo_personajes.insert_arist('Chewbacca', 'Obi-Wan Kenobi', 2)
    grafo_personajes.insert_arist('Obi-Wan Kenobi', 'Darth Vader', 3)
    grafo_personajes.insert_arist('C-3PO', 'Luke Skywalker', 4)
    grafo_personajes.insert_arist('Luke Skywalker', 'Han Solo', 3)
    grafo_personajes.insert_arist('Luke Skywalker', 'Princess Leia', 4)
    grafo_personajes.insert_arist('Han Solo', 'Princess Leia', 2)
    grafo_personajes.insert_arist('Boba Fett', 'Darth Vader', 3)
    grafo_personajes.insert_arist('Darth Vader', 'Han Solo', 6)
    #grafo_personajes.insert_arist('Yoda', 'Luke Skywalker', 3)
    grafo_personajes.insert_arist('R2-D2', 'Luke Skywalker', 3)
    grafo_personajes.insert_arist('Han Solo', 'Kylo Ren', 3)
    grafo_personajes.insert_arist('Kylo Ren', 'Luke Skywalker', 2)
    grafo_personajes.insert_arist('Kylo Ren', 'Rey', 3)
    grafo_personajes.insert_arist('BB-8', 'Rey', 3)
    grafo_personajes.insert_arist('BB-8', 'Luke Skywaler', 3)
insert_aristas()

#b) hallar el árbol de expansión minino y determinar si contiene a Yoda;

#Quise hacerlo de una manera que quede mas prolijo el print del árbol de expansión minimo usando
#mi kruskal modificado (Como hice en el tp6 ejercicio 14), pero no logré hacerlo funcionar
#por lo que usé el mismo código que hicimos en clase + agregué la lógica para yoda...

#Si yoda está por si solo, es decir, no tiene ninguna arista (Porque la linea 38 está comentada), devuelve que no está en ningún arbol (Aunque podría)
#considerarse que un vertice solo es un árbol, creo que no tendría gracia, por lo que hice que si es parte de uno de los árboles de expansión posibles, detecte
#la arista.
#(Des comentar linea 38 para probar)
def b():
    bosque = grafo_personajes.kruskal_original()
    yoda_present = False

    print('-----arboles-----')
    for arbol in bosque:
        print(arbol)

        # Verifica si Yoda está presente en alguna arista
        for nodo in arbol.split(';'):
            if "Yoda" in nodo and '-' in nodo:  # Verifica que haya una arista que incluya a Yoda
                yoda_present = True

    if yoda_present:
        print("Yoda está en algún árbol de expansión mínima")
    else:
        print("Yoda no está en ningún árbol de expansión mínima")


#c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son.
def c():
    grafo_personajes.barrido_mas_pesado() #barrido modificado para esto

b()
