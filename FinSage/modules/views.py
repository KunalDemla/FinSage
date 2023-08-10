from django.shortcuts import render


def index(request):
    return render(request,'modules/index.html',{'sidebar':True})
