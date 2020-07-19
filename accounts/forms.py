from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django_countries import countries


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password2 != password1:
            raise forms.ValidationError('passwords do not match')

    '''def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Are you sure you are registered! We are unable to find this user.")
        return username'''

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_count = User.objects.filter(email=email).count()
        if user_count > 0:
            raise forms.ValidationError(
                "This email has already been registered.")
        return email

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')


class ChangeNameForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', required=False)

    last_name = forms.CharField(label='Last Name', required=False,)

    Country = forms.ChoiceField(choices=list(countries))

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'Door_flat',
                  'Street', 'City', 'State', 'Country', 'Pincode']


class ChangeUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class ProfilePictureFrom(forms.ModelForm):
    profile_pic = forms.ImageField(
        label='Upload Profile Picture', required=False, widget=forms.FileInput(
            attrs={
                'class': 'profile-pic',
                'placeholder': 'Change Profile Pic'
            }
        ))

    class Meta:
        model = Profile
        fields = ('profile_pic',)


class AddAddressForm(forms.ModelForm):
    Country = forms.ChoiceField(choices=list(countries))

    class Meta:
        model = Profile
        fields = ['Door_flat',
                  'Street', 'City', 'State', 'Country', 'Pincode']
