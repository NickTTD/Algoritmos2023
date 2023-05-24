class Notificacion:
    def __init__(self, app, mensaje, hora):
        self.app = app
        self.mensaje = mensaje
        self.hora = hora

    def get_app(self):
        return self.app

    def get_mensaje(self):
        return self.mensaje

    def get_hora(self):
        return self.hora
    
    def mostrar_notificacion(self):
        print(self.app)
        print(self.mensaje)
        print(self.hora)