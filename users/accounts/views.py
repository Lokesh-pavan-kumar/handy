from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from .forms import *
from .tokens import account_activation_token
from django.core.files import File
import os


def home_view(request):
    return render(request, 'accounts/home.html')


def activation_sent_view(request):
    return render(request, 'accounts/activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true
        user.is_active = True
        # set signup_confirmation true
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'accounts/activation_invalid.html')


def signup_view(request):
    print(User.objects.filter(username=request.user))
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            # user can't login until link confirmed
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            # load a template like get_template()
            # and calls its render() method immediately.
            message = render_to_string('accounts/activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # method will generate a hash value with user related data
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')


def user_view(request):
    user = request.user
    return HttpResponse(user)


@login_required(login_url='login')
def settings_view(request):
    return render(request, 'accounts/settings.html')


@login_required(login_url='login')
def changepassword_view(request):
    user = request.user
    print('password is ' + user.password)
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            form.verify_pass()
            form.verify_login(request)
            user.password = form.cleaned_data[newpass]
    else:
        form = ChangePasswordForm()
        return render(request, 'accounts/changepassword.html', {'form': form})


@login_required(login_url='login')
def changedetails_view(request):
    if request.method == 'POST':
        form = ChangeDetailsForm(request.POST)
        if form.is_valid():
            request.user.username = form.cleaned_data['UserName']
            request.user.first_name = form.cleaned_data['FirstName']
            request.user.last_name = form.cleaned_data['LastName']
    form = ChangeDetailsForm()
    return render(request, 'accounts/changedetails.html', {'form': form})


@login_required(login_url='login')
def changeprofilepic_view(request):
    file = open(
        'D:/Academics/College/ASE/Project/handy/users/media/profile_images/default.jpg')
    myfile = File(file)
    if request.method == 'POST':
        user = request.user
        form = ProfilePictureFrom(request.POST, request.FILES, instance=user)
        if form.is_valid():
            if not request.FILES.get('profile_pic', False):
                print('No file')
                request.user.profile.profile_pic.save('default.jpg', myfile)
                return redirect('dashboard')
            else:
                form.save(commit=False)
                request.user.profile.profile_pic = request.FILES.get(
                    'profile_pic', False)
                form.save()
                return redirect('dashboard')
    form = ProfilePictureFrom()
    return render(request, 'accounts/ProfilePic.html', {'form': form})
