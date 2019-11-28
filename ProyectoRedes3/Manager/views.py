from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

def prueba(request):
    return render (request, "layout.html",{"title":"Welcome"})

def routers(request):
    #valor()
    return render (request, "r1.html",{"title":"Monitoring"})


from pysnmp import hlapi, debug

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

def valor():
    hlapi.CommunityData('comunidadSNMP')
    print(get('10.0.10.2', ['.1.3.6.1.4.1.9.9.109.1.1.1.1.5'],hlapi.CommunityData('comunidadSNMP')))


'''class DeliversClient(View):
    template_name='deliversClient.html'
    context_object_name='Delivers'
    def get(self, request, format=None):
        result = PaintingRequest.objects.filter(username=request.user.username, status="D").values()
        return render(request, 
            self.template_name, 
            {
                'result':result,
                'title':self.context_object_name,
                'year':datetime.now().year,
            })'''