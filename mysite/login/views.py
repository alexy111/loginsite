from django.shortcuts import render
from django.shortcuts import redirect
from login import models,forms
import hashlib
# Create your views here.
def hash_code(plain,salt="alex"):
    h = hashlib.sha256()
    plain += salt
    h.update(plain.encode())
    return h.hexdigest()


def index(requset):
    pass
    return render(requset,'login/index.html')

def login(request):
    if request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == "POST":
#        username = request.POST.get("username")
#        password = request.POST.get("password")
        login_form = forms.UserForm(request.POST)
        #message = "All fields need to be filled"
#        if username and password:
#            username = username.strip()
#            try:
#                user = models.User.objects.get(name=username)
#                if user.password == password:
#                    return redirect("/index/")
#                else:
#                   message = "password is wrong!"
#            except:
#                message = "user is not exist!"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            #captcha  = login_form.cleaned_data['captcha']
            try:
                user = models.User.objects.get(name=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect("/index/")
                else:
                   message = "password is wrong!"
            except:
                message = "user is not exist!"

        return render(request,'login/login.html',locals())
    login_form = forms.UserForm()
    return render(request, 'login/login.html',locals())

def register(request):
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if not password1 == password2:
                message = "password is not match!"
                return render(request,'login/register.html',locals())
            else:
                if models.User.objects.filter(name=username):
                    message = "This name is registered!"
                    return render(request, 'login/register.html', locals())
                if models.User.objects.filter(email=email):
                    message = "This email is registered!"
                    return render(request, 'login/register.html', locals())
                new_user = models.User()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')
    register_form = forms.RegisterForm()
    return render(request,'login/register.html',locals())

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/index/")
    request.session.flush()
    return redirect("/index/")