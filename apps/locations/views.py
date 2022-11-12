from django.shortcuts import render
from apps.locations.models import *
from django.contrib.auth.decorators import login_required
from apps.locations.form import *

# Create your views here.
@login_required(login_url='/profiles/login')
# @user_passes_test(is_administrator)
def read_country_view(request):
    countries=Country.objects.all()
    context={
                'countries':countries,
            }
    return render(request, "locations/readCountry.html",context)

@login_required(login_url='/profiles/login')
# @user_passes_test(is_administrator)
def read_departament_view(request):
    departaments=Departament.objects.all()
    context={
                'departaments':departaments,
            }
    return render(request, "locations/readDepartament.html",context)

@login_required(login_url='/profiles/login')
# @user_passes_test(is_administrator)
def read_city_view(request):
    cities=City.objects.all()
    context={
                'cities':cities,
            }
    return render(request, "locations/readCity.html",context)

def create_office_view(request):
    countries = Country.objects.all()
    if request.method == 'POST': 
        form = OfficeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()   
            return redirect('/profiles/readOffice/')
        else:
            print(form.errors)
    else:
        form = OfficeForm()
    context = {
        'form': form,
        'countries': countries
    }
    return render (request,"profiles/createUpdateOffice.html", context)

def read_office_view(request):
    offices=Office.objects.all()
    context={
                'offices':offices,
            }
    return render(request, "locations/readOffice.html",context)

def update_office_view(request,pk):
    office = Office.objects.get()
    countries = Country.objects.all()
    if request.method == 'POST': 
        form = OfficeForm(update_request, request.FILES, instance = office)
        if form.is_valid():
            form.save() 
            return redirect('/profiles/readOffice/')
        else:
            print(form.errors)
    else:
        form = OfficeForm()
    context = {
        'form': form,
        'countries':countries
    }
    return render (request,"profiles/createUpdateOffice.html", context)