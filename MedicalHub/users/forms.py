from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# from .models import Profile

class UserRegisteration(UserCreationForm):
    usable_password = None
    is_staff_field = forms.CharField(required=False, label='Staff Member ', max_length=1)

 

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','is_staff_field')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            # 'phone': forms.TextInput(attrs={'placeholder': 'phone number'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }
        help_texts = {
            'username': None,
            'email': None,
        }

    def __init__(self, *args, **kwargs):
        super(UserRegisteration, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ""
        self.fields['password2'].help_text = ""

    def clean_is_staff_field(self):
        staff_input = self.cleaned_data.get('is_staff_field')
        if staff_input and staff_input.upper() == 'S':
            return staff_input
        return ''  