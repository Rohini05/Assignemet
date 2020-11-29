from django.db import models
from django.contrib.auth.models import User
class extendeduser(models.Model):
    fullname = models.CharField(max_length=20)
    Category_CHOICES = (
   ('S', 'Student'),
   ('T', 'Teacher')
    )
    profile = models.CharField(choices=Category_CHOICES, max_length=128)
    user= models.OneToOneField(User,on_delete=models.CASCADE)
