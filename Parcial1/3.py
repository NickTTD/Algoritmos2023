# 3. Se recuperó la bitácora de la nave del cazarrecompensas Boba Fett, la
# cual se almacenaban en una pila en cada misión de caza que
# emprendió (con la siguiente información planeta visitado, a quien
# capturado, costo de la recompensa), resolver las siguientes
# actividades:

from pila import Pila
from Mision import Mision
ListaMisiones=[]
ListaMisiones.append(Mision("Tatooine","Luke Skywalker",1000))
ListaMisiones.append(Mision("Tatooine","Jabba the Hutt",300))
ListaMisiones.append(Mision("Lothal","Kanan Jarrus",1000))
ListaMisiones.append(Mision("Death Star II","Darth Vader",5000))
ListaMisiones.append(Mision("Illum","Han Solo",1500))

PilaMisiones = Pila()
for Mision in ListaMisiones:
    PilaMisiones.push(Mision)

# for _ in range(PilaMisiones.size()):
#     elemento = PilaMisiones.pop()
#     print(elemento)

#a. Mostrar los planetas visitados en el orden hizo las misiones.
def a():
    print("Cola en orden descendente")
    PilaMisiones.invert()
    while PilaMisiones.size() > 0:
        elemento = PilaMisiones.pop()
        print(elemento)



#b. Determinar cuántos créditos galácticos recaudo en total.
def b():
    contador = 0
    while PilaMisiones.size() > 0:
        elemento = PilaMisiones.pop()
        print(elemento)
        contador += elemento.Recompensa
    print("Total recaudado:", contador)

#c. Determinar el número de la misión en que capturo a Han Solo
#y en que planeta fue, suponga que dicha misión está cargada.
def c():
    PilaMisiones.invert()
    for i in range(PilaMisiones.size()):
        elemento = PilaMisiones.pop()
        if elemento.Capturado == "Han Solo":
            print("Han Solo fue capturado en la misión",i+1,"En el planeta", elemento.Planeta)

opcion = input("Elegir punto a ejecutar(A,B,C)")
if opcion.upper() == "A": a()
if opcion.upper() == "B": b()
if opcion.upper() == "C": c()

