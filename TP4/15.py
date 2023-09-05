from PokemonEntrenador import Pokemon,EntrenadorPokemon
from lista_lista import Lista
from lista import ListaSimple
import msvcrt

def wait_for_key(): #Robé esto de internet, solo lo uso en el menu y es para esperar que el usuario presione una tecla antes de volver a mostrar el menu
    print("\nPresione una tecla para continuar...\n -------------------------")
    msvcrt.getch()  


pokemon1 = Pokemon("Pikachu", 30, "Eléctrico", None)
pokemon2 = Pokemon("Charizard", 15, "Fuego", "Volador")
pokemon3 = Pokemon("Bulbasaur", 20, "Planta", "Veneno")
pokemon4 = Pokemon("Squirtle", 25, "Agua", None)
pokemon5 = Pokemon("Tyrantrum", 40, "Roca", "Dragón")
pokemon6 = Pokemon("Terrakion", 45, "Lucha", "Roca")
pokemon7 = Pokemon("Wingull", 22, "Agua", "Volador")
pokemon8 = Pokemon("Pikachu", 50, "Electrico", None)

entrenador1 = EntrenadorPokemon("Ash Ketchum", 5, 3, 7)
entrenador2 = EntrenadorPokemon("Misty", 3, 2, 6)
entrenador3 = EntrenadorPokemon("Gary Oak", 7, 1, 9)
entrenador4 = EntrenadorPokemon("Brock", 4, 2, 8)
entrenador5 = EntrenadorPokemon("May", 6, 3, 8)
entrenador6 = EntrenadorPokemon("Serena", 8, 4, 10)

lista_entrenadores = Lista()
lista_entrenadores.insert(entrenador1, 'nombre')
lista_entrenadores.insert(entrenador2, 'nombre')
lista_entrenadores.insert(entrenador3, 'nombre')
lista_entrenadores.insert(entrenador4, 'nombre')
lista_entrenadores.insert(entrenador5, 'nombre')
lista_entrenadores.insert(entrenador6, 'nombre')

pokemon_entrenadores = {
    "Ash Ketchum": [pokemon1, pokemon2, pokemon8],
    "Misty": [pokemon3],
    "Gary Oak": [pokemon4],
    "Brock": [pokemon5],
    "May": [pokemon6, pokemon7],
    "Serena": [pokemon1, pokemon2, pokemon3]
}

for i in range (lista_entrenadores.size()):
    nombre_entrenador = lista_entrenadores.get_element_by_index(i)[0].nombre
    if nombre_entrenador in pokemon_entrenadores:
        for pokemon in pokemon_entrenadores[nombre_entrenador]:
            lista_entrenadores.get_element_by_index(lista_entrenadores.search(nombre_entrenador, 'nombre'))[1].insert(pokemon)


#lista_entrenadores.barrido()


#a. obtener la cantidad de Pokémons de un determinado entrenador;
def a():
    EntrenadorSeleccionado = input('Ingrese el nombre del entrenador')
    CantidadPokemones = (lista_entrenadores.get_element_by_index(lista_entrenadores.search(EntrenadorSeleccionado, 'nombre'))[1].size())
    print(f"{EntrenadorSeleccionado} Tiene {CantidadPokemones} pokemones")

#b. listar los entrenadores que hayan ganado más de tres torneos;
def b():
    for i in range (lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(i)[0]
        if entrenador.batallas_ganadas > 3 :
            print(f"{entrenador.nombre} Ganó mas de 3 batallas ({entrenador.batallas_ganadas})")

#c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
def c():
    mayor_cantidad = lista_entrenadores.get_element_by_index(0)[0].torneos_ganados
    pos_mayor = 0
    for pos in range(1, lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(pos)[0]
        if entrenador.torneos_ganados > mayor_cantidad:
            pos_mayor = pos
            mayor_cantidad = entrenador.torneos_ganados


    valor = lista_entrenadores.get_element_by_index(pos_mayor)
    entrenador, sublista = valor[0], valor[1]

    pokemon_mayor = None
    if sublista.size() > 0:
        pokemon_mayor = sublista.get_element_by_index(0)


        for pos in range(sublista.size()):
            pokemon = sublista.get_element_by_index(pos)
            if pokemon.nivel > pokemon_mayor.nivel:
                pokemon_mayor = pokemon

    if pokemon_mayor:
        print(f'El Pokémon de mayor nivel del entrenador {entrenador.nombre} es {pokemon_mayor.nombre} ({pokemon_mayor.nivel})')
    else:
        print(f'No se encontró ningún Pokémon para el entrenador {entrenador.nombre} con torneos ganados {mayor_cantidad}')


#d. mostrar todos los datos de un entrenador y sus Pokémos;
def d():
    EntrenadorSeleccionado = input('Ingrese el nombre del entrenador')

    valor = lista_entrenadores.get_element_by_index(lista_entrenadores.search(EntrenadorSeleccionado, 'nombre'))
    entrenador, sublista = valor[0], valor[1]
    print(entrenador)
    for pos in range(sublista.size()):
            pokemon = sublista.get_element_by_index(pos)
            print (pokemon)    

#e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
def e():
    def calcular_porcentaje(entrenador):
        total_batallas = entrenador.batallas_ganadas + entrenador.batallas_perdidas
        if total_batallas == 0:
            return 0  # Evita dividir por 0
        return (entrenador.batallas_ganadas / total_batallas) * 100
    
    for i in range(lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(i)[0]
        porcentaje_ganadas = calcular_porcentaje(entrenador)
        if porcentaje_ganadas > 79:
            print(f"{entrenador.nombre} tiene un porcentaje de batallas ganadas del {porcentaje_ganadas}%")

#f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
def f():
       for i in range(lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(i)[0]

        for k in range(lista_entrenadores.get_element_by_index(i)[1].size()):
            pokemon = lista_entrenadores.get_element_by_index(i)[1].get_element_by_index(k)
            tipo_pokemon = pokemon.tipo
            subtipo_pokemon = pokemon.subtipo

            if ((tipo_pokemon == "Fuego" or tipo_pokemon == "Planta") and (subtipo_pokemon == "Agua" or subtipo_pokemon == "Volador")):
                print(f'Entrenador: {entrenador.nombre}')
                print(f"Pokémon: {pokemon.nombre}, Tipo: {tipo_pokemon}, Subtipo: {subtipo_pokemon}")

#g. el promedio de nivel de los Pokémons de un determinado entrenador;
def g():
    EntrenadorSeleccionado = input('Ingrese el nombre del entrenador')
    valor = lista_entrenadores.get_element_by_index(lista_entrenadores.search(EntrenadorSeleccionado, 'nombre'))
    entrenador, sublista = valor[0], valor[1]

    if sublista.size() > 0:
        print(f"Niveles de los Pokémon de {entrenador.nombre}:")
        for pos in range(sublista.size()):
            pokemon = sublista.get_element_by_index(pos)
            print(f"{pokemon.nombre}: {pokemon.nivel}")

        total_nivel = 0
        for pos in range(sublista.size()):
            pokemon = sublista.get_element_by_index(pos)
            total_nivel += pokemon.nivel

        promedio_nivel = total_nivel / sublista.size()
        print(f"Promedio de nivel de los Pokémon de {entrenador.nombre}: {promedio_nivel}")
    else:
        print(f"{entrenador.nombre} no tiene ningún Pokémon.")

#h. determinar cuántos entrenadores tienen a un determinado Pokémon;
def h():
    PokemonBuscado = input('Ingrese el nombre del Pokémon que desea buscar')
    contador_entrenadores = 0

    for i in range(lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(i)[0]
        sublista_pokemon = lista_entrenadores.get_element_by_index(i)[1]

        for k in range(sublista_pokemon.size()):
            pokemon = sublista_pokemon.get_element_by_index(k)
            if pokemon.nombre == PokemonBuscado:
                contador_entrenadores += 1

    print(f"{contador_entrenadores} entrenadores tienen a {PokemonBuscado}.")

#i. mostrar los entrenadores que tienen Pokémons repetidos;
def i():
    Minimo1Repetido = False
    for i in range(lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(i)[0]
        sublista_pokemon = lista_entrenadores.get_element_by_index(i)[1]

        nombres_pokemon = ListaSimple()
        pokemon_repetidos = False
        for k in range(sublista_pokemon.size()):
            pokemon = sublista_pokemon.get_element_by_index(k)
            if nombres_pokemon.search(pokemon.nombre) is not None:
                if not pokemon_repetidos:
                    print("Entrenadores que tienen Pokémon con nombres repetidos:")
                    pokemon_repetidos = True
                    Minimo1Repetido = True
                print(entrenador.nombre)
            else:
                nombres_pokemon.insert(pokemon.nombre)
    if not Minimo1Repetido:
        print("No hay entrenadores con repetidos")

#j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-rrakion o Wingull;

def j():
    for i in range(lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(i)[0]
        sublista_pokemon = lista_entrenadores.get_element_by_index(i)[1]

        for k in range(sublista_pokemon.size()):
            pokemon = sublista_pokemon.get_element_by_index(k)
            if pokemon.nombre in ["Tyrantrum", "Terrakion", "Wingull"]:
                print(f"Entrenador: {entrenador.nombre}, Tiene un {pokemon.nombre}")


# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;

#Lo hice un poco mas complejo de lo que debería porque quería mostrar los que tienen repetidos, como ash
def k():

    entrenador_buscado = input("Ingrese el nombre del entrenador: ")
    pokemon_buscado = input("Ingrese el nombre del Pokémon: ")
    entrenador_encontrado = False

    for i in range(lista_entrenadores.size()): #for de lista principal
        entrenador = lista_entrenadores.get_element_by_index(i)[0]
        sublista_pokemon = lista_entrenadores.get_element_by_index(i)[1]

        if entrenador.nombre == entrenador_buscado:
            print("Datos del entrenador:")
            print(entrenador)
            pokemon_encontrado = False

            for k in range(sublista_pokemon.size()): #for de lista secundaria
                pokemon = sublista_pokemon.get_element_by_index(k)
                if pokemon.nombre == pokemon_buscado:
                    print("Datos del Pokémon:")
                    print(pokemon)
                    pokemon_encontrado = True

            if not pokemon_encontrado:
                print(f"No se encontró al Pokémon '{pokemon_buscado}' para el entrenador '{entrenador_buscado}'.")

            entrenador_encontrado = True

    if not entrenador_encontrado:
        print(f"No se encontró al entrenador '{entrenador_buscado}'.")

while True:
    menu = (
        "\nSeleccione una opción:\n"
        "a. Obtener la cantidad de Pokémons de un determinado entrenador\n"
        "b. Listar los entrenadores que hayan ganado más de tres torneos\n"
        "c. Mostrar el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados\n"
        "d. Mostrar todos los datos de un entrenador y sus Pokémons\n"
        "e. Mostrar los entrenadores cuyo porcentaje de batallas ganadas sea mayor al 79 %\n"
        "f. Mostrar los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo)\n"
        "g. Mostrar el promedio de nivel de los Pokémons de un determinado entrenador\n"
        "h. Determinar cuántos entrenadores tienen a un determinado Pokémon\n"
        "i. Mostrar los entrenadores que tienen Pokémon repetidos\n"
        "j. Determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull\n"
        "k. Determinar si un entrenador tiene un Pokémon y mostrar los datos de ambos\n"
        "q. Salir\n"
        "\n"
    )
    
    print(menu)
    opcion = input("Ingrese la letra de la opción que desea ejecutar (o 'q' para salir): ").lower()

    if opcion == 'a':
        a()
    elif opcion == 'b':
        b()
    elif opcion == 'c':
        c()
    elif opcion == 'd':
        d()
    elif opcion == 'e':
        e()
    elif opcion == 'f':
        f()
    elif opcion == 'g':
        g()
    elif opcion == 'h':
        h()
    elif opcion == 'i':
        i()
    elif opcion == 'j':
        j()
    elif opcion == 'k':
        k()
    elif opcion == 'q':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

    wait_for_key()  # Espera a que el usuario presione una tecla antes de mostrar el menú nuevamente