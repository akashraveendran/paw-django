from django.forms import forms,TextInput,PasswordInput,ModelForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class UserAddForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  "email", "password1", "password2"]
        widgets = {
            'username': TextInput(attrs={'placeholder':'Enter Username'}),
            'first_name': TextInput(attrs={'placeholder':'Enter Firstname'}),
            'last_name': TextInput(attrs={'placeholder':'Enter Lastname'}),
            'email': TextInput(attrs={'placeholder':'Enter Email'}),
        }
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({'placeholder':"Enter Password"})
        self.fields["password2"].widget.attrs.update({'placeholder':"Confirm Password"})
