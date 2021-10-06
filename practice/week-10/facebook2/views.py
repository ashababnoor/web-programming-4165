from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Story
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
	context = { 
		'posts': Story.objects.all().order_by('-date')
	}
	return render(request, 'facebook2/index.html', context)

def profile(request):
	# id = request.user.email
	return render(request, 'facebook2/profile.html')

def signin(request):
	if (request.method == 'GET'):
		return render(request, 'facebook2/signin.html')
	elif (request.method == 'POST'):
		u = request.POST.get('user', '')
		p = request.POST.get('pass', '')
		user = authenticate(username=u, password=p)
		if user is None:
			messages.error(request, 'Invalid username or password')
			# messages.info(request, 'extra info')
			return render(request, 'facebook2/signin.html')
		else:
			login(request, user)
			return redirect('home-page')

def signout(request):
	logout(request)
	return redirect('signin')
