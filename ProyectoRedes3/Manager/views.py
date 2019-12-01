from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import Manager.ejemplo_hazel as oids

# Create your views here.

def prueba(request):
    return render (request, "layout.html",{"title":"Welcome"})


def oids_req(request):
    var_oid = oids.obtener_valores_oid()
    print("varid=", var_oid)
    return render (request, "r1.html",{"title":"Monitoring","varoid":var_oid})

