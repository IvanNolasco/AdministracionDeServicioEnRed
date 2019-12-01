from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import Manager.ejemplo_hazel as oids
from Manager.tests import get 
from pysnmp import hlapi, debug

def prueba(request):
    return render (request, "layout.html",{"title":"Welcome"})


def oids_req(request):
    var_oid = oids.obtener_valores_oid()
    print("varid=", var_oid)
    return render (request, "r1.html",
        {"title":"Monitoring",
        "varoid":var_oid
    })

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

