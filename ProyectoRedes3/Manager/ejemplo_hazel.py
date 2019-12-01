from pysnmp import hlapi, debug
import time
import re
import Manager.send_email as enviar_correo


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
    esNumero=True
):
    # debug.setLogger(debug.Debug('io', 'msgproc', 'secmod'))
    hlapi.CommunityData(comunidad)
    respuesta = ''
    if esNumero:
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
        res_final = re.split(
            '\'',
            str(
                nueva
            )
        )

        respuesta = res_final[len(res_final) - 2]
    return respuesta


def regla_de_tres(
    memoria_ocupada=60,
    memoria_libre=40
):
    memoria_total = memoria_ocupada + memoria_libre
    porcentaje_ocupado = memoria_total * 100 / memoria_ocupada
    return porcentaje_ocupado

# TIPO_OID: NORMAL, CPU, MEMORIA


def obtener_valores_oid(
    direc_ip='10.0.80.2',
    tipo_oid='NORMAL',
    umbral=60
):

    # -------------------------------
    # ---- OIDS PARA USO DEL CPU ----
    # -------------------------------

    umbral_porcentaje_cpu = umbral

    # OID para obtener el rendimiento del CPU de un
    # router cada 1 min y 5 min (Pagina de Vic)
    oid_cisco_vic_cpu_1m = ['1.3.6.1.4.1.9.9.109.1.1.1.1.7']
    oid_cisco_vic_cpu_5m = ['1.3.6.1.4.1.9.9.109.1.1.1.1.8']
    # NOTA: Si no funcionan, agregarles un .0 al OID al final o en todo
    # caso un . al principio del OID   
    
    # OID para obtener el rendimiento del CPU de un
    # router con CISCO IOS en el intervalo de 5 segs, 5 min y 1 hora
    oid_cisco_ios_cpu_5s = ['1.3.6.1.4.1.9.2.1.56']
    oid_cisco_ios_cpu_5m = ['1.3.6.1.4.1.9.2.1.58']
    oid_cisco_ios_cpu_1h = ['1.3.6.1.4.1.9.2.1.57']
    # NOTA: Si no funcionan, agregarles un .0 al OID al final o en todo
    # caso un . al principio del OID
    
    # OID para obtener el rendimiento del CPU de un
    # router CISCO ASR 100 en el intervalo de 1 min y 5 min
    # para routers tipo RP0, ESP0, SIP0
    oid_cisco_rp0_cpu_1m = ['1.3.6.1.4.1.9.9.109.1.1.1.1.24.2']
    oid_cisco_esp0_cpu_1m = ['1.3.6.1.4.1.9.9.109.1.1.1.1.24.3']
    oid_cisco_sip0_cpu_1m = ['1.3.6.1.4.1.9.9.109.1.1.1.1.24.4']
    oid_cisco_rp0_cpu_5m = ['1.3.6.1.4.1.9.9.109.1.1.1.1.25.2']
    oid_cisco_esp0_cpu_5m = ['1.3.6.1.4.1.9.9.109.1.1.1.1.25.3']
    oid_cisco_sip0_cpu_5m = ['1.3.6.1.4.1.9.9.109.1.1.1.1.25.4']   
    # NOTA: Si no funcionan, agregarles un .0 al OID al final o en todo
    # caso un . al principio del OID

    # -------------------------------------
    # ---- OIDS PARA USO DE LA MEMORIA ----
    # ------------------------------------- 

    umbral_porcentaje_memoria = umbral

    # OID para obtener el uso de la memoria del procesador de un
    # router (Pagina de Vic)
    oid_cisco_vic_mem_proc_uso = ['1.3.6.1.4.1.9.9.48.1.1.1.5.1']
    # NOTA: Si no funciona usar el siguiente,
    # si no funciona el siguiente
    # agregar un .0 al OID al final o en todo
    # caso un . al principio del OID

    # OID para obtener el uso de la memoria de I/O de un
    # router (Pagina de Vic)
    oid_cisco_vic_mem_io_uso = ['1.3.6.1.4.1.9.9.48.1.1.1.5.2']
    # NOTA: Si no funciona usar el siguiente,
    # si no funciona el siguiente 
    # agregar un .0 al OID al final o en todo
    # caso un . al principio del OID

    # OID para obtener el uso de la memoria de PCI de un
    # router (Pagina de Vic)
    oid_cisco_vic_mem_pci_uso = ['1.3.6.1.4.1.9.9.48.1.1.1.5.3']
    # NOTA: Si no funciona usar el siguiente,
    # si no funciona el siguiente 
    # agregar un .0 al OID al final o en todo
    # caso un . al principio del OID

    # OID para obtener el uso de la memoria de Rapida de un
    # router (Pagina de Vic)
    oid_cisco_vic_mem_fast_uso = ['1.3.6.1.4.1.9.9.48.1.1.1.5.4']
    # NOTA: Si no funciona usar el siguiente,
    # si no funciona el siguiente 
    # agregar un .0 al OID al final o en todo
    # caso un . al principio del OID

    # OID para obtener el uso de la memoria de multibus de un
    # router (Pagina de Vic)
    oid_cisco_vic_mem_fast_uso = ['1.3.6.1.4.1.9.9.48.1.1.1.5.5']
    # NOTA: Si no funciona usar el siguiente,
    # si no funciona el siguiente 
    # agregar un .0 al OID al final o en todo
    # caso un . al principio del OID

    # OID para obtener el restante de la memoria del procesador de un
    # router (Pagina de Vic)
    oid_cisco_vic_mem_proc_rest = ['1.3.6.1.4.1.9.9.48.1.1.1.6.1']
    # NOTA: Si no funciona usar el siguiente,
    # si no funciona el siguiente 
    # agregar un .0 al OID al final o en todo
    # caso un . al principio del OID

    # OID para obtener el restante de la memoria de I/O de un
    # router (Pagina de Vic)
    oid_cisco_vic_mem_io_rest = ['1.3.6.1.4.1.9.9.48.1.1.1.6.2']
    # NOTA: Si no funciona usar el siguiente,
    # si no funciona el siguiente 
    # agregar un .0 al OID al final o en todo
    # caso un . al principio del OID

    # OID para obtener el restante de la memoria de PCI de un
    # router (Pagina de Vic)
    oid_cisco_vic_mem_pci_rest = ['1.3.6.1.4.1.9.9.48.1.1.1.6.3']
    # NOTA: Si no funciona usar el siguiente,
    # si no funciona el siguiente 
    # agregar un .0 al OID al final o en todo
    # caso un . al principio del OID

    # OID para obtener el restante de la memoria de Rapida de un
    # router (Pagina de Vic)
    oid_cisco_vic_mem_fast_rest = ['1.3.6.1.4.1.9.9.48.1.1.1.6.4']
    # NOTA: Si no funciona usar el siguiente,
    # si no funciona el siguiente 
    # agregar un .0 al OID al final o en todo
    # caso un . al principio del OID

    # OID para obtener el restante de la memoria de multibus de un
    # router (Pagina de Vic)
    oid_cisco_vic_mem_fast_rest = ['1.3.6.1.4.1.9.9.48.1.1.1.6.5']
    # NOTA: Si no funciona usar el siguiente,
    # si no funciona el siguiente 
    # agregar un .0 al OID al final o en todo
    # caso un . al principio del OID

    # ---------------------------------------
    # ---- OID PARA OBTENER EL HOSTNAME ----
    # --------------------------------------- 

    # OID para obtener el restante de la memoria de multibus de un
    # router (Pagina de Vic)
    oid_cisco_hostname = ['1.3.6.1.4.1.9.2.1.3']
    # NOTA: Si no funciona agregar un .0 al OID al final o en todo
    # caso un . al principio del OID, tambien se puede utilizar la
    # IP que se usa en ejecutar_oid para enviar_correo()

    # Si se va a ejecutar un ejemplo normalito, usarlo tal cual
    if tipo_oid == 'NORMAL':
        normal = ejecutar_oid(
            ip=direc_ip,
            esNumero=False
        )
        return normal

    # Si se va a monitorear el CPU, ejecutarlo asi:
    if tipo_oid == 'CPU':
        hostname = ejecutar_oid(
            ip=direc_ip,
            oids=oid_cisco_hostname
        )

        cpu = ejecutar_oid(
            ip=direc_ip,
            oids=oid_cisco_vic_cpu_1m
        )

        if int(cpu) > umbral_porcentaje_cpu:
            enviar_correo(hostname,'1')  # Aqui se puede utilizar la IP en lugar del hostname

        return cpu
    # Si se va a monitorear la MEMORIA DEL CPU, ejecutarlo asi:

    if tipo_oid == 'MEMORIA':
        hostname = ejecutar_oid(
            p=direc_ip,
            oids=oid_cisco_hostname
        )

        memoria_uso = ejecutar_oid(
            ip=direc_ip,
            oids=oid_cisco_vic_mem_proc_uso
        )

        memoria_restante = ejecutar_oid(
            ip=direc_ip,
            oids=oid_cisco_vic_mem_proc_rest
        )

        porcentaje_memoria = regla_de_tres(
            int(memoria_uso),
            int(memoria_restante)
        )

        if porcentaje_memoria > umbral_porcentaje_memoria:
            enviar_correo(hostname,'2')  # Aqui se puede utilizar la IP en lugar del hostname

        return porcentaje_memoria

    time.sleep(5)
