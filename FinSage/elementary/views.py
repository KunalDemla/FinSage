from django.shortcuts import render

def index(request):
    context = {
        'sidebar': True
    }
    
    return render(request,'modules/index.html',context)