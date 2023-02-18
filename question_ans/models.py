from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# # Create your models here.

class Question(models.Model):
    que_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    content = models.TextField(default="")
    likes = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
class Answer(models.Model):
    ans_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    que_ans = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.TextField()
    likes = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)