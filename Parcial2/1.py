# 1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
# de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
# tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
from arbol_binario import BinaryTree

lista_pokemons = [
    {'name': 'Pikachu', 'number': 25, 'tipo': 'electric'},
    {'name': 'Bulbasaur', 'number': 1, 'tipo': 'grass/poison'},
    {'name': 'Charmander', 'number': 4, 'tipo': 'fire'},
    {'name': 'Squirtle', 'number': 7, 'tipo': 'water'},
    {'name': 'Jigglypuff', 'number': 39, 'tipo': 'normal/fairy'},
    {'name': 'Meowth', 'number': 52, 'tipo': 'steel'},
    {'name': 'Psyduck', 'number': 54, 'tipo': 'water'},
    {'name': 'Machop', 'number': 66, 'tipo': 'fighting'},
    {'name': 'Geodude', 'number': 74, 'tipo': 'rock/ground'},
    {'name': 'Ponyta', 'number': 77, 'tipo': 'fire'},
    {'name': 'Slowpoke', 'number': 79, 'tipo': 'water/psychic'},
    {'name': 'Jolteon', 'number': 135, 'tipo': 'electric'},
    {'name': 'Lycanroc', 'number': 745, 'tipo': 'rock'},
    {'name': 'Tyrantrum', 'number': 697, 'tipo': 'rock/dragon'},
]

arbol_name = BinaryTree()
arbol_number = BinaryTree()
arbol_tipo = BinaryTree()

for pokemon in lista_pokemons:
    name = pokemon['name']
    number = pokemon['number']
    tipo = pokemon['tipo']

    arbol_name.insert_node(name, {'number': number, 'tipo': tipo})
    arbol_number.insert_node(number, {'name': name, 'tipo': tipo})
    arbol_tipo.insert_node(tipo, {'name': name, 'number': number})

# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
# mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
# caracteres–;

def b1 (): #Nombre por proximidad
    buscado = input('Ingrese nombre de pokemon a buscar: ')
    arbol_name.search_by_coincidence(buscado)

def b2 (): #Por numero sin proximidad
    buscado = int(input('Ingrese nombre de pokemon a buscar: '))
    arbol_number.search_print_node(buscado)

#c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
def c(): #Intenté hacer una modificación del inorden que acepte una lista, pero no logré hacerlo funcionar, está en arbol_binario.py con nombre inorden_pokemon_tip
    arbol_tipo.search_by_coincidence('water')
    arbol_tipo.search_by_coincidence('fire')
    arbol_tipo.search_by_coincidence('plant')
    arbol_tipo.search_by_coincidence('electric')


#d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
#además un listado por nivel por nombre;

def d():
    print('inorden ascendente ')
    #arbol_number.nodetorden_pokemon()  #pensé que había que modificar el inorden invertido para tamibién mostrar nombre
    arbol_number.nodetorden()
    arbol_name.inorden()
    print('')
    print('nombre por nivel')
    print('')
    arbol_name.by_level()

#e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
def e():
    arbol_name.search_print_node('Jolteon')
    arbol_name.search_print_node('Lycanroc')
    arbol_name.search_print_node('Tyrantrum')

#Determina cuantos Pokémons hay de tipo eléctrico y acero.
#Sería buena idea adaptar el contar para que haga un estilo search by coincidence, porque en mi caso
#si tengo multiples tipos estan separados con una / 
def f():
    print('De tipo eléctrico hay: ',arbol_tipo.contar('electric'))
    print('De tipo acero hay: ',arbol_tipo.contar('steel'))

