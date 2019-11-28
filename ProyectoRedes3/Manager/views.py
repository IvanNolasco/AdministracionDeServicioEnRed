from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

def prueba(request):
    return render (request, "layout.html",{"title":"Welcome", "year":"2019"})

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