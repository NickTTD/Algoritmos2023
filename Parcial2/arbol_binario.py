from cola import Cola
import linecache


def get_value_from_file(file_name, index):
    line = linecache.getline(file_name, index)
    line_split = line.split(';')
    line_split.pop()
    return line_split

class NodeTree():

    def __init__(self, value, other_values=None):
        self.value = value
        self.other_values = other_values
        self.left = None
        self.right = None
        self.height = 0


class BinaryTree:

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height > right_height else right_height) + 1

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def balancing(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def insert_node(self, value, other_values=None):

        def __insertar(root, value, other_values):
            if root is None:
                return NodeTree(value, other_values)
            elif value < root.value:
                root.left = __insertar(root.left, value, other_values)
            else:
                root.right = __insertar(root.right, value, other_values)
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insertar(self.root, value, other_values)

    def by_level(self):
        if self.root is not None:
            cola_tree = Cola()
            cola_tree.arrive(self.root)
            while cola_tree.size() > 0:
                node = cola_tree.atention()
                print(node.value)
                # a = input()
                if node.left is not None:
                    cola_tree.arrive(node.left)
                if node.right is not None:
                    cola_tree.arrive(node.right)

    def by_level_file(self, file_name):
        if self.root is not None:
            cola_tree = Cola()
            cola_tree.arrive(self.root)
            while cola_tree.size() > 0:
                node = cola_tree.atention()
                value = get_value_from_file(file_name, node.other_values)
                print(node.value, value[0])

                if node.left is not None:
                    cola_tree.arrive(node.left)
                if node.right is not None:
                    cola_tree.arrive(node.right)
                    
    def by_level_heroe(self):
        if self.root is not None:
            cola_tree = Cola()
            if self.root.other_values is True:
                cola_tree.arrive(self.root)
            while cola_tree.size() > 0:
                node = cola_tree.atention()
                if node.other_values is True:  # Verifica si es un héroe antes de imprimir
                    print(node.value)
                if node.left is not None:
                    cola_tree.arrive(node.left)
                if node.right is not None:
                    cola_tree.arrive(node.right)

    def inorden_super_or_villano(self, is_hero):
        def __inorden_s_v(root, is_hero):
            if root is not None:
                __inorden_s_v(root.left, is_hero)
                if root.other_values is is_hero:
                    print(root.value)
                __inorden_s_v(root.right, is_hero)

        __inorden_s_v(self.root, is_hero)

    

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        __inorden(self.root)

    def inorden_pokemon(self, tipo):
        def __inorden_pokemon(root, tipo):
            if root is not None:
                __inorden_pokemon(root.left, tipo)
                if tipo in root.value:
                    print(root.other_values['name'])
                __inorden_pokemon(root.right, tipo)

        __inorden_pokemon(self.root, tipo)


    def inorden_ranking(self, ranking):
        def __inorden_ranking(root, ranking):
            if root is not None:
                __inorden_ranking(root.left, ranking)
                if root.other_values['derrotado'] is not None:
                    if root.other_values['derrotado'] not in ranking:
                        ranking[root.other_values['derrotado']] = 1
                    else:
                        ranking[root.other_values['derrotado']] += 1
                __inorden_ranking(root.right, ranking)

        __inorden_ranking(self.root, ranking)

    def inorden_add_field(self):
        def __inorden_add_field(root):
            if root is not None:
                __inorden_add_field(root.left)
                root.other_values['capturado'] = None
                __inorden_add_field(root.right)

        __inorden_add_field(self.root)

    def inorden_file(self, file_name):
        def __inorden_file(root, file_name):
            if root is not None:
                __inorden_file(root.left, file_name)
                value = get_value_from_file(file_name, root.other_values)
                print(root.value, value[0])
                __inorden_file(root.right, file_name)

        __inorden_file(self.root, file_name)

    def inorden_file_lightsaber(self, file_name, lightsaber_color):
        def __inorden_file_lightsaber(root, file_name, lightsaber_color):
            if root is not None:
                __inorden_file_lightsaber(root.left, file_name, lightsaber_color)
                value = get_value_from_file(file_name, root.other_values)
                if lightsaber_color in value[4].split('/'):
                    print(root.value, value[4].split('/'))
                __inorden_file_lightsaber(root.right, file_name, lightsaber_color)

        __inorden_file_lightsaber(self.root, file_name, lightsaber_color)

    def inorden_file_jedi_master(self, file_name, rank):
        def __inorden_file_jedi_master(root, file_name, rank):
            if root is not None:
                __inorden_file_jedi_master(root.left, file_name, rank)
                value = get_value_from_file(file_name, root.other_values)
                if value[1] == rank:
                    print(root.value, value[1])
                __inorden_file_jedi_master(root.right, file_name, rank)

        __inorden_file_jedi_master(self.root, file_name, rank)

    def inorden_file_species(self, file_name, species):
        def __inorden_file_species(root, file_name, species):
            if root is not None:
                __inorden_file_species(root.left, file_name, species)
                value = get_value_from_file(file_name, root.other_values)
                if value[2] == species:
                    print(root.value, value[2])
                __inorden_file_species(root.right, file_name, species)

        __inorden_file_species(self.root, file_name, species)

    def inorden_file_master(self, file_name):
        def __inorden_file_master(root, file_name):
            if root is not None:
                __inorden_file_master(root.left, file_name)
                value = get_value_from_file(file_name, root.other_values)
                if value[3] != "-":
                    print(root.value, value[3].split('/'))
                __inorden_file_master(root.right, file_name)

        __inorden_file_master(self.root, file_name)

    def inorden_super_or_villano(self, is_hero):
        def __inorden_s_v(root, is_hero):
            if root is not None:
                __inorden_s_v(root.left, is_hero)
                if root.other_values is is_hero:
                    print(root.value)
                __inorden_s_v(root.right, is_hero)

        __inorden_s_v(self.root, is_hero)

    def inorden_start_with(self, cadena):
        def __inorden_start_with(root, cadena):
            if root is not None:
                __inorden_start_with(root.left, cadena)
                if root.other_values is True and root.value.upper().startswith(cadena):
                    print(root.value)
                __inorden_start_with(root.right, cadena)

        __inorden_start_with(self.root, cadena)

    def inorden_in_jedi(self, cadena): #Probablemente mal nombre, busca caracteres en el string del root
        def __inorden_in_jedi(root, cadena):
            if root is not None:
                __inorden_in_jedi(root.left, cadena)
                if cadena in root.value.upper():
                    print(root.value)
                __inorden_in_jedi(root.right, cadena)

        __inorden_in_jedi(self.root, cadena)

    #Quería practicar usar descripciones de funciones, así que...
    # La función mostrar_criatura la usé originalmente para mostrar toda la información de una criatura, pero aprendí como
    #hacerlo genérico, e implementé la función "print node", sin embargo no borré esto porque quedó a modo de explicación de como llegué a lo otro
    def mostrar_criatura(self, node):
        """
        Muestra la información de una criatura, incluyendo su nombre, quién la derrotó y la descripción.
        Debería ser usada luego de un Search, o una función que devuelva un nodo del árbol

        Parámetros:
        - node (NodeTree): El nodo que representa la criatura en el árbol.
        """
        print(f'Nombre: {node.value}| Derrotado por: {node.other_values["derrotado"]}| Descripción: {node.other_values.get("descripcion", "Sin descripción")}')

    def print_node(self, node):
        """
        Muestra todos los valores en other_values de un nodo, soporta diccionarios y other values de tipos de datos simples

        Parámetros:
        - node (NodeTree): El nodo que se va a mostrar.
        """
        print('-----')
        print(node.value)
        
        # Verificar si other_values es un diccionario
        if isinstance(node.other_values, dict):
            for key, value in node.other_values.items():
                print(f'{key}: {value}')
        else:
            print(f'other_values: {node.other_values}')

    def search_print_node(self, key):
        """
        Busca un nodo en el árbol por la clave dada y muestra el nombre del nodo y los other values, si se encuentra.

        Parámetros:
        - key (str): La clave del nodo que se va a buscar y mostrar.
        """
        pos = self.search(key)
        if pos:
            self.print_node(pos)
        else:
            print(f'Nodo con clave {key} no encontrado en el árbol.')

    
    def inorden_criaturas(self):
        def __inorden_criaturas(root):
            if root is not None:
                __inorden_criaturas(root.left)
                self.mostrar_criatura(root)
                __inorden_criaturas(root.right)

        __inorden_criaturas(self.root)

    def inorden_derrotado_por_heroe(self, heroe):
        def __inorden_derrotado(root, heroe):
            if root is not None:
                __inorden_derrotado(root.left, heroe)

                if root.other_values['derrotado'] == heroe:
                    self.mostrar_criatura(root)

                __inorden_derrotado(root.right, heroe)

        __inorden_derrotado(self.root, heroe)

                
    def nodetorden(self):
        def __nodetorden(root):
            if root is not None:
                __nodetorden(root.right)
                print(root.value)
                __nodetorden(root.left)

        __nodetorden(self.root)

    def nodetorden_pokemon(self):
        def __nodetorden_pokemon(root):
            if root is not None:
                __nodetorden_pokemon(root.right)
                print(root.value, root.other_values['name'])
                __nodetorden_pokemon(root.left)

        __nodetorden_pokemon(self.root)

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value, root.height)
                __preorden(root.left)
                __preorden(root.right)

        __preorden(self.root)

    def search_by_coincidence(self, value):
        def __search_by_coincidence(root, value):
            if root is not None:
                if root.value.startswith(value):
                    #print(root.value)                     #Solo printear el nombre del nodo
                    self.print_node(root)                  #Printear toda la info del nodo
                __search_by_coincidence(root.left, value)
                __search_by_coincidence(root.right, value)

        __search_by_coincidence(self.root, value)
    def get_nodes_starting_with(self, value):
        """
        Obtiene nodos cuyos nombres comienzan con el valor dado.

        Parámetros:
        - value (str): El valor con el cual comparar el inicio del nombre de los nodos.

        Retorna:
        - list: Lista de nodos encontrados.
        """
        matching_nodes = []

        def __get_nodes_starting_with(root, value):
            if root is not None:
                if root.value.startswith(value):
                    matching_nodes.append(root)
                __get_nodes_starting_with(root.left, value)
                __get_nodes_starting_with(root.right, value)

        __get_nodes_starting_with(self.root, value)
        
        return matching_nodes

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)

        return __search(self.root, key)

    def delete_node(self, key):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
            return root, replace_node

        def __delete(root, key):
            value = None
            if root is not None:
                if key < root.value:
                    root.left, value = __delete(root.left, key)
                elif key > root.value:
                    root.right, value = __delete(root.right, key)
                else:
                    value = root.value
                    if root.left is None and root.right is not None:
                        return root.right, value
                    elif root.right is None and root.left is not None:
                        return root.left, value
                    elif root.left is None and root.right is None:
                        return None, value
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                    root = self.balancing(root)
                    self.update_height(root)
            return root, value

        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, key)
        return delete_value

    def contar(self, value):
        def __contar(root, value):
            count = 0
            if root is not None:
                if root.value == value:
                    count = 1
                count += __contar(root.left, value)
                count += __contar(root.right, value)
            return count

        return __contar(self.root, value)
    
    def contar_heroes(self):
        def __contar_heroes(root):
            count = 0
            if root is not None:
                if root.other_values is True:
                    count = 1
                count += __contar_heroes(root.left)
                count += __contar_heroes(root.right)
            return count

        return __contar_heroes(self.root)
    
    def tree_split(self, Arbol_A, Arbol_B):
        def __preorden(root, Arbol_A, Arbol_B):
            if root is not None:
                if root.other_values is True:
                    Arbol_A.insert_node(root.value, root.other_values)
                else:
                    Arbol_B.insert_node(root.value, root.other_values)
                
                __preorden(root.left, Arbol_A, Arbol_B)
                __preorden(root.right, Arbol_A, Arbol_B)

        __preorden(self.root, Arbol_A, Arbol_B)

# arbol = BinaryTree()

# for i in range(15):
#     arbol.insert_node(name, {'derrotado_por': derrotado})


# node.other_values['capurado_por'] = 'asdas'
# arbol.preorden()

# arbol.root = arbol.balancing(arbol.root)



# print(arbol.root)
# arbol.insert_node('F')
# arbol.insert_node('B')
# # arbol.insert_node('E')
# arbol.insert_node('K')
# arbol.insert_node('H')
# arbol.insert_node('J')
# arbol.insert_node('I')
# arbol.insert_node('R')

# arbol.preorden()

# print()
# deleted = arbol.delete_node('F')
# # if deleted:
# #     print('el valor fue eliminado', deleted)
# # print()
# arbol.preorden()
# deleted = arbol.delete_node('Z')
# print()
# arbol.preorden()
# deleted = arbol.delete_node('K')
# print()
# arbol.preorden()


# print()
# node = arbol.search('Z')
# print(node)
# if node:
#     print('valor encontrado', node.value)