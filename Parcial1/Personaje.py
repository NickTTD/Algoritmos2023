#Dada una lista con nombres de personajes de la saga de Avengers
# ordenados por nombre del superhéroes, de los cuales se conoce:
# nombre del superhéroe, nombre del personaje (puede ser vacio),
# grupo al que (perteneces puede ser vacio), año de aparición, por
# ejemplo (Star Lord – Peter Quill – Guardianes de la galaxia - 1976).
# Resolver las siguientes tareas:
class Personaje:
    def __init__(self,nombreHeroe, nombrePersonaje, grupo, año):
        self.nombreHeroe = nombreHeroe
        self.nombrePersonaje = nombrePersonaje
        self.grupo = grupo
        self.año = año

    def __str__(self):
        separador = "-" * 20
        return f"Personaje: {self.nombrePersonaje}\nHéroe: {self.nombreHeroe}\nGrupo: {self.grupo}\nAño: {self.año}\n{separador}"