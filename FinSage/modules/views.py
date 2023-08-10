from django.shortcuts import render,redirect,HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Modules
from django.contrib.auth.decorators import login_required

def index(request):
    data = Modules.objects.all().values()
    fav = {}
    for module in data:
        mod = get_object_or_404(Modules,moduleId=module['moduleId'])
        if mod.likes.filter(id=request.user.id).exists():
            module['fav'] = False
        else:
            module['fav'] = True
            # fav[module['moduleId']] = True
            
    context = {
        #'form': forms[cipher_choice](),
        'modules': data,
        'sidebar': True,
        # 'fav': fav
        # 'fav': True
    }
    
    # cipher = get_object_or_404(Ciphers,name=cipher_choice)
    # if cipher.favourites.filter(id=request.user.id).exists():
    #     context['fav'] = False
    
        
    

    #print(data)
    return render(request,'modules/index.html',context)

def modules(request,modules_choice):
    mapping = {
        "budgeting" : "budgeting.html",
        "interest" : "interest.html",
        "digitalPayments" : "digital_payment.html",
        "financialGoals" : "financial_goals.html",
        "needsVsWants" : "index.html",
        "mutualFunds" : "mutual_funds.html",
        "stockMarket" : "stocks.html",
        "retirementPlanning": "retirement.html",
        "privateEquity":"equity.html",
        "taxPlanning": "tax.html",
        "cryptocurrency": "crypto.html"
    }
    return render(request,'modules/'+mapping[modules_choice],{'sidebar':False})

def favourite_add(request,modules_choice):
    module = get_object_or_404(Modules,moduleId=modules_choice)
    if module.likes.filter(id=request.user.id).exists():
        module.likes.remove(request.user)
        module.likeCount-=1
        module.save()
    else:
        module.likes.add(request.user)
        module.likeCount+=1
        module.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def recommendations(request):
    return render(request,'modules/recommendation.html',{'sidebar':True})

@login_required
def liked(request):
    data = Modules.objects.all().values()
    fav = []
    for module in data:
        mod = get_object_or_404(Modules,moduleId=module['moduleId'])
        if mod.likes.filter(id=request.user.id).exists():
            fav.append(module)
    context = {
        "sidebar" : True,
        "modules" : fav,
    }
    return render(request,'modules/favourite_ciphers_list.html',context)