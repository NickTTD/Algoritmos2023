from cola import Cola
from PersonajeClass import Personaje
from copy import deepcopy
# Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
# ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino

# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
# manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

ListaPersonajes=[] #(Esta vez lo hice con una lista para no tener que agregar manualmente a la cola)
ListaPersonajes.append(Personaje("Tony Stark","Iron Man","M"))
ListaPersonajes.append(Personaje("Miles Morales","Spiderman","M"))
ListaPersonajes.append(Personaje("Carol Danvers","Captain Marvel","F"))
ListaPersonajes.append(Personaje("Black Widow","Natasha Romanoff","F"))
ListaPersonajes.append(Personaje("Scott Lang","Ant-man","M"))

ColaPersonajes = Cola()

for Personaje in ListaPersonajes:
    ColaPersonajes.arrive(Personaje)

#Para mostrar la cola original:
# for Personaje in ListaPersonajes:
#     PersonajeActual = Personajes.atention()
#     PersonajeActual.mostrar_personaje()
print("----------")
print("a. determinar el nombre del personaje de la superhéroe Capitana Marvel;")
ColaPersonajes_A = deepcopy(ColaPersonajes)

for _ in range(ColaPersonajes_A.size()):
     PersonajeActual = ColaPersonajes_A.atention()
     if PersonajeActual.get_nombreHeroe() == "Captain Marvel":
            print("Capitana Marvel está en la cola, su nombre es: ",PersonajeActual.get_nombrePersonaje())



print("----------")
print("b. mostrar los nombre de los superhéroes femeninos;")
ColaPersonajes_B = deepcopy(ColaPersonajes)

for _ in range(ColaPersonajes_B.size()):
     PersonajeActual = ColaPersonajes_B.atention()
     if PersonajeActual.get_genero() == "F":
            print(PersonajeActual.get_nombrePersonaje());




print("----------")
print("c. mostrar los nombres de los personajes masculinos;")
ColaPersonajes_C = deepcopy(ColaPersonajes)

for _ in range(ColaPersonajes_C.size()):
     PersonajeActual = ColaPersonajes_C.atention()
     if PersonajeActual.get_genero() == "M":
            print(PersonajeActual.get_nombrePersonaje());



print("----------")
print("d. determinar el nombre del superhéroe del personaje Scott Lang;")
ColaPersonajes_D = deepcopy(ColaPersonajes)

for _ in range(ColaPersonajes_D.size()):
     PersonajeActual = ColaPersonajes_D.atention()
     if PersonajeActual.get_nombrePersonaje() == "Scott Lang":
            print("Scott Lang está en la cola, su supernombre es:",PersonajeActual.get_nombreHeroe())


print("----------")
print("e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;")
ColaPersonajes_E = deepcopy(ColaPersonajes)

for _ in range(ColaPersonajes_E.size()):
     PersonajeActual = ColaPersonajes_E.atention()
     if PersonajeActual.get_nombrePersonaje()[0] == "S" or PersonajeActual.get_nombreHeroe()[0] == "S":
            PersonajeActual.mostrar_personaje()



print("----------")
print("f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.")
ColaPersonajes_F = deepcopy(ColaPersonajes)
#No es igual que el A y el D?

for _ in range(ColaPersonajes_F.size()):
     PersonajeActual = ColaPersonajes_F.atention()
     if PersonajeActual.get_nombrePersonaje() == "Carol Danvers":
            print("Carol Danvers está en la cola, su supernombre es:",PersonajeActual.get_nombreHeroe())