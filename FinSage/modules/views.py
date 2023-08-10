from django.shortcuts import render
from .models import Modules

def index(request):
    data = Modules.objects.all().values()
    context = {
        #'form': forms[cipher_choice](),
        'data': data
        
    }
    

    #print(data)
    return render(request,'modules/index.html',{'sidebar':True})

def modules(request):
    return render(request,'modules/index.html',{'sidebar':True})

def recommendations(request):
    return render(request,'modules/index.html',{'sidebar':True})

