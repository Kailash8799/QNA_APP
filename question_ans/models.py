from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# # Create your models here.

class Tags(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_name = models.CharField(max_length=20)
    t_used = models.IntegerField(default=0)
    def __str__(self):
        return self.t_name

class Question(models.Model):
    que_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    # tags = models.ForeignKey(Tags,on_delete=models.CASCADE)
    tags = models.CharField(max_length=500,default="Programming")
    content = HTMLField()
    likes = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)
    total_ans = models.IntegerField(default=0)
    total_views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
class Answer(models.Model):
    ans_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    que_ans = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = HTMLField()
    likes = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)


class Contact(models.Model):
    c_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    desc = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

