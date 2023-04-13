from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django import forms
from .forms import BmiForm
from .forms import PatientForm
#from .forms import InputForm



#working
#def bmi(request)
def homePageView(request): 
    form = BmiForm(request.POST or None)
    #form = PatientForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST': 
        form = BmiForm(request.POST)
        #form = PatientForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data['height']
            New_height = height * 0.025
            weight = form.cleaned_data['weight']
            New_weight = weight * 0.45
            Og_bmi = New_weight/New_height ** 2
            bmi = round(Og_bmi,1)
            #form.save()
            print("form", form.cleaned_data)
            context['message'] = 'Data saved.'
            return render(request, 'home.html', {'form':form, 'bmi':bmi})
    return render(request, "home.html", context)


'''
#working
def homePageView(request): 
    form = PatientForm()

    if request.method == 'POST': 
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
        
    context = {'form':form}
    return render(request, "home.html", context)
'''
'''
def homePageView(request): 
    context= {}
    context['form']= InputForm()
    return render(request, "home.html", context)
'''
'''
def home(request): 
    return HttpResponse("Completed")
'''
# Create your views here.
'''
class HomePageView(TemplateView): 
    template_name = "home.html"
'''     