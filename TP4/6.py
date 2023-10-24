from Superheroe import Superheroe
from lista import Lista
#nombre, añoAparicion, casaComic, biografia


DataPersonajes=[] #(Esta vez lo hice con una lista para no tener que agregar manualmente a la cola)
DataPersonajes.append(Superheroe('Tony Stark', 1968, 'Marvel','Hijo de Howard stark, portador del traje...'))
DataPersonajes.append(Superheroe('Linterna Verde', 1940, 'DC','Protagonista de la peor película de DC...'))
DataPersonajes.append(Superheroe('Dr. Strange', 1974, 'DC','El hechicero supremo, nacido en NY...'))
DataPersonajes.append(Superheroe('Capitana Marvel', 1967, 'Marvel','Hija de Mari-Ell y Joe Danvers'))
DataPersonajes.append(Superheroe('Mujer Maravilla', 1941, 'DC','Tiene armadura, Diana of Themyscira is an Amazon warrior...'))
DataPersonajes.append(Superheroe('Flash', 1940, 'DC','Barry Allen, is the fastest man alive, and the second speedster to be called the Flash'))
DataPersonajes.append(Superheroe('Starlord', 2014, 'Marvel','Peter Jason Quill is a Celestial-Human hybrid wh...'))
DataPersonajes.append(Superheroe('Wolverine', 1974, 'Marvel','Wolveeeeeerine'))

ListaPersonajes = Lista()
for Superheroe in DataPersonajes:
    ListaPersonajes.insert(Superheroe, 'nombre')


def mostrarOriginal():
    ListaPersonajes.barrido()

#a. eliminar el nodo que contiene la información de Linterna Verde;
def a():
    ListaPersonajes.delete('Linterna Verde', 'nombre')
    ListaPersonajes.barrido()


#b. mostrar el año de aparición de Wolverine;
# def b():
#     try:
#         print(ListaPersonajes.searchObjeto('Wolverine', 'nombre').get_año_aparicion())
#     except:
#         print("No se encontró a Wolverine")
# b()

#No se muy bien por qué quise hacerlo usando 1 sola linea de código, terminé creando el método busqueda por objeto
#y aprendiendo un poco como sobre funcionan las excepciones, de todas formas acá está resuelto de manera correcta:

def b():
    Elemento = ListaPersonajes.search('Wolverine', 'nombre')
    if Elemento != None:
        print(ListaPersonajes.get_element_by_index(Elemento).añoAparicion)
    else:
        print("Wolverine no está en la lista")

ListaPersonajes.barrido()
#c. cambiar la casa de Dr. Strange a Marvel;
def c():
    Elemento = ListaPersonajes.search('Dr. Strange', 'nombre')
    if Elemento != None:
        ListaPersonajes.get_element_by_index(Elemento).casaComic = "Marvel"
        ListaPersonajes.barrido()
    else:
        print("DrStrange no está en la lista")

#d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
#“traje” o “armadura”;
def d():
    for i in range(ListaPersonajes.size()):
        Bio = ListaPersonajes.get_element_by_index(i).biografia
        if "traje" in Bio or "armadura" in Bio:
            print(Bio)

# mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;
def d():
    
