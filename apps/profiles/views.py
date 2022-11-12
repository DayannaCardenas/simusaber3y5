from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
from apps.profiles.form import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def user_validate_group(roles=[]):
	def decorator(view_func):
		def arguments(request, *args, **kwargs):
			if request.user.groups.exists():
				if request.user.groups.all()[0].name in roles:
					return view_func(request, *args, **kwargs)
			return redirect('profiles:login')
		return arguments
	return decorator

def user_validate_group(roles=[]):
	def decorator(view_func):
		def arguments(request, *args, **kwargs):
			if request.user.groups.exists():
				if request.user.groups.all()[0].name in roles:
					return view_func(request, *args, **kwargs)
			return redirect('profiles:login')
		return arguments
	return decorator

def login_user(request):
    context={}
    if request.POST:
        form=AuthenticationForm(None, request.POST)
        username = request.POST['username']
        password = request.POST['password']
        if form.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profiles:home')
            else:
                form.add_error(None, "Usuario no encontrado")
        context['form']=form
    return render(request, "general/login.html", context)

def logout_user(request):
    logout(request)
    return redirect('/profiles/login')

@login_required(login_url='/profiles/login')
# @user_validate_group(roles=['Administrator', 'Authorizer'])
def home_view(request):
    return render(request, "general/home.html")


def create_customer_view(request):
    type_documents = TypeDocument.objects.all()
    countries = Country.objects.all()
    if request.method == 'POST': 
        update_request = request.POST.copy()
        update_request.update({'email':request.POST['email'].lower(), 'username':request.POST['email'].lower(), 'rol':2,'state':1})
        form = UserForm(update_request)
        form1 = CustomerForm(update_request, request.FILES)
        if form.is_valid() and form1.is_valid():
            user = form.save(commit = False)
            user.set_password(form.data['new_password'])
            user.save()            
            user.groups.add(form.data['rol'])
            customer = form1.save(commit = False)
            customer.user_id = user.id
            customer.save()   
            return redirect('/profiles/readCustomer/')
        else:
            print(form.errors)
            print(form1.errors)
    else:
        form = UserForm()
        form1 = CustomerForm()
    context = {
        'form': form,
        'form1': form1,
        'type_documents': type_documents,
        'countries':countries
    }
    return render (request,"profiles/createUpdateCustomer.html", context)

def update_customer_view(request,pk):
    customer = Customer.objects.get(user__id = pk)
    type_documents = TypeDocument.objects.all()
    countries = Country.objects.all()
    if request.method == 'POST': 
        update_request = request.POST.copy()
        update_request.update({ 'state':1, 'user':customer.user.id})
        form = UserUpdateForm(update_request, instance = customer.user)
        form1 = CustomerForm(update_request, request.FILES, instance = customer)
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()   
            return redirect('/profiles/readCustomer/')
        else:
            print(form.errors)
            print(form1.errors)
    else:
        form = UserUpdateForm()
        form1 = CustomerForm()
    context = {
        'form': form,
        'form1': form1,
        'type_documents': type_documents,
        'customer': customer,
        'countries':countries
    }
    return render (request,"profiles/createUpdateCustomer.html", context)

def read_customer_view(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers 
    }
    return render (request,"profiles/readCustomer.html", context)

