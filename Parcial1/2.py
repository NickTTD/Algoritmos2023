from lista import Lista
from Personaje import Personaje
from cola import Cola
#nombreHeroe, nombrePersonaje, grupo, año
DataPersonajes=[]
DataPersonajes.append(Personaje('Capitana Marvel','Carol Danvers', 'Avengers', 1967))
DataPersonajes.append(Personaje('Starlord','Peter Quill', 'Guardianes de la galaxia', 2017))
#DataPersonajes.append(Personaje('Rocket Raccoon','', 'Guardianes de la galaxia', 2017))
DataPersonajes.append(Personaje('Gamora','', 'Guardianes de la galaxia', 2017))
DataPersonajes.append(Personaje('Drax','', 'Guardianes de la galaxia', 2017))
DataPersonajes.append(Personaje('Groot','', 'Guardianes de la galaxia', 2017))
DataPersonajes.append(Personaje('Nebula','', 'Guardianes de la galaxia', 2017))
DataPersonajes.append(Personaje('Sr Fantástico','Reed Richards', 'Los 4 Fantásticos', 1960))
DataPersonajes.append(Personaje('Mujer Invisible','Susan Storm', 'Los 4 Fantásticos', 1960))
DataPersonajes.append(Personaje('Antorcha Humana','Johnny Storm', 'Los 4 Fantásticos', 1960))
DataPersonajes.append(Personaje('Thing','Ben Grimm', 'Los 4 Fantásticos', 1810))
DataPersonajes.append(Personaje('Iron Man','Tony Stark', 'Avengers', 1963))
DataPersonajes.append(Personaje('Quicksilver','Pietro Maximoff', 'Avengers', 1964))
DataPersonajes.append(Personaje('Spiderman','Peter Parker', 'Avengers', 1962))
DataPersonajes.append(Personaje('Spiderman','Miles Morales', 'Avengers', 2011))
DataPersonajes.append(Personaje('Thor','Thor Odinson', 'Avengers', 1962))
DataPersonajes.append(Personaje('Vision','', 'Avengers', 2015))
DataPersonajes.append(Personaje('Dr. Strange','Stephen Strange', 'Avengers', 1974))
DataPersonajes.append(Personaje('Vlanck Widow','Natasha Romanoff', 'Avengers', 1964))
# f. Dada una lista auxiliar con los siguientes personajes (‘Black
# Cat’, ‘Hulk’, ‘Rocket Racoonn’, ‘Loki’, complete el resto de la
# información), agregarlos a la lista principal en el caso de no
# estar cargados.
DataPersonajesExtra=[]
DataPersonajesExtra.append(Personaje('Black Cat','Felicia Hardy', '',1979 ))
DataPersonajesExtra.append(Personaje('Hulk','Bruce Banner', 'Avengers',1960))
DataPersonajesExtra.append(Personaje('Rocket Raccoon','', 'Guardianes de la galaxia', 2017))
DataPersonajesExtra.append(Personaje('Loki','Loki Laufeyson', '', 1949 ))

ListaPersonajes = Lista()
for Personaje in DataPersonajes:
    ListaPersonajes.insert(Personaje, 'nombreHeroe')

colaGuardianes = Cola()

#a. Determinar si “Capitana Marvel” está en la lista y mostrar su
#nombre de personaje;
def a():
    Elemento = ListaPersonajes.search('Capitana Marvel', 'nombreHeroe')
    if Elemento != None:
        print(ListaPersonajes.get_element_by_index(Elemento).nombrePersonaje)
    else:
        print("Capitana Marvel no está en la lista")

# b. Almacenar los superhéroes que pertenezcan al grupo
# “Guardianes de la galaxia” en una cola e indicar cuantos son.

def b():

    contador = 0

    for i in range(ListaPersonajes.size()):
        if ListaPersonajes.get_element_by_index(i).grupo == "Guardianes de la galaxia":
            colaGuardianes.arrive(ListaPersonajes.get_element_by_index(i))
            contador += 1
    print('Hay', contador,' Guardianes de la galaxia, los mismos fueron almacenados en la cola colaGuardianes.')

#c. Mostrar de manera descendente los superhéroes que
#pertenecen al grupo “Los cuatro fantásticos” y “Guardoanes de
#la galaxia”.
def c():
    print("Cola de guardianes:")
    for _ in range(colaGuardianes.size()): #Necesita que se ejecute def B
        PersonajeActual = colaGuardianes.atention()
        print(PersonajeActual)

    print('Los 4 fantásticos:')
    ListaPersonajes.order_by("nombrePersonaje")
    for i in range(ListaPersonajes.size()):
        elemento=ListaPersonajes.get_element_by_index(i)
        if elemento.grupo == "Los 4 Fantásticos":
            print(elemento)
        

#d. Listar los superhéroes que tengan nombre de personajes cuyo
#año de aparición sea posterior a 1960.
def d():
    print("Personajes con nombre y > 1960")
    for i in range(ListaPersonajes.size()):
        elemento=ListaPersonajes.get_element_by_index(i)
        if elemento.nombrePersonaje != "" and elemento.año >1960:
            print(elemento)

# e. Hemos detectado que la superhéroe “Black Widow” está mal
# cargada por un error de tipeo, figura como “Vlanck Widow”,
# modifique dicho superhéroe para solucionar este problema.

def e():
    #ListaPersonajes.barrido() #muestra la lista completa con el error
    Elemento = ListaPersonajes.searchObjeto('Vlanck Widow', 'nombreHeroe')
    if Elemento != None:
        Elemento.nombreHeroe = "Black Widow"
        #ListaPersonajes.barrido() #muestra la lista completa con el error corregido
        print(Elemento)


def f():
    for Personaje in DataPersonajesExtra:
        ListaPersonajes.insert(Personaje, 'nombreHeroe')

#g. Mostrar todos los personajes que comienzan con C, P o S.
def g(): #Lo hice con nombre de heroe(porque todos tienen) y solo mostré el nombre, no todos los datos
    for i in range(ListaPersonajes.size()):
        elemento=ListaPersonajes.get_element_by_index(i)
        if elemento.nombreHeroe[0] in ("C", "P", "S"):
            print(elemento.nombreHeroe)


opcion = input("Elegir punto a ejecutar(A,B,C,D,E,F,G)")
if opcion.upper() == "A": a()
if opcion.upper() == "B": b()
if opcion.upper() == "C": b(), c()
if opcion.upper() == "D": d()
if opcion.upper() == "E": e()
if opcion.upper() == "F": f()
if opcion.upper() == "G": g()