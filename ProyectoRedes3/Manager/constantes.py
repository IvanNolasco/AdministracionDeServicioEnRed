direc_ip = '10.0.80.2'
umbral_porcentaje_cpu = 5
umbral_porcentaje_memoria_proc = 60
umbral_porcentaje_memoria_io = 60
umbral_temperatura = 2

# -------------------------------
# ---- OIDS PARA USO DEL CPU ----
# -------------------------------

# OID para obtener el rendimiento del CPU de un
# router cada 1 min y 5 min (Pagina de Vic)
oid_cisco_vic_cpu_1m = ['1.3.6.1.4.1.9.9.109.1.1.1.1.7']
oid_cisco_vic_cpu_5m = ['1.3.6.1.4.1.9.9.109.1.1.1.1.8']
# NOTA: Si no funcionan, agregarles un .0 al OID al final o en todo
# caso un . al principio del OID   

# OID para obtener el rendimiento del CPU de un
# router con CISCO IOS en el intervalo de 5 segs, 5 min y 1 hora
oid_cisco_ios_cpu_5s = ['1.3.6.1.4.1.9.2.1.56.0']
oid_cisco_ios_cpu_5m = ['1.3.6.1.4.1.9.2.1.58.0']
oid_cisco_ios_cpu_1h = ['1.3.6.1.4.1.9.2.1.57.0']
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


# -----------------------------------------
# ---- OID PARA OBTENER LA TEMPERATURA ----
# -----------------------------------------

# OID para obtener la temperatura, es el OID que utiliza Mayra
oid_cisco_temperatura = ['1.3.6.1.4.1.9.9.13.1.3.1.6.1']

# ---------------------------------------
# ---- OID PARA OBTENER EL HOSTNAME ----
# --------------------------------------- 

# OID para obtener el restante de la memoria de multibus de un
# router (Pagina de Vic)
oid_cisco_hostname = ['1.3.6.1.4.1.9.2.1.3']
# NOTA: Si no funciona agregar un .0 al OID al final o en todo
# caso un . al principio del OID, tambien se puede utilizar la
# IP que se usa en ejecutar_oid para enviar_correo()


# OID para obtener el nombre de cualquier equipo,
# es el OID que usa Mayra principalmente
oid_equipo_nombre = ['1.3.6.1.2.1.1.5.0']


