from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from clg.forms import PermissionForm,PaymentForm
from django.http import FileResponse
from django.views.generic import View

import os

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .decorators import unauthenticated_user, allowed_users, admin_only
from .models import Permission,Payment
from .forms import RegistrationForm



# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url='login')

def home(request):

	return render(request,'home.html')

@unauthenticated_user
def registerPage(request):
	form = RegistrationForm()
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='students')
			user.groups.add(group)

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'signup.html', context)


@unauthenticated_user
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
		return redirect('viewper')
	    
	else:
		form=PermissionForm()				
	context={
		'form':form
	}
	return render(request,'permission.html',context)

class PermissionListView(View):
	def get(self,*args,**kwargs):
		permissions=Permission.objects.all()
		context={
			"permissions":permissions,
		}
		return render(self.request,'viewper.html',context)
	def post(self,request):
		permission_ids=request.POST.getlist("i.id")
		permission_ids=list(map(int,permission_ids))

		update_status_for_permission=int(request.POST['status'])
		permissions=Permission.objects.filter(id__in=permission_ids)
		if update_status_for_permission == 0:
			permissions.update(status=False)
		else:
			permissions.update(status=True)
		return redirect('viewper')				

def  givePermission(request,id):
	obj=Permission.objects.get(id=id)
	if request.method=='POST':
		obj=Permission.objects.get(id=id)
		form=PermissionForm(request.POST,instance=obj)
		if form.is_valid():
			obj.name=form.cleaned_data['name']
			obj.save()
			form.save()
			return redirect('viewper')
	    
	else:
		form=PermissionForm(instance=obj)				
	context={
		'form':form,
		'obj':obj,
	}
	return render(request,'giveper.html',context)
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

