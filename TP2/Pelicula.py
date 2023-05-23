class Pelicula:
    def __init__(self, titulo, estudio, año_estreno):
        self.titulo = titulo
        self.estudio = estudio
        self.año_estreno = año_estreno

    def get_titulo(self):
        return self.titulo

    def get_estudio(self):
        return self.estudio

    def get_año_estreno(self):
        return self.año_estreno
    
    #Los setters no se usan pero los dejé igual porque estaba practicando objetos 
    # def set_titulo(self, nuevo_titulo):
    #     self.titulo = nuevo_titulo

    # def set_estudio(self, nuevo_estudio):
    #     self.estudio = nuevo_estudio

    # def set_año_estreno(self, nuevo_año_estreno):
    #     self.año_estreno = nuevo_año_estreno
