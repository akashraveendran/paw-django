from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from doctors.models import DoctorProfile

# Create your models here.




class PetProfile(models.Model):
    user_ID = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True )
    Pet_name = models.CharField(max_length=200,null=True,blank=True)
    Pet_category = models.CharField(max_length=200,null=True,blank=True)
    Pet_Breed = models.CharField(max_length=200,null=True,blank=True)
    Age = models.CharField(max_length=200,null=True,blank=True)
    Pet_photo = models.ImageField(upload_to="pets",null=True,blank=True)


class Booking(models.Model):
    Doctor_ID = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True )
    Patient_ID = models.IntegerField(null=True,blank=True )
    Doctor_Name = models.CharField(max_length=200,null=True,blank=True)
    Patient_Name = models.CharField(max_length=200,null=True,blank=True)
    Booking_Date = models.DateField(max_length=200,null=True,blank=True)
    Booking_Time = models.CharField(max_length=200,null=True,blank=True)
    Reason = models.CharField(max_length=200,null=True,blank=True)
    status = models.CharField(max_length=200,null=True,blank=True)



class Vaccination(models.Model):
    user_ID = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True )
    Pet_name = models.CharField(max_length=200,null=True,blank=True)
    Vaccination_Name = models.CharField(max_length=200,null=True,blank=True)
    Vaccinated_Date = models.CharField(max_length=200,null=True,blank=True)
    Vaccination_Document = models.FileField(upload_to="vaccines",max_length=200,null=True,blank=True)