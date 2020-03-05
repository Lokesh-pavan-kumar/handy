from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('customer-login')
	else:
		form = UserRegistrationForm()
	return render(request, 'customers/register.html', {'form':form})


