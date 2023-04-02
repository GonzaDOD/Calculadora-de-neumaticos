# -*- coding: utf-8 -*-
# La línea superior habilita las tildes en nuestro código
neumatico = input("Ingresá los datos del neumático sin espacios: ")  
# Obtenemos los datos del neumático para realizar los cálculos y recopilar información
neumatico_list = list(neumatico)  # Lo convertimos en lista para poder acceder a sus dígitos

if len(neumatico) != 12:  # Verificamos si tiene 12 dígitos y no tiene espacios
    raise Exception(
        "Los datos ingresados no son correctos, por favor, intente nuevamente")  
    # Si la condición se cumple, se obtiene una excepción.

else:  # Si, por lo contrario, los datos introducidos son correctos, se procede a realizar los cálculos
    ancho_pisada = neumatico_list[0] + neumatico_list[1] + neumatico_list[
        2]  # Obtenemos los 3 primeros digitos que pertenecen al ancho de pisada
    porcentaje_flanco = neumatico_list[4] + neumatico_list[
        5]  # Obtenemos los 2 digitos que siguen después de la barra diagonal (/)
    construccion = neumatico_list[6]  # Obtenemos el codigo de construcción (R/D)
    diametro_llanta_p = neumatico_list[7] + neumatico_list[
        8]  # Obtenemos el diametro de la llanta como los siguientes 2 dígitos
    codigo_carga = neumatico_list[9] + neumatico_list[10]  # Obtenemos el código de la capacidad de carga
    codigo_velocidad = neumatico_list[11]  # Obtenemos el código de la capacidad de carga

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
    capacidad_carga = {  # Obtenemos los valores de la tabla de capacidad, en un diccionario
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
