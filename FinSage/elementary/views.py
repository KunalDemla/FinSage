from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from users.models import Profile
from .forms import ExclusiveForm

def index(request):
    context = {
        'sidebar': True
    }
    
    return render(request,'elementary/index.html',context)

@login_required
def connect(request):
    prof = get_object_or_404(Profile,user= request.user)
    exclu = ['SC','ST','PWD']
    if request.method == 'POST':
        form = ExclusiveForm(request.POST)
        if form.is_valid() and prof.exclusiveChecked == False:
            prof.exclusiveChecked = True
            gender = form.cleaned_data['gender']
            area = form.cleaned_data['area']
            category = form.cleaned_data['category']
            if gender == 'female' or gender == 'others' or area == 'rural' or category in exclu:
                prof.exclusive = True
            prof.save()
    if prof.exclusiveChecked:
        if prof.exclusive:
            return render(request,'elementary/exclusive.html',{'sidebar':False})
        else:
            return render(request,'elementary/not_exclusive.html',{'sidebar':False})
    else:
        return render(request,'elementary/exclusive_check.html',{'sidebar':False, 'form':ExclusiveForm()})