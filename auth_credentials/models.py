from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# GENDER_CHOICES = (
#     ('1','Not Selected'),
#     ('2','MALE'),
#     ('3','FEMALE'),
#     ('4','OTHER'),
# )

class Users(models.Model):
    user_id = models.AutoField(primary_key=True) 
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)
    user_first_name = models.CharField(max_length=20,default="")
    user_last_name = models.CharField(max_length=20,default="")
    gender = models.CharField(max_length=20,default="Not Selected")
    contact_no = models.CharField(max_length=13,default="")
    address = models.CharField(max_length=60,default="")
    status = models.CharField(max_length=20,default="Active")
    user_email = models.EmailField(max_length=30)
    user_image = models.ImageField(upload_to='Images',default="Images/auser.png")
    asked_que = models.IntegerField(default=0)
    user_date_join = models.DateTimeField(default=timezone.now)
    profession = models.CharField(max_length=200,default="Student")
    about_user = models.CharField(max_length=500,default="")
