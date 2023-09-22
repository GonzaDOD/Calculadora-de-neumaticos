# -*- coding: utf-8 -*-
# La línea superior habilita las tildes en nuestro código

def neumatico():
    n = input("Ingresá los datos del neumático con espacios(255/55 R 20 110 V): ")
    if n == "":
        return "255/55 R 20 110 V"
    else:
        return n


neumatico = neumatico()
# Obtenemos los datos del neumático para realizar los cálculos y recopilar información
neumatico_list = neumatico.split(" ")  # Lo convertimos en una lista separada para poder acceder a sus dígitos.

if len(neumatico_list) != 5:  # Verificamos si la lista tiene los 5 indices,
    raise Exception(
        "Los datos ingresados no son correctos, por favor, intente nuevamente")
    # Si la condición se cumple, se obtiene una excepción.

else:  # Si, por lo contrario, los datos introducidos son correctos, se procede a realizar los cálculos
    dato1 = neumatico_list[0].split("/")
    ancho_pisada = dato1[0]  # Obtenemos los primeros digitos que pertenecen al ancho de pisada
    porcentaje_flanco = dato1[1]  # Obtenemos los 2 digitos que siguen después de la barra diagonal (/)
    construccion = neumatico_list[1]  # Obtenemos el codigo de construcción (R/D)
    diametro_llanta_p = neumatico_list[2]  # Obtenemos el diametro de la llanta
    codigo_carga = neumatico_list[3]  # Obtenemos el código de la capacidad de carga
    codigo_velocidad = neumatico_list[4]  # Obtenemos el código de la capacidad de carga

    construccion_dict = {  # Obtenemos los dos valores posibles de construccion, en un diccionario
        "R": "Radial",
        "D": "Diagonal"
    }

    diametro_llanta_mm = int(int(diametro_llanta_p) * 25.4)

    velocidad_max = {  # Obtenemos los valores de la tabla de velocidad, en un diccionario
        "L": "120",
        "M": "130",
        "N": "140",
        "P": "150",
        "Q": "160",
        "R": "170",
        "S": "180",
        "T": "190",
        "H": "210",
        "V": "240",
        "W": "270",
        "Y": "300",
        "ZR": "Mayor a 240",
    }
    capacidad_carga = {
        "70": "335",
        "71": "345",
        "72": "355",
        "73": "365",
        "74": "375",
        "75": "387",
        "76": "400",
        "77": "412",
        "78": "425",
        "79": "437",
        "80": "450",
        "81": "462",
        "82": "475",
        "83": "487",
        "84": "500",
        "85": "515",
        "86": "530",
        "87": "545",
        "88": "560",
        "89": "580",
        "90": "600",
        "91": "615",
        "92": "630",
        "93": "660",
        "94": "670",
        "95": "690",
        "96": "710",
        "97": "730",
        "98": "750",
        "99": "775",
        "100": "800",
        "101": "825",
        "102": "850",
        "103": "875",
        "104": "900",
        "105": "925",
        "106": "950",
        "107": "975",
        "108": "1000",
        "109": "1030",
        "110": "1060"
    }

    print(f"""
    Ancho de pisada: {ancho_pisada}mm
    Medida del flanco: {int(int(ancho_pisada) * int(porcentaje_flanco) / 100)}mm
    Tipo de Construcción: {construccion_dict[construccion.upper()]}
    Diámetro Interno: {diametro_llanta_mm}mm
    Capacidad de Carga: {capacidad_carga[codigo_carga]}Kg
    Velocidad Máxima: {velocidad_max[codigo_velocidad.upper()]}Km/h
    """)
    # Mostramos en pantalla la información recopilada haciendo los cálculos necesarios
    # incluyendo la unidad de los valores y añadiendo el ".upper" para permitir minúsculas.
input()
