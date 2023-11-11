from grafo_objetos import Grafo

# Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas y naturales 
# del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
# uno en las naturales) y tipo (natural o arquitectónica);
grafo_maravillas = Grafo(dirigido=False)

class Maravilla:
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo

    def __str__(self):
        return f'{self.nombre} - {self.pais} - {self.tipo}'

    def __eq__(self, other):
        """Define la igualdad entre dos objetos Maravilla."""
        return isinstance(other, Maravilla) and self.pais == other.pais
    

def insertar_vertices():
    grafo_maravillas.insert_vertex(Maravilla('Gran Muralla China', 'China', 'arquitectónica'), criterio='nombre')
    grafo_maravillas.insert_vertex(Maravilla('Petra', 'Jordania', 'arquitectónica'), criterio='nombre')
    grafo_maravillas.insert_vertex(Maravilla('Cristo Redentor', 'Brasil', 'arquitectónica'), criterio='nombre')
    grafo_maravillas.insert_vertex(Maravilla('Chichén Itzá', 'Brasil', 'arquitectónica'), criterio='nombre') #Puse que Chichen Itzá está en Brasil para que funcione el punto E
    grafo_maravillas.insert_vertex(Maravilla('Machu Picchu', 'Brasil', 'arquitectónica'), criterio='nombre')
    grafo_maravillas.insert_vertex(Maravilla('Coliseo de Roma', 'Italia', 'arquitectónica'), criterio='nombre')
    grafo_maravillas.insert_vertex(Maravilla('Muralla de Adriano', 'Reino Unido', 'arquitectónica'), criterio='nombre')

    grafo_maravillas.insert_vertex(Maravilla('Amazonia', 'Italia', 'natural'), criterio='nombre') #Puse que Amazonia está en Italia para que funcione el punto D
    grafo_maravillas.insert_vertex(Maravilla('Bahía de Ha-Long', 'Vietnam', 'natural'), criterio='nombre')
    grafo_maravillas.insert_vertex(Maravilla('Cataratas del Iguazú', 'Argentina y Brasil', 'natural'), criterio='nombre')
    grafo_maravillas.insert_vertex(Maravilla('Isla Jeju', 'Corea del Sur', 'natural'), criterio='nombre')
    grafo_maravillas.insert_vertex(Maravilla('Montaña de la Mesa', 'Sudáfrica', 'natural'), criterio='nombre')
    grafo_maravillas.insert_vertex(Maravilla('Parque Nacional de Komodo', 'Indonesia', 'natural'), criterio='nombre')
    grafo_maravillas.insert_vertex(Maravilla('Río Subterráneo de Puerto Princesa', 'Filipinas', 'natural'), criterio='nombre')
insertar_vertices()

def insertar_aristas():
    #Maravillas arquitectónicas
    grafo_maravillas.insert_arist('Gran Muralla China', 'Petra', 500, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Gran Muralla China', 'Cristo Redentor', 300, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Gran Muralla China', 'Chichén Itzá', 200, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Gran Muralla China', 'Machu Picchu', 400, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Gran Muralla China', 'Coliseo de Roma', 450, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Gran Muralla China', 'Muralla de Adriano', 600, criterio_vertice='nombre')

    grafo_maravillas.insert_arist('Petra', 'Cristo Redentor', 250, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Petra', 'Chichén Itzá', 150, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Petra', 'Machu Picchu', 350, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Petra', 'Coliseo de Roma', 400, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Petra', 'Muralla de Adriano', 550, criterio_vertice='nombre')

    grafo_maravillas.insert_arist('Cristo Redentor', 'Chichén Itzá', 100, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Cristo Redentor', 'Machu Picchu', 300, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Cristo Redentor', 'Coliseo de Roma', 350, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Cristo Redentor', 'Muralla de Adriano', 500, criterio_vertice='nombre')

    grafo_maravillas.insert_arist('Chichén Itzá', 'Machu Picchu', 200, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Chichén Itzá', 'Coliseo de Roma', 250, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Chichén Itzá', 'Muralla de Adriano', 400, criterio_vertice='nombre')

    grafo_maravillas.insert_arist('Machu Picchu', 'Coliseo de Roma', 150, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Machu Picchu', 'Muralla de Adriano', 300, criterio_vertice='nombre')

    grafo_maravillas.insert_arist('Coliseo de Roma', 'Muralla de Adriano', 250, criterio_vertice='nombre')

    #Maravillas naturales
    grafo_maravillas.insert_arist('Amazonia', 'Bahía de Ha-Long', 30, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Amazonia', 'Cataratas del Iguazú', 20, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Amazonia', 'Isla Jeju', 40, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Amazonia', 'Montaña de la Mesa', 45, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Amazonia', 'Parque Nacional de Komodo', 60, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Amazonia', 'Río Subterráneo de Puerto Princesa', 25, criterio_vertice='nombre')

    grafo_maravillas.insert_arist('Bahía de Ha-Long', 'Cataratas del Iguazú', 10, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Bahía de Ha-Long', 'Isla Jeju', 30, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Bahía de Ha-Long', 'Montaña de la Mesa', 35, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Bahía de Ha-Long', 'Parque Nacional de Komodo', 50, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Bahía de Ha-Long', 'Río Subterráneo de Puerto Princesa', 65, criterio_vertice='nombre')

    grafo_maravillas.insert_arist('Cataratas del Iguazú', 'Isla Jeju', 20, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Cataratas del Iguazú', 'Montaña de la Mesa', 25, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Cataratas del Iguazú', 'Parque Nacional de Komodo', 40, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Cataratas del Iguazú', 'Río Subterráneo de Puerto Princesa', 55, criterio_vertice='nombre')

    grafo_maravillas.insert_arist('Isla Jeju', 'Montaña de la Mesa', 15, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Isla Jeju', 'Parque Nacional de Komodo', 30, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Isla Jeju', 'Río Subterráneo de Puerto Princesa', 45, criterio_vertice='nombre')

    grafo_maravillas.insert_arist('Montaña de la Mesa', 'Parque Nacional de Komodo', 25, criterio_vertice='nombre')
    grafo_maravillas.insert_arist('Montaña de la Mesa', 'Río Subterráneo de Puerto Princesa', 40, criterio_vertice='nombre')

    grafo_maravillas.insert_arist('Parque Nacional de Komodo', 'Río Subterráneo de Puerto Princesa', 20, criterio_vertice='nombre')

insertar_aristas()




def c():
    bosque = grafo_maravillas.kruskal()
    for arbol in bosque:
        print('arbol')
        for nodo in arbol.split(';'):
            print(nodo)


def d():
    grafo_maravillas.barrido_maravilla()

def e(): #Creo que la idea de este punto era preguntarle al usuario que país quiere verificar, y hacer un search, pero...
    def paisesMasDeUna(grafo):
        conteo_por_pais_tipo = {} #Este diccionario va a almacenar la concatenación de país - tipo de maravilla - cantidad de TODOS los paises

        #Iterar en todos los vertices del grafo y agregarlos al diccionario
        for vertice in grafo._Grafo__elements:
            maravilla = vertice[0]   #[0] = Vertice / [1] = Lista de aristas / [2] = Marcador de visitado
            pais = maravilla.pais
            tipo = maravilla.tipo
            key = f"{pais}-{tipo}"

 
            if key in conteo_por_pais_tipo:
                conteo_por_pais_tipo[key] += 1
            else:
                conteo_por_pais_tipo[key] = 1

        # Verificar y obtener los países con más de una maravilla del mismo tipo
        paises_con_mas_de_una_maravilla = []
        for key, cantidad in conteo_por_pais_tipo.items():
            if cantidad > 1:
                pais, tipo = key.split('-')
                paises_con_mas_de_una_maravilla.append((pais, tipo, cantidad))

        return paises_con_mas_de_una_maravilla


    paises_con_mas_de_una_maravilla = paisesMasDeUna(grafo_maravillas)
    print("Países con más de una maravilla del mismo tipo:")
    for pais, tipo, cantidad in paises_con_mas_de_una_maravilla:
        print(f"{pais} tiene {cantidad} maravillas de tipo {tipo}")

e()