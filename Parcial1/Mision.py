# 3. Se recuperó la bitácora de la nave del cazarrecompensas Boba Fett, la
# cual se almacenaban en una pila en cada misión de caza que
# emprendió (con la siguiente información planeta visitado, a quien
# capturado, costo de la recompensa), resolver las siguientes
# actividades:

class Mision:
    def __init__(self,Planeta, Capturado, Recompensa):
        self.Planeta = Planeta
        self.Capturado = Capturado
        self.Recompensa = Recompensa
        
    def __str__(self):
        separador = " | "
        return f"Planeta: {self.Planeta}{separador}Capturado: {self.Capturado}{separador}Recompensa: {self.Recompensa}"