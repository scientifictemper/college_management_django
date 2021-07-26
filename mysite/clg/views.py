from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from clg.forms import PermissionForm,PaymentForm
from .models import Permission,Payment
from django.http import FileResponse
import os


# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
	
    return render(request,'home.html')
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = RegistrationForm()
		if request.method == 'POST':
			form = RegistrationForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'signup.html', context)  

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')    


def material(request):
	return render(request,'material.html')

def payment(request):
	if request.method=='POST':
		form=PaymentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	    
	else:
		form=PaymentForm()				
	context={
		'form':form
	}
	
	return render(request,'payment.html',context)

def profile(request):
	return render(request,'profile.html')

def permission(request):
	if request.method=='POST':
		form=PermissionForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('viewpay')
	    
	else:
		form=PermissionForm()				
	context={
		'form':form
	}
	return render(request,'permission.html',context)
def viewpermission(request):
	obj=Permission.objects.all()
	return render(request,'viewper.html',{'data':obj})

def viewpayment(request):
	obj=Payment.objects.all()
	return render(request,'viewpay.html',{'data':obj})

def letter(request,id):
	obj=Permission.objects.get(id=id)
	return render(request,'letter.html',{'data':obj})

def feebalance(request,id):
	obj=Payment.objects.get(id=id)
	return render(request,'balance.html',{'data':obj})
def cse(requset):
	return render(requset,'material/cse.html')


def it(requset):
	return render(requset,'material/it.html')

def eee(requset):
	return render(requset,'material/eee.html')

def ece(requset):
	return render(requset,'material/ece.html')

def mech(requset):
	return render(requset,'material/mech.html')


def timetable(request):
    filepath = os.path.join('static', 'timetable.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
def cse_pdf(requset):
	filepath = os.path.join('static', 'cse.pdf')
	return FileResponse(open(filepath, 'rb'), content_type='application/pdf')