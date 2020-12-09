from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone_number= models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to = "Images/Profile_Pictures/") 


    def __str__(self):
        return self.name