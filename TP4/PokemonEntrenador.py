class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        separador = "-" * 20
        return f"{separador}\nNombre: {self.nombre}\nNivel: {self.nivel}\nTipo: {self.tipo}\nSubtipo: {self.subtipo}\n{separador}"

class EntrenadorPokemon:
    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas

    def __str__(self):
        separador = "-" * 20
        return f"{separador}\n ENTRENADOR \nNombre: {self.nombre}\nTorneos Ganados: {self.torneos_ganados}\nBatallas Perdidas: {self.batallas_perdidas}\nBatallas Ganadas: {self.batallas_ganadas}\n{separador}"