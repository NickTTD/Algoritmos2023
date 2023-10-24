from arbol_binario import BinaryTree
import msvcrt

# Robé esto de internet, solo lo uso en el menu y es para esperar que el usuario presione una tecla antes de volver a mostrar el menu
def wait_for_key():
    print("\nPresione una tecla para continuar...\n -------------------------")
    msvcrt.getch()  

lista_heroes = [
    {'name': 'iron man', 'heroe': True},
    {'name': 'thanos', 'heroe': False},
    {'name': 'capitan america', 'heroe': True},
    {'name': 'red skull', 'heroe': False},
    {'name': 'hulk', 'heroe': True},
    {'name': 'black widow', 'heroe': True},
    {'name': 'rocket raccon', 'heroe': True},
    {'name': 'dotor strage', 'heroe': True},
    {'name': 'doctor octopus', 'heroe': True},
    {'name': 'deadpool', 'heroe': True},
]

arbol = BinaryTree()

for heroe in lista_heroes:
    arbol.insert_node(heroe['name'], heroe['heroe'])

# b. listar los villanos ordenados alfabéticamente;
def B():
    arbol.inorden_super_or_villano(False)

# c. mostrar todos los superhéroes que empiezan con C;
def C():
    arbol.inorden_start_with('C')

# d. determinar cuántos superhéroes hay en el árbol;
def D():
    print(f"Hay {arbol.contar_heroes()} héroes en el árbol")

# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
def E():
    print(arbol.search_by_coincidence('d'))
    value = input('Los anteriores heroes comienzan con D, ¿cuál desea modificar? ')
    pos = arbol.search(value)
    if pos:
        is_hero = pos.other_values
        arbol.delete_node(value)
        new_value = input('Ingrese el nuevo nombre: ')
        arbol.insert_node(new_value, is_hero)
    else:
        print('No está')
    print(arbol.inorden())

# f. listar los superhéroes ordenados de manera descendente;
def F():
    print('Barrido por nivel mostrando solo heroes')
    print(arbol.by_level_heroe())

# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.
def G():
    heroes = BinaryTree()
    villanos = BinaryTree()
    arbol.tree_split(heroes, villanos)

    print("Barrido alfabetico Heroes")
    heroes.inorden()
    print()
    print("Barrido alfabetico Villanos")
    villanos.inorden()



while True:
    menu = (
        "\nSeleccione una opción:\n"
        "a. (No es una opción válida) además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;\n"
        "b. listar los villanos ordenados alfabéticamente;\n"
        "c. mostrar todos los superhéroes que empiezan con C;\n"
        "d. determinar cuántos superhéroes hay el árbol;\n"
        "e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;\n"
        "f. listar los superhéroes ordenados de manera descendente;\n"
        "g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:\n"
        "\n"
    )
    
    print(menu)
    opcion = input("Ingrese la letra de la opción que desea ejecutar (o 'q' para salir): ").lower()

    if opcion == 'b':
        B()
    elif opcion == 'c':
        C()
    elif opcion == 'd':
        D()
    elif opcion == 'e':
        E()
    elif opcion == 'f':
        F()
    elif opcion == 'g':
        G()    
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

    wait_for_key()  # Espera a que el usuario presione una tecla antes de mostrar el menú nuevamente
