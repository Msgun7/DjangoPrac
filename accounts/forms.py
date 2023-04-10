from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)
#기본적으로 제공하는 것들에 더해 email을 추가하기 위해 정의합니다.

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
