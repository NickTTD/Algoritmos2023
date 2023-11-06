from grafo import Grafo

#Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:
grafo_casa = Grafo(dirigido=True)

#a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
#baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
def insert_vertices():#Hice esto para colapsarlo en vscode
    grafo_casa.insert_vertex('cocina')
    grafo_casa.insert_vertex('comedor')
    grafo_casa.insert_vertex('cochera')
    grafo_casa.insert_vertex('quincho')
    grafo_casa.insert_vertex('baño 1')
    grafo_casa.insert_vertex('baño 2')
    grafo_casa.insert_vertex('habitación 1')
    grafo_casa.insert_vertex('habitación 2')
    grafo_casa.insert_vertex('sala de estar')
    grafo_casa.insert_vertex('terraza')
    grafo_casa.insert_vertex('patio')
insert_vertices()


#b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco,
# el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;
def insert_arists ():  
    grafo_casa.insert_arist('cocina', 'comedor', 8)
    grafo_casa.insert_arist('cocina', 'cochera', 12)
    grafo_casa.insert_arist('cocina', 'quincho', 5)
    grafo_casa.insert_arist('cocina', 'baño 1', 5)
    grafo_casa.insert_arist('cocina', 'terraza', 15)
    grafo_casa.insert_arist('comedor', 'cochera', 10)
    grafo_casa.insert_arist('comedor', 'baño 1', 4)
    grafo_casa.insert_arist('comedor', 'habitación 1', 6)
    grafo_casa.insert_arist('comedor', 'terraza', 35)
    grafo_casa.insert_arist('comedor', 'baño 2', 10)
    grafo_casa.insert_arist('cochera', 'quincho', 7)
    grafo_casa.insert_arist('cochera', 'habitación 2', 9)
    grafo_casa.insert_arist('cochera', 'terraza', 15)
    grafo_casa.insert_arist('quincho', 'terraza', 8)
    grafo_casa.insert_arist('quincho', 'habitación 1', 10)
    grafo_casa.insert_arist('quincho', 'sala de estar', 12)
    grafo_casa.insert_arist('baño 1', 'habitación 1', 3)
    grafo_casa.insert_arist('baño 1', 'patio', 6)
    grafo_casa.insert_arist('baño 1', 'sala de estar', 9)
    grafo_casa.insert_arist('habitación 1', 'terraza', 12)
    grafo_casa.insert_arist('habitación 1', 'habitación 2', 7)
    grafo_casa.insert_arist('habitación 1', 'cochera', 11)
    grafo_casa.insert_arist('habitación 2', 'terraza', 12)
    grafo_casa.insert_arist('habitación 2', 'sala de estar', 9)
    grafo_casa.insert_arist('habitación 2', 'patio', 7)
    grafo_casa.insert_arist('sala de estar', 'terraza', 12)
    grafo_casa.insert_arist('sala de estar', 'patio', 7)
    grafo_casa.insert_arist('sala de estar', 'habitación 1', 8)
    grafo_casa.insert_arist('habitación 1', 'comedor', 3)
    grafo_casa.insert_arist('comedor', 'sala de estar', 5)
insert_arists()


#c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
#para conectar todos los ambientes;
def c():
    bosque, total = grafo_casa.kruskal()
    for arbol in bosque:
     print('arbol')
    for nodo in arbol.split('|||'):
        print(nodo)
    print('El total es de ', total)


#d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
#determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.
def d():
    ori = 'habitación 1'
    des = 'sala de estar'
    origen = grafo_casa.search_vertice(ori)
    destino = grafo_casa.search_vertice(des)
    camino_mas_corto = None
    listaOutput = []
    if origen is not None and destino is not None:
        if grafo_casa.has_path(ori, des):
            camino_mas_corto = grafo_casa.dijkstra(ori, des)
            fin = des
            while camino_mas_corto.size() > 0:
                value = camino_mas_corto.pop()
                if fin == value[0]:
                    listaOutput.append((value[0], value[1]))
                    fin = value[2]
            listaOutput.reverse()

            # Obtengo el numero de la última tupla
            last_tuple = listaOutput[-1]
            last_number = last_tuple[1]
            print(f'El peso total del camino es: {last_number}')

            #Quitar numeros de la lista
            listaOutput = [place for place, _ in listaOutput]

            #Printear las tuplas sin numeros
            print('Con el siguiente camino: ')
            formatted_output = " -> ".join(f'{place}' for place in listaOutput)
            print(formatted_output)
        else:
            print('No hay camino')

d()
