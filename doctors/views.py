from django.shortcuts import render,redirect
from django.contrib import messages

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

from .forms import UserAddForm
from .decorators import doctor_only, not_auth_doctor

# Create your views here.



@doctor_only
def doctor_home(request):
    return render(request, "doctors/doctor-home.html")

@not_auth_doctor
def d_signup(request):  # first get the user form from forms.py to render with signup.html
    signup_form = UserAddForm()
    if(request.method == "POST"):
        form = UserAddForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("password")
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken !!! Retry")
                return redirect("d_signup")
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken !!! Retry")
                return redirect("d_signup")
            else:
                new_user = form.save()
                new_user.save()

                # getting and assigning group to the user
                group = Group.objects.get(name="doctors")
                new_user.groups.add(group)
                messages.info(request, "doctor Account Created")
                return redirect("d_signin")
        else:
            messages.info(
                request, "Fom validation Failed!!! Try a defferent password.")

    return render(request, "doctors/signup.html", {"signup_form": signup_form})


@not_auth_doctor
def d_signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session["username"] = username
            request.session["password"] = password
            login(request, user)
            return redirect("doctor_home")
        else:
            messages.info(request, "Username or password incorrect ")
            return redirect("d_signin")
    return render(request, "doctors/signin.html")

@doctor_only
def d_signout(request):
    logout(request)
    return redirect("d_signin")
