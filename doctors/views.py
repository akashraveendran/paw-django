from django.shortcuts import render,redirect
from django.contrib import messages

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

from .forms import UserAddForm,DoctorProfieForm
from .models import DoctorProfile
from pets.models import Booking,PetProfile

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


@doctor_only
def add_doctor_profile(request):
    form = DoctorProfieForm()
    if request.method == "POST":
        add_form = DoctorProfieForm(request.POST,request.FILES)
        if(add_form.is_valid()):
            doctor = User.objects.get(id=request.user.id)
            updated_profile = add_form.save()
            updated_profile.doctor_ID = doctor
            updated_profile.save()
            return redirect("doctor_home")
    return render(request, "doctors/add-profile.html",{"form":form})

@doctor_only
def view_doctor_profile(request):
    doctor = DoctorProfile.objects.filter(doctor_ID=request.user.id)
    if(len(doctor) == 0):
        return redirect("add_doctor_profile")
    return render(request,"doctors/doctor-profile.html",{"doctor":doctor[0]})

@doctor_only
def view_doctor_appoinments(request):
    all_bookings = Booking.objects.filter(Doctor_ID=request.user.id)
    return render(request,"doctors/appoinments.html",{"all_bookings":all_bookings})


@doctor_only
def view_patient(request,id):
    patient = PetProfile.objects.get(id=id)
    return render(request,"doctors/patient-profile.html",{"pet":patient})

@doctor_only
def cancel_booking(request,id):
    booking = Booking.objects.get(id=id)
    booking.status = "Cancelled By Doctor"
    booking.save()
    return redirect("view_doctor_appoinments")