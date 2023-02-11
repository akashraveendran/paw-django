from django.shortcuts import render,redirect
from django.contrib import messages

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

from .forms import UserAddForm,AddPetForm
from .models import PetProfile

from .decorators import pet_only, not_auth_pet

# Create your views here.


def index(request):
    return render(request, "home.html")

@pet_only
def pet_home(request):
    return render(request, "pets/pet-home.html")

@not_auth_pet
def signup(request):  # first get the user form from forms.py to render with signup.html
    signup_form = UserAddForm()
    if(request.method == "POST"):
        form = UserAddForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("password")
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken !!! Retry")
                return redirect("signup")
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken !!! Retry")
                return redirect("signup")
            else:
                new_user = form.save()
                new_user.save()

                # getting and assigning group to the user
                group = Group.objects.get(name="pets")
                new_user.groups.add(group)
                messages.info(request, "Pet Account Created")
                return redirect("signin")
        else:
            messages.info(
                request, "Fom validation Failed!!! Try a defferent password.")

    return render(request, "pets/signup.html", {"signup_form": signup_form})


@not_auth_pet
def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session["username"] = username
            request.session["password"] = password
            login(request, user)
            return redirect("pet_home")
        else:
            messages.info(request, "Username or password incorrect ")
            return redirect("signin")
    return render(request, "pets/signin.html")

@pet_only
def signout(request):
    logout(request)
    return redirect("signin")

@pet_only
def add_user_profile(request):
    form = AddPetForm()
    if request.method == "POST":
        add_form = AddPetForm(request.POST,request.FILES)
        if(add_form.is_valid()):
            user = User.objects.get(id=request.user.id)
            updated_profile = add_form.save()
            updated_profile.user_ID = user
            updated_profile.save()
            return redirect("pet_home")
    return render(request, "pets/add-profile.html",{"form":form})

@pet_only
def view_user_profile(request):
    pet = PetProfile.objects.filter(user_ID=request.user.id)
    if(len(pet) == 0):
        return redirect("add_user_profile")
    return render(request,"pets/pet-profile.html",{"pet":pet[0]})