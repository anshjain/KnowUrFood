from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Sign Up Form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional',
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name', 'autocomplete': 'off',
                                                               'class': 'w3-input w3-border'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional',
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'autocomplete': 'off',
                                                              'class': 'w3-input w3-border'})
                                )

    email = forms.EmailField(max_length=254, help_text='Enter a valid email address',
                             widget=forms.TextInput(attrs={'placeholder': u'Email', 'class': 'w3-input w3-border'})
                             )

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'autocomplete': 'off',
                                                                 'class': 'w3-input w3-border'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'autocomplete': 'off',
                                                                  'class': 'w3-input w3-border'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': u'Username', 'class': 'w3-input w3-border'}),
        }