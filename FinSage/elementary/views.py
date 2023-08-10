from django.shortcuts import render

def index(request):
    context = {
        'sidebar': True
    }
    
    return render(request,'elementary/index.html',context)