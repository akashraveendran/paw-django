from django.forms import forms,TextInput,PasswordInput,ModelForm,Textarea
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import DoctorProfile

class UserAddForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  "email", "password1", "password2"]
        widgets = {
            'username': TextInput(attrs={"class":"form-control"}),
            'first_name': TextInput(attrs={"class":"form-control"}),
            'last_name': TextInput(attrs={"class":"form-control"}),
            'email': TextInput(attrs={"class":"form-control"}),
        }
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({"class":"form-control"})
        self.fields["password2"].widget.attrs.update({"class":"form-control"})


class DoctorProfieForm(ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ["Doctor_name","Specialised_In","Experience","Clinic_Name","Clinic_Address","About","Doctor_Photo"]

        widgets = {
            'Doctor_name': TextInput(attrs={"class":"contact-input"}),
            'Specialised_In': TextInput(attrs={"class":"contact-input"}),
            'Experience': Textarea(attrs={"class":"contact-input"}),
            'Clinic_Name': TextInput(attrs={"class":"contact-input"}),
            'Contact_Number': TextInput(attrs={"class":"contact-input"}),
            'Clinic_Address': Textarea(attrs={"class":"contact-input"}),
            'About': Textarea(attrs={"class":"contact-input"}),
        }