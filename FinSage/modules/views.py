from django.shortcuts import render,redirect,HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Modules
from django.contrib.auth.decorators import login_required
from .forms import QuestionsForm

def index(request):
    data = Modules.objects.all().values()
    fav = {}
    form  = QuestionsForm()
    mapping = {
        0 : "Basic",
        1 : "Intermediate",
        2 : "Advanced",
    }
    for module in data:
        mod = get_object_or_404(Modules,moduleId=module['moduleId'])
        if mod.likes.filter(id=request.user.id).exists():
            module['fav'] = False
        else:
            module['fav'] = True
            # fav[module['moduleId']] = True
        module['difficulty'] = mapping[module['difficulty']]
            
    context = {
        #'form': forms[cipher_choice](),
        'modules': data,
        'sidebar': True,
        'form' : form,
        # 'fav': fav
        # 'fav': True
    }
    
    
        
    

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

@login_required
def recommendations(request):
    mapping = {
        0 : "Basic",
        1 : "Intermediate",
        2 : "Advanced",
    }
    score = [0,0,0,0,0,0,0,0,0]
    recommendations = []
    data = Modules.objects.all().values()
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            for i in range(27):
                score[(int)(i/3)] += int(form.cleaned_data[f'q{i}'])
            i = 0 
            for module in data:
                if score[i] <= 1:
                    recommendations.append(module)
                i+=1
                mod = get_object_or_404(Modules,moduleId=module['moduleId'])
                if mod.likes.filter(id=request.user.id).exists():
                    module['fav'] = False
                else:
                    module['fav'] = True
                module['difficulty'] = mapping[module['difficulty']]

    context = {
        'sidebar':True,
        'form' : QuestionsForm(),
        'recommendations' : recommendations,
    }
    return render(request,'modules/recommendation.html',context)

def calculators(request):
    context = {
        'sidebar':True
    }
    return render(request,'modules/calculators.html',context)

@login_required
def certi(request):
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        score =0
        cleared = False
        sidebar = False
        if form.is_valid():
            for i in range(27):
                score+= int(form.cleaned_data[f'q{i}'])
            if score >= 20:
                cleared = True
                sidebar = True
        context = {'sidebar':sidebar,'cleared':cleared,'user':request.user}
        return render(request,'modules/certi.html',context)
    context = {'sidebar':False,'user':request.user,'type':'get','form':QuestionsForm()}
    return render(request,'modules/certi.html',context)