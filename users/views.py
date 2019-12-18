from django.shortcuts import render 
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import UserForm, UserLoginForm
from django.urls import reverse
from django.contrib.auth import logout as auth_logout,authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Food
from django.core import serializers
import json
# from django import forms
# from django.core.exceptions import ValidationError
# Create your views here.
def index(request):
	usfo=UserForm()
	return render(request,'users/index.html',{'usfo':usfo})

def login(request):
	usfo=UserLoginForm(request.POST or None)
	err=None
	if request.method=='POST':
		if usfo.is_valid():
			email=usfo.cleaned_data.get('email')
			password=usfo.cleaned_data.get('password')
			user=authenticate(email=email,password=password)
			if user==None:
				# raise forms.ValidationError({'bark_volume': ["Must be louder!",]})
				err="Invalid login credentials"
			if user:
				if user.is_active:
					auth_login(request,user,backend='users.backend.NewBackend')
					print(request.user.name,request.user.email)
					return HttpResponseRedirect(reverse('simp'))
				else:
					return HttpResponse("Your account is inactive.")
	return render(request,'users/login.html',{'usfo':usfo,'err':err})

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
	# data=Food.objects.all()
	# list_data=[]
	# for d in data:
	# 	dic={}
	# 	dic['name']=d.user.name
	# 	dic['email']=d.user.email
	# 	dic['longitude']=d.longitude
	# 	dic['latitude']=d.latitude
	# 	dic['description']=d.food_item_decription
	# 	dic['phone_number']=d.phone_number
	# 	list_data.append(dic)

	# print(json.dumps(list_data))
	# return JsonResponse(list_data, safe=False)
	# qs_json = serializers.serialize('json', list_data)
	# return HttpResponse(qs_json, content_type='application/json')
	return	render(request,'users/simple.html')

@login_required
def simp_api(request):
	data=Food.objects.all()
	list_data=[]
	for d in data:
		dic={}
		dic['name']=d.user.name
		dic['email']=d.user.email
		dic['longitude']=d.longitude
		dic['latitude']=d.latitude
		dic['description']=d.food_item_decription
		dic['phone_number']=d.phone_number
		list_data.append(dic)

	# print(json.dumps(list_data))
	return JsonResponse(list_data, safe=False)
	# qs_json = serializers.serialize('json', list_data)
	# return HttpResponse(qs_json, content_type='application/json')
	# return	render(request,'users/simple.html')

@login_required
def simp1(request):
	if(request.method=="POST"):
		data=request.POST
		food_entry=Food()
		food_entry.user=request.user
		food_entry.food_item_decription=data['description']
		food_entry.latitude=data['latitide']
		food_entry.longitude=data['longitude']
		food_entry.phone_number=data['phone_number']
		food_entry.save()
		return HttpResponseRedirect(reverse('simp'))
	return	render(request,'users/simp1.html')



def logout(request):
	auth_logout(request)
	return HttpResponseRedirect(reverse('index'))


# import random
# def fun():
# 	a='4'
# 	while(a=='4'):
# 		print(random.choice(['a','b','c','d','e','f','g','h'])+random.choice(['1','2','3','4','5','6','7','8']))
# 		a=input()