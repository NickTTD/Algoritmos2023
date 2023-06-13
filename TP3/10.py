# Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades
from cola import Cola
from NotificacionesClass import Notificacion
from copy import deepcopy
from datetime import datetime

Noti1 = Notificacion("Twitter","Python es un gran lenguaje de programación","20:39")
Noti2 = Notificacion("Facebook","Mensaje de facebook","14:30")
Noti3 = Notificacion("Reddit","Reeeeeeeeee","23:39")
Noti4 = Notificacion("Instagram","Respondió una historia ","3:30")
Noti5 = Notificacion("Twitter","Python goated","4:20")
Noti6 = Notificacion("Tumblr","Average tumblr post","11:45")

Notificaciones = Cola()
Notificaciones.arrive(Noti1)
Notificaciones.arrive(Noti2)
Notificaciones.arrive(Noti3)
Notificaciones.arrive(Noti4)
Notificaciones.arrive(Noti5)
Notificaciones.arrive(Noti6)

#a. escribir una función que elimine de la cola todas las notificaciones de Facebook;

def EliminarFB(Cola):
    for _ in range(Cola.size()):
        if Cola.on_front().get_app() == "Facebook":
            Cola.atention()
        else:
            Cola.move_to_end()

#Este código muestra la cola con la notif de fb:
# Notificaciones_A = deepcopy(Notificaciones)
# for i in range(Notificaciones.size()):
#     print("----------")
#     Notificaciones_A.on_front().mostrar_notificacion()
#     Notificaciones_A.atention()

print('----------Sin notif de fb------------')
Notificaciones_A = deepcopy(Notificaciones)
EliminarFB(Notificaciones_A)
for i in range(Notificaciones_A.size()):
    print("----------")
    Notificaciones_A.on_front().mostrar_notificacion()
    Notificaciones_A.atention()

#b escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
#la palabra ‘Python’, sin perder datos en la cola;

print('---------B-------- Notif de twitter con "python" en el mensaje')
Notificaciones_B = deepcopy(Notificaciones)
for _ in range(Notificaciones_B.size()):
    Elemento = Notificaciones_B.move_to_end()
    if (Elemento.get_app() == "Twitter") and ("Python" in Elemento.get_mensaje()):
        Elemento.mostrar_notificacion()
        print("----------")

# utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son.
print('---------C-------- Mensajes entre 11:43 y las 15:57')
def horaentero(Notificacion):
    hora_objeto = datetime.strptime(Notificacion.get_hora(), "%H:%M")
    hora_entero = hora_objeto.hour * 100 + hora_objeto.minute
    return hora_entero


NotificacionesAux = Cola()
Notificaciones_C = deepcopy(Notificaciones)
for _ in range(Notificaciones_C.size()):
    Notif = Notificaciones_C.atention()
    hora = horaentero(Notif)
    if hora > 1143 and hora < 1557:
        NotificacionesAux.arrive(Notif)

for _ in range(NotificacionesAux.size()):
    Notif = NotificacionesAux.atention()
    Notif.mostrar_notificacion()
    print("----------")
