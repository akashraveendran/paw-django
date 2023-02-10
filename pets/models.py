from django.db import models

# Create your models here.
from django.contrib.auth.models import User


# Create your models here.




class PetProfile(models.Model):
    user_ID = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True )
    Pet_name = models.CharField(max_length=200,null=True,blank=True)
    Pet_category = models.CharField(max_length=200,null=True,blank=True)
    Pet_Breed = models.CharField(max_length=200,null=True,blank=True)
    Age = models.CharField(max_length=200,null=True,blank=True)
    Pet_photo = models.ImageField(upload_to="pets",null=True,blank=True)