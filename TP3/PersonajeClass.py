class Personaje:
    def __init__(self, nombrePersonaje, nombreHeroe, genero):
        self.nombrePersonaje = nombrePersonaje
        self.nombreHeroe = nombreHeroe
        self.genero = genero

    def get_nombrePersonaje(self):
        return self.nombrePersonaje

    def get_nombreHeroe(self):
        return self.nombreHeroe

    def get_genero(self):
        return self.genero
    
    def mostrar_personaje(self):
        print(self.nombrePersonaje, "-",self.nombreHeroe, "-",self.genero)