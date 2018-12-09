from django import forms
from .models import Group
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class NewGroup(forms.ModelForm):
    class Meta:
        model = Group
        exclude = ('owner', 'members')
        # fields = ('name', 'description', 'category', 'max_num', 'months')

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')