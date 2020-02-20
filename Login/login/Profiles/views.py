from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def ProfileDashBoard(request):
    return render(request, 'dashboard.html')
