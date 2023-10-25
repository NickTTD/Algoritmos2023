from arbol_binario import BinaryTree, get_value_from_file
import msvcrt

# Robé esto de internet, solo lo uso en el menu y es para esperar que el usuario presione una tecla antes de volver a mostrar el menu
def wait_for_key():
    print("\nPresione una tecla para continuar...\n -------------------------")
    msvcrt.getch() 
file_jedi = open('jedis.txt')
read_lines = file_jedi.readlines()
file_jedi.close()

#a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
name_tree = BinaryTree()
specie_tree = BinaryTree()
ranking_tree = BinaryTree()

read_lines.pop(0)
for index, linea_jedi in enumerate(read_lines):
    jedi = linea_jedi.split(';')
    jedi.pop() 
    name_tree.insert_node(jedi[0], index+2)
    specie_tree.insert_node(jedi[2], index+2)
    ranking_tree.insert_node(jedi[1], index+2)

#b. realizar un barrido inorden del árbol por nombre y ranking;
def b():
    name_tree.inorden()
    print()
    ranking_tree.inorden_file('jedis.txt')

#c. realizar un barrido por nivel de los árboles por ranking y especie;
def c():
    print("------------>Ranking por nivel<-----------")
    ranking_tree.by_level_file("jedis.txt")
    print("------------>Especie por nivel<-----------")
    specie_tree.by_level_file("jedis.txt")



#d. mostrar toda la información de Yoda y Luke Skywalker;
def d():
    pos = name_tree.search('yoda')
    if pos:
        print(get_value_from_file('jedis.txt', pos.other_values))
    else:
        print('no esta en la lista')

    pos = None
    pos = name_tree.search('luke skywalker')
    if pos:
        print(get_value_from_file('jedis.txt', pos.other_values))
    else:
        print('no esta en la lista')


#e. mostrar todos los Jedi con ranking “Jedi Master”;
def e():
    name_tree.inorden_file_jedi_master('jedis.txt', 'jedi master')

#f. listar todos los Jedi que utilizaron sabe de luz color verde;
def f():
    name_tree.inorden_file_lightsaber('jedis.txt', 'green')

#g. listar todos los Jedi cuyos maestros están en el archivo;    
def g():
    name_tree.inorden_file_master('jedis.txt')

#h. h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
def h():
    name_tree.inorden_file_species('jedis.txt', 'togruta')
    name_tree.inorden_file_species('jedis.txt', 'cerean')

#i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.
def i():
    name_tree.inorden_start_with_jedi('A')
    name_tree.inorden_in_jedi('-')


while True:
    menu = (
        "\nSeleccione una opción:\n"
        "b. #b. realizar un barrido inorden del árbol por nombre y ranking\n"
        "c. Realizar un barrido por nivel de los árboles por ranking y especie;\n"
        "d. Mostrar toda la información de Yoda y Luke Skywalker\n"
        "e. Mostrar todos los Jedi con ranking “Jedi Master”\n"
        "f. Listar todos los Jedi que utilizaron sabe de luz color verde;\n"
        "g. Listar todos los Jedi cuyos maestros están en el archivo';\n"
        "h. Mostrar todos los Jedi de especie “Togruta” o “Cerean;\n"
        "i. Listar los Jedi que comienzan con la letra A y los que contienen un '-';\n"
        "q. Salir"
    )

    print(menu)
    opcion = input("Ingrese la letra de la opción que desea ejecutar (o 'q' para salir): ").lower()

    if opcion == 'b':
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
    elif opcion == 'q':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

    wait_for_key()  # Espera a que el usuario presione una tecla antes de mostrar el menú nuevamente