def eliminar_notificaciones_facebook(cola):
    cola = [notificacion for notificacion in cola if notificacion['aplicacion'] != 'Facebook']
    return cola

cola = [
    {'hora': '10:30', 'aplicacion': 'Facebook', 'mensaje': 'Nueva publicación'},
    {'hora': '11:15', 'aplicacion': 'Twitter', 'mensaje': '¡Nuevo seguidor!'},
    {'hora': '12:00', 'aplicacion': 'Facebook', 'mensaje': 'Foto etiquetada'},
    {'hora': '13:30', 'aplicacion': 'Instagram', 'mensaje': 'Me gusta en tu foto'},
]

cola_sin_facebook = eliminar_notificaciones_facebook(cola)
print(cola_sin_facebook)


def mostrar_notificaciones_twitter_python(cola):
    for notificacion in cola:
        if notificacion['aplicacion'] == 'Twitter' and 'Python' in notificacion['mensaje']:
            print(notificacion)

cola = [
    {'hora': '10:30', 'aplicacion': 'Facebook', 'mensaje': 'Nueva publicación'},
    {'hora': '11:15', 'aplicacion': 'Twitter', 'mensaje': '¡Nuevo seguidor!'},
    {'hora': '12:00', 'aplicacion': 'Twitter', 'mensaje': 'Aprende Python desde cero'},
    {'hora': '13:30', 'aplicacion': 'Instagram', 'mensaje': 'Me gusta en tu foto'},
]

mostrar_notificaciones_twitter_python(cola)


def contar_notificaciones_entre_horas(cola):
    pila = [] 
    contador = 0
    for notificacion in cola:
        hora = notificacion['hora']
        if '11:43' <= hora <= '15:57':
            pila.append(notificacion)
            contador += 1

    print("Número de notificaciones entre las 11:43 y las 15:57:", contador)
    return pila


cola = [
    {'hora': '11:00', 'aplicacion': 'Facebook', 'mensaje': 'Nueva publicación'},
    {'hora': '11:45', 'aplicacion': 'Twitter', 'mensaje': '¡Nuevo seguidor!'},
    {'hora': '12:30', 'aplicacion': 'Instagram', 'mensaje': 'Me gusta en tu foto'},
    {'hora': '15:00', 'aplicacion': 'Facebook', 'mensaje': 'Foto etiquetada'},
    {'hora': '16:00', 'aplicacion': 'Twitter', 'mensaje': 'Nueva mención'},
]

pila_notificaciones = contar_notificaciones_entre_horas(cola)
print(pila_notificaciones)

