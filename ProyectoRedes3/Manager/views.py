from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import Manager.ejemplo_hazel as oids

# Create your views here.

def prueba(request):
    return render (request, "layout.html",{"title":"Welcome"})


def oids_req(request):

    nombre, cpu, mem_proc, mem_io, temp = oids.obtener_valores_oid(
        direc_ip='10.0.80.2',
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

    return render (request, "r1.html",{"title":"Monitoring","nombre":nombre})
