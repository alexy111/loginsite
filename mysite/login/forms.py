from django import forms
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    username = forms.CharField(label="username",max_length=128,widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="password",max_length=256,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    captcha  = CaptchaField(label="code")

class RegisterForm(forms.Form):
    gender = (
        ('male', "man"),
        ('female', "woman"),
    )
    username = forms.CharField(label="username",max_length=128,widget=forms.TextInput(attrs={"class":"form-control"}))
    password1 = forms.CharField(label="password1",max_length=256,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(label="password2",max_length=256,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    email    = forms.EmailField(label="email",widget=forms.EmailInput(attrs={"class":"form-control"}))
    sex      = forms.ChoiceField(label="sex",choices=gender)
    captcha  = CaptchaField(label='code')



