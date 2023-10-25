from arbol_binario import BinaryTree
import msvcrt

# Robé esto de internet, solo lo uso en el menu y es para esperar que el usuario presione una tecla antes de volver a mostrar el menu
def wait_for_key():
    print("\nPresione una tecla para continuar...\n -------------------------")
    msvcrt.getch()  

arbol = BinaryTree()


datos = [
    {'name': 'Medusa', 'derrotado': 'Perseo', 'descripcion': 'test'},
    {'name': 'Medusa2', 'derrotado': 'Zeus'},
    {'name': 'Tifon', 'derrotado': 'Zeus'},
    {'name': 'Leon Nimea', 'derrotado': 'Heracles'},
    {'name': 'Hydra de Lerna', 'derrotado': None, 'descripcion': 'serpiente acuática con múltiples cabezas'},
    {'name': 'Otro', 'derrotado': 'Heracles'},
    {'name': 'Ceto', 'derrotado': None, 'descripcion': 'antigua diosa del mar'},
    {'name': 'Toro de Creta', 'derrotado': None, 'descripcion': 'toro mítico enviado por Poseidón'},
    {'name': 'Cierva Cerinea', 'derrotado': None, 'descripcion': 'cierva de Ceryneia'},
    {'name': 'Jabalí de Erimanto', 'derrotado': None, 'descripcion': 'jabalí salvaje'},
    {'name': 'Ceto2', 'derrotado': 'Apolo'},
    {'name': 'Ceto3', 'derrotado': 'Apolo'},
    {'name': 'Basilisco'},
    {'name': 'Sirenas'},
    {'name': 'Aves de Estínfalo 1'},
    {'name': 'Aves de Estínfalo 2'},
    {'name': 'Aves de Estínfalo 3'},
    {'name': 'Ladón'},
    {'name': 'Talos', 'derrotado': 'Medea', 'descripcion': 'autómata gigante hecho de bronce que protegía a la Creta minoica de piratas e invasores'}
]

for criatura in datos:
    derrotado = criatura.get('derrotado', None)     #Si no tiene derrotado en el diccionario, se le setea en none
    descripcion = criatura.get('descripcion', None) #Si no hay descripción en los datos, se le asigna none al .other_values[descripción]
    arbol.insert_node(criatura['name'], {'derrotado': derrotado, 'descripcion': descripcion})


#a. listado inorden de las criaturas y quienes la derrotaron;
def A():
    arbol.inorden_criaturas()

#b. se debe permitir cargar una breve descripción sobre cada criatura;
def B(): #No se si interpreté bien esta consigna, pero...
    arbol.inorden_criaturas()
    value = input('Ingrese el nombre de la criatura a modificar')
    pos = arbol.search(value)
    if pos:
        nueva_descripcion = input('Ingrese la nueva descripción: ')
        pos.other_values['descripcion'] = nueva_descripcion
        arbol.mostrar_criatura(pos) #Originalmente mostraba el arbol entero, pero esta función la hice para el C así que cambié a esto
    else:
        print('No está')

#c. mostrar toda la información de la criatura Talos;
def C():
    pos = arbol.search('Talos')
    arbol.mostrar_criatura(pos)

#d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
def D():
    dic_ranking = {}
    arbol.inorden_ranking(dic_ranking)

    #print(dic_ranking)


    def order_por(item):
        #print(item)
        return item[1]

    ordenados = list(dic_ranking.items())
    ordenados.sort(key=order_por, reverse=True)
    print(ordenados[:3])


#e. listar las criaturas derrotadas por Heracles;
def E():
    arbol.inorden_derrotado_por_heroe('Heracles')

#f. listar las criaturas que no han sido derrotadas;
def F():
    arbol.inorden_derrotado_por_heroe(None)


#g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
#o dios que la capturo;
#Supongo que se refiere a agregar other values mientras lo ejecuto
# sin embargo, si quisiera por ejemplo agregarle edad a Talos,
#En este punto terminé creando las funciones get_node_info (Genérica, para mostrar todos los valores de un diccionario en other values)
#y search_print_node
def G():
    pos = arbol.search('Talos')
    arbol.print_node(pos)
    pos.other_values['edad'] = '3500'
    arbol.search_print_node('Talos') # Puedo hacer arbol.print_node(pos), pero quería probar mi función nueva. >:)


#h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
#Erimanto indicando que Heracles las atrapó;
def H():
    criaturas_a_capturar = ['Cerbero', 'Toro de Creta', 'Cierva Cerinea', 'Jabalí de Erimanto']
    arbol.inorden_criaturas()

    for criatura_nombre in criaturas_a_capturar:
        criatura = arbol.search(criatura_nombre)
        if criatura:
            criatura.other_values['derrotado'] = 'Heracles'
    print()
    arbol.inorden_criaturas()
#i. se debe permitir búsquedas por coincidencia;
def I():
    buscado = input('Ingrese la busqueda por coincidencia a realizar: ')
    arbol.search_by_coincidence(buscado)

#.J eliminar al Basilisco y a las Sirenas;
def J():
    arbol.inorden()
    pos = arbol.search('Sirenas')
    arbol.delete_node(pos.value)
    pos = arbol.search('Basilisco')
    arbol.delete_node(pos.value)
    print()
    arbol.inorden()


#k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
#derroto a varias;
#Como tengo varios nodos ennumerados, terminé haciendo la función get nodes starting with, que es una modificación de la
#busqueda por coincidencia pero te devuelve una lista
def K():
    arbol.search_by_coincidence('Aves')
    matching_nodes = arbol.get_nodes_starting_with('Aves')
    for node in matching_nodes:
     node.other_values['derrotado'] = 'Heracles'
    print()
    arbol.search_by_coincidence('Aves')


#l. modifique el nombre de la criatura Ladón por Dragón Ladón;
def L():
    arbol.inorden()
    pos = arbol.search('Ladón')
    if pos:
        pos.value = 'Dragón Ladón'
        arbol.search_print_node('Dragón Ladón')
    else:
        print('Criatura no encontrada en el árbol.')
    arbol.mostrar_criatura(pos)

def M():
    arbol.by_level()

#n. muestre las criaturas capturadas por Heracles.
#Repetido del E?

while True:
    menu = (
        "\nSeleccione una opción:\n"
        "a. listado inorden de las criaturas y quienes las derrotaron;\n"
        "b. permitir cargar una breve descripción sobre cada criatura;\n"
        "c. mostrar toda la información de la criatura Talos;\n"
        "d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;\n"
        "e. listar las criaturas derrotadas por Heracles;\n"
        "f. listar las criaturas que no han sido derrotadas;\n"
        "g. cada nodo debe tener un campo 'capturada' que almacene el nombre del héroe o dios que la capturó;\n"
        "h. modificar los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;\n"
        "i. permitir búsquedas por coincidencia;\n"
        "j. eliminar al Basilisco y a las Sirenas;\n"
        "k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derrotó a varias;\n"
        "l. modificar el nombre de la criatura Ladón por Dragón Ladón;\n"
        "m. mostrar el árbol por niveles;\n"
    )
    
    print(menu)
    opcion = input("Ingrese la letra de la opción que desea ejecutar (o 'q' para salir): ").lower()

    if opcion == 'a':
        A()
    elif opcion == 'b':
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
    elif opcion == 'h':
        H()
    elif opcion == 'i':
        I()
    elif opcion == 'j':
        J()
    elif opcion == 'k':
        K()
    elif opcion == 'l':
        L()
    elif opcion == 'm':
        M()
    elif opcion == 'q':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

    wait_for_key()  # Espera a que el usuario presione una tecla antes de mostrar el menú nuevamente
