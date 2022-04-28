from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.
def register(req):
	if req.method == 'POST':
		form = UserRegistrationForm(req.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(req, f'Welcome, {username}!')
			return redirect('login')
	else:
		form = UserRegistrationForm()

	data = {'form':form}
	return render(req,'registration.html', data)
