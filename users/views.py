from django.shortcuts import render 
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm, UserLoginForm
from django.urls import reverse
from django.contrib.auth import logout,authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
	usfo=UserForm()
	return render(request,'users/index.html',{'usfo':usfo})

def login(request):
	usfo=UserLoginForm(request.POST or None)
	if request.method=='POST':
		if usfo.is_valid():
			email=usfo.cleaned_data.get('email')
			password=usfo.cleaned_data.get('password')
			user=authenticate(email=email,password=password)
			if user:
				if user.is_active:
					auth_login(request,user,backend='users.backend.NewBackend')
					print(request.user.name,request.user.email)
					return HttpResponseRedirect(reverse('simp'))
				else:
					return HttpResponse("Your account is inactive.")
	return render(request,'users/login.html',{'usfo':usfo})

def signup(request):
	usfo=UserForm(request.POST or None)
	if request.method == 'POST':
		print(usfo.is_valid(),usfo.clean_email(),usfo.clean_password2())
		print(usfo.clean())
		print(usfo.data)
		print(usfo.cleaned_data)
		if usfo.is_valid() and usfo.clean_email() and usfo.clean_password2():
			
			
			us=usfo.save(commit=False)
			print(usfo)
			us.set_password(usfo.clean_password2())
			us.save()
			auth_login(request,us,backend='users.backend.NewBackend')
			return HttpResponseRedirect(reverse('simp'))
		else:
			print(usfo.errors)

	return render(request,'users/signup.html',{'usfo':usfo})
@login_required
def simp(request):
	return	render(request,'users/simple.html')

@login_required
def simp1(request):
	return	render(request,'users/simp1.html')