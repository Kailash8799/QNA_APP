from django.db import models
# from datetime import datetime
from django.utils import timezone
# Create your models here.

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=30)
    user_password = models.CharField(max_length=20)
    user_image = models.ImageField(upload_to='Images',default="auser.png")
    user_date_join = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.user_name