from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .models import *
from django.contrib.auth.models import User
import json
from django.core import serializers

def home(request):
	template_name = 'tracker/home.html'
	return render(request, template_name)


def create_trip(request):
	template_name = 'tracker/create_trip.html'

	if request.method == 'POST':
		data_keys = request.POST.keys()

		#print(request.POST.get('date'))
		new_trip = Trip.objects.create(mileage_user=request.user.mileage_user, date=request.POST.get('date'))

		for input_name in data_keys:
			if input_name.startswith('stop'):
				input_num = input_name[-1]
				if len(input_name) == 6:
					input_num = input_name[-2]

				new_stop = Stop.objects.create(place_id=request.POST.get(input_name), number=input_num, trip=new_trip)

		return HttpResponse('Success!')
	else:
		if request.user.is_authenticated:
			places = Place.objects.all()
			mileage_user = request.user.mileage_user
			last_date = None
			if mileage_user.last_date:
				last_date = mileage_user.last_date

			exists = bool(last_date)

			return render(request, template_name, {'places_json':serializers.serialize('json', places),'places':places, 'last_date': {'exists':exists, 'date':last_date}})
		else:
			return HttpResponseRedirect('/register')

def register(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		if len(User.objects.filter(username=username)) < 1:
			user = User.objects.create_user(username=username, password=password)
			MileageUser.objects.create(user=user)

			login(request, user)
			return HttpResponseRedirect('/')
		else:
			return HttpResponse('That username is already taken')
	else:
		return render(request, 'tracker/register.html')

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request=request, username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponse("Your account is disabled.")
		else:
			print("Invalid login details")
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'tracker/login.html', {})

def user_logout(request):
	logout(request)
	return render(request, 'tracker/home.html', {})

def view_mileage(request):
	return render(request, 'tracker/view_mileage.html')
