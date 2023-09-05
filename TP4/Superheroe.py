# Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,

# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
# rias para poder realizar las siguientes actividades:
class Superheroe:
    def __init__(self, nombre, añoAparicion, casaComic, biografia):
        self.nombre = nombre
        self.añoAparicion = añoAparicion
        self.casaComic = casaComic
        self.biografia = biografia

    def __str__(self):
        separador = "-" * 20
        return f"Nombre: {self.nombre}\nAño de Aparición: {self.añoAparicion}\nCasa de Cómics: {self.casaComic}\nBiografía: {self.biografia}\n{separador}"