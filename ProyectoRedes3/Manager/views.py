from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import Manager.ejemplo_hazel as oids
from Manager.tests import get 
from pysnmp import hlapi, debug
from Manager.graficas import  cpu_graph

def pr(request):
    return render (request, "prueba.html")


def prueba(request):
    return render(request, "layout.html", {"title": "Welcome"})

def oids_req(request):
    dir=request.GET['dir']
    r = request.GET['r']
    nombre, cpu, mem_proc, mem_io, temp = oids.obtener_valores_oid(
        direc_ip=dir,
        umbral_cpu=5,
        umbral_memoria_proc=60,
        umbral_memoria_io=60,
        umbral_temp=2
    ) # Igual puedes llamar a la funcion sin parametros

    print("Nombre: ", nombre)
    print("CPU: ", cpu)
    print("Memoria del procesador: ", mem_proc)
    print("Memoria I/O: ", mem_io)
    print("Temperatura: ", temp)
    mem_proc="{0:.2f}".format(mem_proc)
    mem_io = "{0:.2f}".format(mem_io)
    memotp="{0:.2f}".format(100-(float(mem_proc)))
    memotio="{0:.2f}".format(100-(float(mem_proc)))
    cpu_graph("R"+r)
    return render (request, "r1.html", {"title":"Monitoring","r":r, "nombre":nombre,"cpu":cpu,"memp":mem_proc,"memio":mem_io,"temp":temp,"memotp":memotp,"memotio":memotio})

'''def oids_req(request):
    #var_oid = oids.obtener_valores_oid()
    #print("varid=", var_oid)
    nombre, cpu_usage, temperature, memoryUtilization=getRouterParameters(
        "10.0.0.2")
    return render (request, "r1.html",
        {"title":"Monitoring",
        "nombre":nombre,
        "cpu":cpu_usage,
        "temp":temperature,
        "mem":memoryUtilization
    })'''


def getRouterParameters(ipInterface):
    print(ipInterface)
    oids = get(ipInterface, [
        '1.3.6.1.2.1.1.5.0',
        '1.3.6.1.4.1.9.2.1.56.0',
        '1.3.6.1.4.1.9.9.13.1.3.1.6.1',
        '1.3.6.1.4.1.9.9.48.1.1.1.5.1',
        '1.3.6.1.4.1.9.9.48.1.1.1.6.1'
    ], hlapi.CommunityData('comunidadSNMP'))
    nombre = oids['1.3.6.1.2.1.1.5.0']
    cpu_usage = oids['1.3.6.1.4.1.9.2.1.56.0']
    temperature = oids['1.3.6.1.4.1.9.9.13.1.3.1.6.1']
    memoryPoolUsed = oids['1.3.6.1.4.1.9.9.48.1.1.1.5.1']
    memoryPoolFree = oids['1.3.6.1.4.1.9.9.48.1.1.1.6.1']
    memoryUtilization = (memoryPoolUsed*100)/(memoryPoolUsed+memoryPoolFree)
    return nombre, cpu_usage, temperature, memoryUtilization 
