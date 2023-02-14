from django.forms import TextInput,ModelForm,DateInput
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import PetProfile,Booking

class UserAddForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username",
                  "email", "password1", "password2"]
        widgets = {
            'username': TextInput(attrs={"class":"form-control"}),
            
            'email': TextInput(attrs={"class":"form-control"}),
        }
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({"class":"form-control"})
        self.fields["password2"].widget.attrs.update({"class":"form-control"})


class AddPetForm(ModelForm):
    class Meta:
        model = PetProfile
        fields = ["Pet_name","Pet_category","Pet_Breed","Age","Pet_photo"]

        widgets = {
            'Pet_name': TextInput(attrs={"class":"contact-input"}),
            'Pet_category': TextInput(attrs={"class":"contact-input"}),
            'Pet_Breed': TextInput(attrs={"class":"contact-input"}),
            'Age': TextInput(attrs={"class":"contact-input"}),
        }

class AddBookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ["Booking_Date","Booking_Time","Reason"]

        widgets = {
            'Booking_Date': DateInput(attrs={"class":"contact-input",'type': 'date'}),
            'Booking_Time': TextInput(attrs={"class":"contact-input",'type': 'time'}),
            'Reason': TextInput(attrs={"class":"contact-input"}),
        }