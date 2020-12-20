from django.db import models
from django_mysql.models import ListCharField
from Home.models import User
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)  
    date = models.CharField(max_length=20,default="")
    time =  models.CharField(max_length=40,default="")
    job_title = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    difficulty = models.CharField(max_length=10)
    experience = models.CharField(max_length=200)
    questions = ListCharField(
        base_field=models.CharField(max_length=40),
        max_length=(20 * 40)
    )

    def __str__(self):
        return self.date
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=50)

    def __str__(self):
        return self.comment[:10]

class FavouritePost(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    def __str__(self):
        return self.post.date


class Question(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    
    question = models.CharField(max_length=40,default="")
    subject = models.CharField(max_length=30,default="")
    
    def __str__(self):
        return self.question