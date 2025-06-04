from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class QuickRegistrationForm(UserCreationForm):
    """A simplified registration form for quick user creation."""
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make the form simpler and more user-friendly
        self.fields['username'].help_text = 'Choose a username'
        self.fields['password1'].help_text = 'Choose a password'
        self.fields['password2'].help_text = 'Confirm your password' 