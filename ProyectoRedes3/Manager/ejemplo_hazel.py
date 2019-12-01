from pysnmp import hlapi, debug
import re
import Manager.send_email as mail
import Manager.constantes as const

# ----------------------------------------
# CONSTANTES QUE SE USAN PARA LA FUNCION
# def obtener_valores_oid()
# SE PUEDEN CAMBIAR A VOLUNTAD, PUEDE
# APOYARSE UTILIZANDO LAS CONSTANTES DEL
# ARCHIVO constantes.py, QUE SE ENCUENTRA
# EN ESTE MISMO DIRECTORIO.
# ----------------------------------------

guardar_en_archivo = True

direccion_ip = const.direc_ip

umbral_porcentaje_cpu = const.umbral_porcentaje_cpu
umbral_porcentaje_memoria_proc = const.umbral_porcentaje_memoria_proc
umbral_porcentaje_memoria_io = const.umbral_porcentaje_memoria_io
umbral_temperatura = const.umbral_temperatura

oid_nombre = const.oid_equipo_nombre
oid_cpu = const.oid_cisco_ios_cpu_5s
oid_memoria_proc_uso = const.oid_cisco_vic_mem_proc_uso
oid_memoria_proc_rest = const.oid_cisco_vic_mem_proc_rest
oid_memoria_io_uso = const.oid_cisco_vic_mem_io_uso
oid_memoria_io_rest = const.oid_cisco_vic_mem_io_rest
oid_temperatura = const.oid_cisco_temperatura


def get(target, oids, credentials, port=161, engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
    handler = hlapi.getCmd(
        engine,
        credentials,
        hlapi.UdpTransportTarget((target, port)),
        context,
        *construct_object_types(oids)
    )
    return fetch(handler, 1)[0]


def construct_object_types(list_of_oids):
    object_types = []
    for oid in list_of_oids:
        object_types.append(hlapi.ObjectType(hlapi.ObjectIdentity(oid)))
    return object_types


def fetch(handler, count):
    result = []
    for i in range(count):
        try:
            error_indication, error_status, error_index, var_binds = next(handler)
            if not error_indication and not error_status:
                items = {}
                for var_bind in var_binds:
                    items[str(var_bind[0])] = cast(var_bind[1])
                result.append(items)
            else:
                raise RuntimeError('Got SNMP error: {0}', format(error_indication))
        except StopIteration:
            break
    return result


def cast(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        try:
            return float(value)
        except (ValueError, TypeError):
            try:
                return str(value)
            except (ValueError, TypeError):
                pass
    return value


def ejecutar_oid(
    ip='10.0.0.1',
    oids=['1.3.6.1.2.1.1.5.0'],
    comunidad='comunidadSNMP',
    es_numero=True
):
    # debug.setLogger(debug.Debug('io', 'msgproc', 'secmod'))
    hlapi.CommunityData(comunidad)
    respuesta = ''
    if es_numero:
        coincidencias_num = re.split(
            '=\s+',
            str(
                get(
                    ip,
                    oids,
                    hlapi.CommunityData(comunidad)
                )  # Nota: Si no funciona, agregar un [0] aqui
            )
        )

        print('\n El Resultado es: ', coincidencias_num)
        respuesta = coincidencias_num[len(coincidencias_num) - 1]
    else:
        coincidencias_num = re.split(
            ':\s*', 
            str(
                get(
                    ip,
                    oids,
                    hlapi.CommunityData(comunidad)
                )  # Nota: Si no funciona, agregar un [0] aqui
            )
        )
        nueva = coincidencias_num[len(coincidencias_num)-1]
        
        print('\n El Resultado antes del regex es: ', coincidencias_num)
        res_final = re.split(
            '\'',
            str(
                nueva
            )
        )
        print('\n El Resultado despues del regex es: ', res_final)
        respuesta = res_final[len(res_final) - 2]

    print('Se ejecuto el OID: ', oids)
    print('\nen la IP: ', ip)
    print('\n en la comunidad: ', comunidad)
    print('\n Es un numero el resultado?: ', es_numero)
    return respuesta


def regla_de_tres(
    memoria_ocupada=60,
    memoria_libre=40
):
    memoria_total = memoria_ocupada + memoria_libre
    porcentaje_ocupado = memoria_ocupada * 100 / memoria_total
    return porcentaje_ocupado


class File:
    def __init__(self, nom_archivo, nom_modo):
        self.nom_archivo = nom_archivo
        self.nom_modo = nom_modo

    def __enter__(self):
        self.open_file = open(self.nom_archivo, self.nom_modo)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()


def escribir_archivo(nom_archivo, dato):
    datos = []
    with File(nom_archivo, 'w+') as archivo:
        archivo.write(str(dato) + ',')
        datos.append(archivo)


def guardar_resultados_archivo(
    nombre,
    cpu,
    porcentaje_memoria_proc,
    porcentaje_memoria_io,
    temperatura
):
    escribir_archivo(
        str(nombre) + '_resultados_cpu.txt',
        str(cpu)
    )

    escribir_archivo(
        str(nombre) + '_resultados_memoria_proc.txt',
        str(porcentaje_memoria_proc)
    )

    escribir_archivo(
        str(nombre) + '_resultados_memoria_io.txt',
        str(porcentaje_memoria_io)
    )

    escribir_archivo(
        str(nombre) + '_resultados_temperatura.txt',
        str(temperatura)
    )


def obtener_valores_oid(
    direc_ip='10.0.80.2',
    umbral_cpu=5,
    umbral_memoria_proc=60,
    umbral_memoria_io=60,
    umbral_temp=2
):
    global direccion_ip
    global umbral_porcentaje_cpu
    global umbral_porcentaje_memoria_proc
    global umbral_porcentaje_memoria_io
    global umbral_temperatura
    global oid_nombre
    global oid_cpu
    global oid_memoria_proc_uso
    global oid_memoria_proc_rest
    global oid_memoria_io_uso
    global oid_memoria_io_rest
    global oid_temperatura
    global guardar_en_archivo

    if direccion_ip != direc_ip:
        direccion_ip = direc_ip
        umbral_porcentaje_cpu = const.umbral_porcentaje_cpu
        umbral_porcentaje_memoria_proc = const.umbral_porcentaje_memoria_proc
        umbral_porcentaje_memoria_io = const.umbral_porcentaje_memoria_io
        umbral_temperatura = const.umbral_temperatura

    if umbral_memoria_proc != umbral_porcentaje_memoria_proc:
        umbral_porcentaje_memoria_proc = umbral_memoria_proc

    if umbral_memoria_io != umbral_porcentaje_memoria_io:
        umbral_porcentaje_memoria_io = umbral_memoria_io

    if umbral_cpu != umbral_porcentaje_cpu:
        umbral_porcentaje_cpu = umbral_cpu

    if umbral_temp != umbral_temperatura:
        umbral_temperatura = umbral_temp

    # OID que obtiene el nombre del equipo
    nombre = ejecutar_oid(
        ip=direc_ip,
        oids=oid_nombre,
        es_numero=False
    )

    # OID para obtener el porcentaje de uso del CPU
    cpu = ejecutar_oid(
        ip=direc_ip,
        oids=oid_cpu
    )

    # Si pasa del umbral va a enviar un correo al admin
    if float(cpu) > umbral_porcentaje_cpu:
        mail.send_email(nombre, '1')

    # OID que obtiene el porcentaje de MEMORIA DEL PROCESADOR
    memoria_proc_uso = ejecutar_oid(
        ip=direc_ip,
        oids=oid_memoria_proc_uso
    )

    memoria_proc_restante = ejecutar_oid(
        ip=direc_ip,
        oids=oid_memoria_proc_rest
    )

    porcentaje_memoria_proc = regla_de_tres(
        float(memoria_proc_uso),
        float(memoria_proc_restante)
    )

    # Si pasa del umbral va a enviar un correo al admin
    if porcentaje_memoria_proc > umbral_porcentaje_memoria_proc:
        mail.send_email(nombre, '2')

    # OID que obtiene el porcentaje de MEMORIA I/O
    memoria_io_uso = ejecutar_oid(
        ip=direc_ip,
        oids=oid_memoria_io_uso
    )

    memoria_io_restante = ejecutar_oid(
        ip=direc_ip,
        oids=oid_memoria_io_rest
    )

    porcentaje_memoria_io = regla_de_tres(
        float(memoria_io_uso),
        float(memoria_io_restante)
    )

    # Si pasa del umbral va a enviar un correo al admin
    if porcentaje_memoria_io > umbral_porcentaje_memoria_io:
        mail.send_email(nombre, '3')

    # OID que obtiene el estado de la TEMPERATURA
    temperatura = ejecutar_oid(
        ip=direc_ip,
        oids=oid_temperatura
    )

    # Si devuelve un valor mayor a 1, manda un email al admin
    if int(temperatura) > umbral_temperatura:
        mail.send_email(nombre, '4')

    # En este proceso escribe en los archivos los resultados
    # obtenidos para hacer las graficas estaticas
    # solamente si esta habilitada la opcion de guardar_en_archivo
    if guardar_en_archivo:
        guardar_resultados_archivo(
            nombre,
            cpu,
            porcentaje_memoria_proc,
            porcentaje_memoria_io,
            temperatura
        )

    return \
        nombre, \
        cpu, \
        porcentaje_memoria_proc, \
        porcentaje_memoria_io, \
        temperatura
    # time.sleep(5)
