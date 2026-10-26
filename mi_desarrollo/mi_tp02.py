# =====================================================================
#  TP02 - Programacion I
#  Controlador de misiones
#
#  ESTE ES EL ARCHIVO DONDE ESCRIBIS TU PROGRAMA.
#
#  Antes de ejecutarlo:
#    1. Abri INICIAR_SIMULADOR (elegi G1 o Go2)
#    2. Espera a que aparezca la ventana con el robot
#    3. Recien ahi ejecuta este archivo
#
#  Nombre y apellido:  .....................................
#  Comision:           .....................................
# =====================================================================

from robot import ErrorDeSeguridad, Robot

from misiones import MISION_BASICA, MISION_CON_ERRORES, MISION_CUADRADO


# =====================================================================
#  PARTE 1 - Validar un comando
# =====================================================================
def comando_es_valido(comando):
    """Decide si un comando se puede ejecutar. Devuelve True o False.

    Un comando es una tupla. El primer elemento dice que hacer:

        ("avanzar", velocidad, tiempo)    velocidad en m/s, tiempo en s
        ("girar", velocidad, tiempo)      velocidad en rad/s, tiempo en s
        ("detenerse",)
        ("saludar",)

    Cosas que conviene revisar:
      - que la tupla no este vacia
      - que el nombre del comando sea uno de los cuatro validos
      - que tenga la cantidad de datos que corresponde
        (avanzar y girar llevan dos; detenerse y saludar, ninguno)
      - que velocidad y tiempo sean numeros de verdad, no textos
      - que el tiempo no sea negativo
    """
    # TU CODIGO ACA
    if type(comando) != tuple:
        return False

    if len(comando) == 0:
        return False

    nombre = comando[0]

    if nombre == "detenerse" or nombre == "saludar":
        if len(comando) == 1:
            return True
        else:
            return False

    if nombre == "avanzar" or nombre == "girar":
        if len(comando) != 3:
            return False

        velocidad = comando[1]
        tiempo = comando[2]

        if type(velocidad) != int and type(velocidad) != float:
            return False

        if type(tiempo) != int and type(tiempo) != float:
            return False

        if tiempo >= 0 and tiempo <= 10:
            if nombre == "avanzar":
                if velocidad >= -0.2 and velocidad <= 0.2:
                    return True

            if nombre == "girar":
                if velocidad >= -0.5 and velocidad <= 0.5:
                    return True

    return False
# =====================================================================
#  PARTE 2 - Ejecutar un comando
# =====================================================================
def ejecutar_comando(robot, comando):
    """Ejecuta UN comando en el robot. Devuelve un texto con lo que paso.

    Ordenes que podes usar:

        robot.avanzar(velocidad=..., tiempo=...)
        robot.girar(velocidad=..., tiempo=...)
        robot.detenerse()
        robot.saludar()

    Ojo: aunque el comando parezca valido, el robot puede rechazarlo
    igual (por ejemplo, si la velocidad supera el limite de la materia).
    Eso llega como un ErrorDeSeguridad y conviene atraparlo.
    """
    # TU CODIGO ACA
    nombre = comando[0]

    if nombre == "avanzar":
        robot.avanzar(velocidad=comando[1], tiempo=comando[2])

    elif nombre == "girar":
        robot.girar(velocidad=comando[1], tiempo=comando[2])

    elif nombre == "detenerse":
        robot.detenerse()

    elif nombre == "saludar":
        robot.saludar()

    return "Ejecutado"
# =====================================================================
#  PARTE 3 - Recorrer la mision entera
# =====================================================================
def ejecutar_mision(robot, mision, historial):
    """Recorr
    e la lista de comandos, uno por uno.

    Por cada comando:
      - si NO es valido, lo rechaza y sigue con el siguiente
      - si es valido, lo ejecuta
      - en los dos casos, guarda en 'historial' que fue lo que paso

    Un comando invalido NO tiene que cortar la mision.
    """
    # TU CODIGO ACA
    for comando in mision:
        print("Procesando:", comando)

        if comando_es_valido(comando):
            resultado = ejecutar_comando(robot, comando)
        else:
            resultado = "Rechazado"

        registro = {
            "comando": comando,
            "resultado": resultado
        }

        historial.append(registro)
# =====================================================================
#  PARTE 4 - El reporte final
# =====================================================================
def generar_reporte(historial):
    """Muestra por pantalla un resumen de la mision.

    Tiene que decir, como minimo:
      - cuantos comandos se ejecutaron bien
      - cuantos se rechazaron
      - cual fue el motivo de cada rechazo
    """
    # TU CODIGO ACA
    ejecutados = 0
    rechazados = 0

    for registro in historial:
        if registro["resultado"] == "Ejecutado":
            ejecutados = ejecutados + 1
        else:
            rechazados = rechazados + 1
            print("Comando rechazado:", registro["comando"])
            print("Motivo: El comando es incorrecto.")

    print("Comandos que fueron ejecutados:", ejecutados)
    print("Comandos que fueron rechazados:", rechazados)
    pass


# =====================================================================
#  PROGRAMA PRINCIPAL
# =====================================================================
def main():
    robot = Robot()
    robot.conectar()

    historial = []

    ejecutar_mision(robot, MISION_CON_ERRORES, historial)
    generar_reporte(historial)

    robot.detenerse()
    robot.desconectar()


if __name__ == "__main__":
    main()